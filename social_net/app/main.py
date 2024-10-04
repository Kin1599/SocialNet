from fastapi import FastAPI, Body, Depends
import routers.auth_router
import uvicorn
from app.auth.auth_bearer import JWTBearer
from app.db_models import Base
from app.config.database import engine

app = FastAPI()

app.include_router(routers.auth_router.router)

@app.get("/", dependencies=[Depends(JWTBearer())], tags=[""])
def home():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
