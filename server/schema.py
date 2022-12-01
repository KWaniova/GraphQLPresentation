from functools import reduce
import datetime
from typing import List,  Optional

import typing
import decimal
import strawberry

BOOKS_LOOKUP = {
    'Frank Herbert': [{
        'title': 'Dune',
        'date_published': '1965-08-01',
        'price': '5.99',
        'isbn': 9780801950773
    }],
}


@strawberry.type
class Book:
    title: str
    author: 'Author'
    date_published: datetime.date
    price: decimal.Decimal
    isbn: str


def get_books_by_author(root: 'Author') -> List['Book']:
    print("ROOT: ", root)
    stored_books = BOOKS_LOOKUP[root.name]

    return [Book(
        title=book.get('title'),
        author=root,
        date_published=book.get('date_published'),
        price=book.get('price'),
        isbn=book.get('isbn')
    ) for book in stored_books]


@strawberry.type
class Author:
    name: str
    books: List[Book] = strawberry.field(resolver=get_books_by_author)


@strawberry.type
class Group:
    name: Optional[str]  # groups of authors don't necessarily have names
    authors: List[Author]

    @strawberry.field
    def books(self) -> List[Book]:
        books = []

        for author in self.authors:
            books += get_books_by_author(author)

        return books


def get_authors(root) -> typing.List[Author]:
    return [Author(name=author) for author in BOOKS_LOOKUP]


def get_books():
    # print(reduce(lambda x, y: x+y, [[Book(title=book.get('title'),
    #              author=author,
    #              date_published=book.get(
    #     'date_published'),
    #     price=book.get('price'),
    #     isbn=book.get('isbn')) for book in BOOKS_LOOKUP[author]] for author in BOOKS_LOOKUP]))
    return reduce(lambda x, y: x+y, [[Book(title=book.get('title'),
                                           author=Author(name=author),
                                           date_published=book.get(
        'date_published'),
        price=book.get('price'),
        isbn=book.get('isbn')) for book in BOOKS_LOOKUP[author]] for author in BOOKS_LOOKUP])


@ strawberry.type
class Query:
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)
    books: typing.List[Book] = strawberry.field(resolver=get_books)


@ strawberry.type
class Mutation:
    @ strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        print(f'Adding {title} by {author}')

        return Book(title=title, author=author)

    @ strawberry.mutation  # nic nie zwraca
    def restart() -> None:
        print(f'Restarting the server')


schema = strawberry.Schema(query=Query, mutation=Mutation)
