from fastapi import APIRouter, HTTPException, Depends
from app.db_requests import create_new_user, user_login
from app.models import UserDtoLogin, UserReg
from sqlalchemy.orm import Session
from app.config.database import create_session
from app.auth.auth_handler import signJWT, token_response


router = APIRouter(tags=['Auth'])

@router.post("/register")
def register_new_user(user: UserReg, db: Session = Depends(create_session)) -> dict[str, str]:
    new_user = create_new_user(user, db)
    return signJWT(new_user.id)

@router.post("/login")
def login(user: UserDtoLogin, db: Session = Depends(create_session)) -> dict[str, str]:
    log_user = user_login(user, db)
    if log_user.id:
        return signJWT(log_user.id)
    raise HTTPException(status_code=404, detail="Item Not Found")


