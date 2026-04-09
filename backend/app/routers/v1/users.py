from typing import Sequence

from fastapi import APIRouter
from sqlmodel import select

from app.deps.db import SessionDep
from app.jobs.users import create_random_bulk_users_task, create_random_user_task
from app.models.users import User, create_random_user
from app.requests.users import BulkRandomUserRequest
from app.responses.users import TaskResponse, UserPublic

router = APIRouter(prefix="/users")


@router.get("/", response_model=list[UserPublic])
async def get_users(session: SessionDep) -> Sequence[User]:
    return session.exec(select(User).limit(20).offset(0)).all()


@router.post("/create/random")
async def create_random_user_route(session: SessionDep):
    user = create_random_user()
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.post("/create/random/task", response_model=TaskResponse)
async def create_random_user_job_route(session: SessionDep) -> TaskResponse:
    create_random_user_task.delay()
    return TaskResponse(ok=True)


@router.post("/create/random/task/bulk", response_model=TaskResponse)
async def create_bulk_random_user_job_route(
    session: SessionDep, requests: BulkRandomUserRequest
) -> TaskResponse:
    create_random_bulk_users_task.delay(requests.amount)
    return TaskResponse(ok=True)
