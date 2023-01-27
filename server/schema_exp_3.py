import typing
import strawberry
from strawberry.dataloader import DataLoader

# mutations
# docstrings
# methods of class (how to call them in client queries)
# data loaders


def get_author_for_book(root) -> "Author":
    book_from_database = list(filter(lambda x: x["id"] == root.id, books))[0]
    author = list(filter(lambda x: x["id"] ==
                         book_from_database['author_id'], authors))[0]
    return Author(id=author['id'], name=author["name"])


@strawberry.type(description="This is book class")
class Book:
    id: strawberry.ID
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)


def get_books_for_author(root):
    return [Book(id=book['id'], title=book["title"]) for book in filter(lambda x: x.get("author_id") == root.id, books)]


@strawberry.type
class Author:
    id: strawberry.ID
    name: str
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)

    @strawberry.field(description="This is author greeting function")
    def greeting(self, name: str) -> str:
        return f"Hello {name}. I am {self.name}"


# baza danych
books = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author_id": 1},
    {"id": 2, "title": "Lord of The Rings", "author_id": 2},
    {"id": 3, "title": "1984", "author_id": 3}
]

authors = [
    {"id": 1, "name": 'J.K.Rowling'},
    {"id": 2, "name": 'J. R. R. Tolkien'},
    {"id": 3, "name": 'G. Orwell'},
]


@strawberry.input(description="This is input type of object")
class AddBookForAuthor:
    title: str
    author_id: strawberry.ID


def get_authors() -> typing.List[Author]:
    return [Author(id=author['id'], name=author["name"]) for author in authors]


def get_books() -> typing.List[Book]:
    return [Book(id=book['id'], title=book["title"]) for book in books]


# DATA LOADERS
async def load_authors(keys) -> typing.List[Author]:
    found_authors = list(filter(lambda x: str(x["id"]) in keys, authors))
    return [Author(id=author['id'], name=author["name"]) for author in found_authors]


loader = DataLoader(load_fn=load_authors)


@strawberry.type
class Query:
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)
    books: typing.List[Book] = strawberry.field(resolver=get_books)

    @strawberry.field(description="This is example of query with params.")
    async def author(self, id: strawberry.ID) -> Author:
        return await loader.load(id)


@strawberry.type
class Mutation:

    @ strawberry.mutation(description="This is mutation for adding book")
    def add_book(self, inputBook: AddBookForAuthor) -> None:
        author = list(filter(lambda x: x.id == int(
            inputBook.author_id), get_authors()))[0]
        books.append(
            {"id": len(books) + 1, "title": inputBook.title, "author_id": author.id})


schema = strawberry.Schema(query=Query, mutation=Mutation)
