from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import date
from app.services import get_all_expenses, get_summary

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def homepage(request: Request, category: str | None = Query(None), start: str | None = Query(None), end: str | None = Query(None)):
    expenses = get_all_expenses()
    # apply category filter and date filters client-side
    if category:
        expenses = [e for e in expenses if e.category.lower() == category.lower()]
    start_date = date.fromisoformat(start) if start else None
    end_date = date.fromisoformat(end) if end else None
    if start_date:
        expenses = [e for e in expenses if e.date >= start_date]
    if end_date:
        expenses = [e for e in expenses if e.date <= end_date]
    summary = get_summary(start=start_date, end=end_date)
    categories = sorted({e.category for e in get_all_expenses()})
    return templates.TemplateResponse("index.html", {"request": request, "expenses": expenses, "summary": summary, "categories": categories})

@router.get("/summary_page", response_class=HTMLResponse)
def summary_page(request: Request, start: str | None = None, end: str | None = None):
    start_date = date.fromisoformat(start) if start else None
    end_date = date.fromisoformat(end) if end else None
    summary = get_summary(start=start_date, end=end_date)
    return templates.TemplateResponse("summary.html", {"request": request, "summary": summary, "start": start, "end": end})
