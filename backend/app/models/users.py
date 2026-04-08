from datetime import datetime, timezone
from random import uniform
from typing import Any

from faker import Faker
from pgvector.sqlalchemy import VECTOR
from sqlalchemy.sql import func
from sqlmodel import DateTime, Field, SQLModel

EMBEDDING_SIZE: int = 500
faker = Faker()


def generate_random_embedding() -> list[float]:
    return [uniform(-1, 1) for _ in range(EMBEDDING_SIZE)]


class User(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    embedding: Any = Field(sa_type=VECTOR(EMBEDDING_SIZE))
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=DateTime,
        sa_column_kwargs={"server_default": func.now()},
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_type=DateTime,
        sa_column_kwargs={
            "onupdate": func.now(),
            "server_default": func.now(),
        },
        nullable=False,
    )


def create_random_user() -> User:
    return User(name=faker.name(), embedding=generate_random_embedding())
