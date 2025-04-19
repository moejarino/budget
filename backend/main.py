from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define GraphQL types
@strawberry.type
class Transaction:
    id: int
    amount: float
    description: str
    date: str

# Define GraphQL queries
@strawberry.type
class Query:
    @strawberry.field
    def transactions(self) -> List[Transaction]:
        # This is a placeholder - we'll implement the actual database query later
        return [
            Transaction(id=1, amount=100.0, description="Test transaction", date="2024-04-14")
        ]

# Create schema
schema = strawberry.Schema(query=Query)

# Create FastAPI app
app = FastAPI()

# Add GraphQL endpoint
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root():
    return {"message": "Welcome to the Budget API"} 