from typing import Optional
import strawberry

# Optional parameters


@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: Optional[str] = None) -> str:
        if name is None:
            return "Hello world!"
        return f"Hello {name}!"

    @strawberry.field
    def greet(self, name: Optional[str] = strawberry.UNSET) -> str:
        if name is strawberry.UNSET:
            return "Name was not set!"
        if name is None:
            return "Name was null!"
        return f"Hello {name}!"


schema = strawberry.Schema(query=Query)
