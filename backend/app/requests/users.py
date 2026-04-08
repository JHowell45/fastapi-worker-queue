from pydantic import BaseModel, Field


class BulkRandomUserRequest(BaseModel):
    amount: int = Field(default=10, gt=0, le=300)
