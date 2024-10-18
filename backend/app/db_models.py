from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
import datetime

metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name =  Column(String(50), unique=False, nullable=False)
    surname = Column(String(50), unique=False, nullable=False)
    login = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(256), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, unique=False, nullable=False)
    title = Column(String(100), unique=False, nullable=False)
    content = Column(String(1000), unique=False, nullable=False)
    media_links = Column(String(1000))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
