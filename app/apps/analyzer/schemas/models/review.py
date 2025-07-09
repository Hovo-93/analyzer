from datetime import datetime

from pydantic import BaseModel


class ReviewResponseSchema(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: datetime
