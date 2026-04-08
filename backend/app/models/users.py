from datetime import datetime, timezone
from typing import Any

from pgvector.sqlalchemy import VECTOR
from sqlalchemy.sql import func
from sqlmodel import DateTime, Field, SQLModel

EMBEDDING_SIZE: int = 500


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
