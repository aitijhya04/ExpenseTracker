from typing import Optional
import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./expenses.db")

# echo only if debug
engine = create_engine(DATABASE_URL, echo=os.getenv("DEBUG", "false").lower() in ("1", "true"))

def init_db():
    # import models to register them with SQLModel metadata
    from app.models import Expense
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    return Session(engine)
