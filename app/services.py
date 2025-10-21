from app.models import Expense
from sqlmodel import Session, select
from sqlmodel import create_engine
from typing import Optional
from datetime import date

DATABASE_URL = "sqlite:///./expenses.db"
engine = create_engine(DATABASE_URL, echo=True)

def add_expense(expense: Expense):
    with Session(engine) as session:
        session.add(expense)
        session.commit()
        session.refresh(expense)
        return expense

def get_all_expenses():
    with Session(engine) as session:
        expenses = session.exec(select(Expense)).all()
        return expenses

def get_summary(start: Optional[date] = None, end: Optional[date] = None):
    with Session(engine) as session:
        query = select(Expense)
        if start:
            query = query.where(Expense.date >= start)
        if end:
            query = query.where(Expense.date <= end)
        expenses = session.exec(query).all()

        total = sum(e.amount for e in expenses)
        summary = {}
        for e in expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount
        return {"total": total, "by_category": summary}

