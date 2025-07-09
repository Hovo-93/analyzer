"""
    API request Schemas.
    Schemas are divided between schemas for query params and for json bodies.
        - Schemes for query params are called like this SQP<Name>
        - The schemas for json data in the request body are called like this SJB<Name>
"""
from pydantic import BaseModel, Field


class SJBReviewInput(BaseModel):
    text: str = Field(..., example="Очень люблю этот сервис!")


class SJBFilterInput(BaseModel):
    sentiment: str
