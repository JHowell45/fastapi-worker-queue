from fastapi import APIRouter

from app.routers import utils, v1

router = APIRouter(prefix="/api")
router.include_router(v1.router)
router.include_router(utils.router)
