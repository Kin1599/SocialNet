import psycopg2
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import UserDto, UserReg, UserDtoLogin
from app.db_models import User
from passlib.hash import pbkdf2_sha256


def passhash(password: str) -> pbkdf2_sha256.hash:
    return pbkdf2_sha256.hash(password)


def create_new_user(user: UserReg, db: Session):
    if db.query(User).filter(User.login == user.login).first():
        raise HTTPException(status_code=400, detail="Login claimed")

    new_user = User(name=user.name, surname=user.surname,
                    login=user.login, email=user.email,
                    password_hash=passhash(user.password))

    db.add(new_user)
    db.commit()
    return new_user

def user_login(user: UserDtoLogin, db: Session):
    our_user = db.query(User).filter(User.login == user.login).first()
    if not our_user:
        raise HTTPException(status_code=404, detail="Пользователя не существует!")
    if not pbkdf2_sha256.verify(user.password, our_user.password_hash):
        return {"error": "wrong pass"}
    return our_user
