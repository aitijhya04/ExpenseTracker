from typing import Optional
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount: float
    category: str
    date: date
    description: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)