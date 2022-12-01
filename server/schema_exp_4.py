import typing
import strawberry

# interface
# optional


@strawberry.interface
class MutationResponse:
    code: str
    success: bool
    message: typing.Optional[str]


@strawberry.type
class Query:
    book: None


@strawberry.input(description="This is input type of object")
class AddBookForAuthor:
    title: str
    author_id: strawberry.ID


@strawberry.type
class Mutation:
    @strawberry.mutation(description="This is mutation for adding book")
    def add_book(self, inputBook: AddBookForAuthor) -> None:
        return None


schema = strawberry.Schema(query=Query, mutation=Mutation)
