from fastapi import FastAPI, Depends
import uvicorn

from app.routers import auth_router, user_page_router
from app.auth.auth_bearer import JWTBearer
from app.db_models import Base
from app.config.database import engine

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(user_page_router.router)

@app.get("/", dependencies=[Depends(JWTBearer())], tags=[""])
def home():
    return {"message": f"Hello World!"}

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
