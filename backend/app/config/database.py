from sqlalchemy import create_engine
from decouple import config
from app.db_models import Base
from sqlalchemy.orm import Session

DB_USERNAME = config("DB_USERNAME")
DB_PASSWORD = config("DB_PASSWORD")
DB_NAME = config("DB_NAME")
DB_HOST = config("DB_HOST")

DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

def create_session():
    db_local = Session(bind=engine)
    try:
        yield db_local
    finally:
        db_local.close()
