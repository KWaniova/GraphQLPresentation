import typing
import strawberry

from enum import Enum

# resolvers
# enums in python strawberry


@strawberry.enum
class BookType(Enum):
    FANTASY = 'Fantasy'
    MYSTERY = 'Mystery'
    HISTORICAL = "Historical"


books = [
    {"id": 1, "title": "Harry Potter", "type": BookType.FANTASY},
    {"id": 2, "title": "Lord of The Rings", "type": BookType.FANTASY},
    {"id": 3, "title": "Ogniem i mieczem", "type": BookType.HISTORICAL}
]


@strawberry.type
class Book:
    id: strawberry.ID
    title: str
    type: BookType


def get_books() -> typing.List[Book]:
    return [Book(id=book['id'], title=book["title"], type=book["type"]) for book in books]


def get_books_by_type(type: BookType) -> typing.List[Book]:
    return [Book(id=book['id'], title=book["title"], type=book["type"]) for book in filter(lambda x: x['type'] == type, books)]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)

    @strawberry.field
    def bookByType(type: BookType) -> typing.List[Book]:
        return get_books_by_type(type)


schema = strawberry.Schema(query=Query)
