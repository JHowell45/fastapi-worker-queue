from typing import Sequence

from fastapi import APIRouter
from sqlmodel import select

from app.deps.db import SessionDep
from app.models.users import User, create_random_user
from app.responses.users import UserPublic

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[UserPublic])
def get_users(session: SessionDep) -> Sequence[User]:
    return session.exec(select(User).limit(20).offset(0)).all()


@router.post("/create/random")
def create_random_user_route(session: SessionDep):
    user = create_random_user()
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
