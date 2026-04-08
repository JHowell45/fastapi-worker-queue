from pydantic import BaseModel


class UserPublic(BaseModel):
    id: int
    name: str
