from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pathlib import Path
import os

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

DBNAME = os.environ["DB_NAME"]
USER = os.environ["DB_USER"]
PASSWORD = os.environ["DB_PASSWORD"]
HOST = os.environ["DB_HOST"]
PORT = os.environ["DB_PORT"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DBNAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)