from celery import Celery

from app.deps.settings import get_settings

settings = get_settings()

celery = Celery(__file__, broker=str(settings.CELERY_URI))

if __name__ == "__main__":
    celery.start()
