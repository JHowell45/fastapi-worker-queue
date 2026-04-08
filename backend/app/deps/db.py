from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session, create_engine

from app.deps.settings import get_settings

settings = get_settings()

engine = create_engine(str(settings.DB_URI))


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def create_session() -> Session:
    return get_session().__next__()


SessionDep = Annotated[Session, Depends(get_session)]
