from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/utils")


@router.get("/healthcheck")
async def healthcheck() -> JSONResponse:
    return JSONResponse({"Ok": True})
