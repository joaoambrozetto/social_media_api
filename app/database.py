import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from . import models


dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

DBNAME = os.environ["DB_NAME"]
USER = os.environ["DB_USER"]
PASSWORD = os.environ["DB_PASSWORD"]
HOST = os.environ["DB_HOST"]
PORT = os.environ["DB_PORT"]

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{USER}:{PASSWORD}@{HOST}/{DBNAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

def create_db_and_tables():
    models.Base.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session