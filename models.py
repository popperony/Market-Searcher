from pydantic import BaseModel


class Queries(BaseModel):
    query: str


class Description(BaseModel):
    query: str
    description: str
