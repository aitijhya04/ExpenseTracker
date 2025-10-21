from fastapi import APIRouter, Depends, Form, Request, HTTPException
from fastapi.responses import RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from datetime import date, datetime
import csv
import io

from app.db import init_db
from app.models import Expense
from app.services import add_expense, get_all_expenses, get_summary

router = APIRouter(prefix="/api", tags=["api"])
templates = Jinja2Templates(directory="app/templates")

# ensure DB present
init_db()

@router.post("/add_expense")
async def api_add_expense(amount: float = Form(...),
                          category: str = Form(...),
                          date_str: str = Form(...),
                          description: Optional[str] = Form(None)):
    """
    Accepts form-data and inserts into DB. date_str format: YYYY-MM-DD
    """
    try:
        d = date.fromisoformat(date_str)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    expense = Expense(amount=round(float(amount), 2), category=category, date=d, description=description)
    res = add_expense(expense)
    # redirect to homepage
    return RedirectResponse(url="/", status_code=303)

@router.get("/expenses")
def api_get_expenses():
    return get_all_expenses()

@router.get("/summary")
def api_get_summary(start: Optional[str] = None, end: Optional[str] = None):
    start_date = date.fromisoformat(start) if start else None
    end_date = date.fromisoformat(end) if end else None
    return get_summary(start=start_date, end=end_date)

@router.get("/export")
def api_export_csv(start: Optional[str] = None, end: Optional[str] = None):
    """Export filtered expenses as CSV"""
    start_date = date.fromisoformat(start) if start else None
    end_date = date.fromisoformat(end) if end else None
    data = get_all_expenses()
    if start_date:
        data = [d for d in data if d.date >= start_date]
    if end_date:
        data = [d for d in data if d.date <= end_date]

    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "amount", "category", "date", "description", "created_at"])
    for e in data:
        writer.writerow([e.id, e.amount, e.category, e.date.isoformat(), e.description or "", e.created_at.isoformat()])
    buffer.seek(0)
    headers = {"Content-Disposition": "attachment; filename=expenses.csv"}
    return StreamingResponse(buffer, media_type="text/csv", headers=headers)
