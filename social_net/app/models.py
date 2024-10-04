from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
    id: int = 0
    login: str = ""
    name: str = ""
    surname: str = ""
    email: EmailStr = ""
    pass_hash: str = ""


class UserReg(BaseModel):
    login: str = ""
    name: str = ""
    surname: str = ""
    email: EmailStr = ""
    password: str = ""


class UserDtoLogin(BaseModel):
    login: str = ""
    password: str = ""
