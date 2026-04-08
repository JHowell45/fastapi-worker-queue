from app.deps.db import create_session
from app.models.users import create_random_user
from app.worker import celery


@celery.task
def create_random_user_task():
    session = create_session()
    session.add(create_random_user())
    session.commit()


@celery.task
def create_random_bulk_users_task(amount: int):
    session = create_session()
    for _ in range(amount):
        session.add(create_random_user())
    session.commit()
