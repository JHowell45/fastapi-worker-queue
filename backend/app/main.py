import uvicorn
from fastapi import FastAPI

from app import routers

app = FastAPI(title="FastAPI Queue Example")
app.include_router(routers.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
