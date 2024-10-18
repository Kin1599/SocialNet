from pydantic import BaseModel, EmailStr

class UserPage(BaseModel):
    id: int
    username: str
    posts: list


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


class PostModel(BaseModel):
    uid: int = 0
    title: str = ""
    content: str = ""
    media_links: str = ""