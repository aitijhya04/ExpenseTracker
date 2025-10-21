from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Expense Tracker - Mini Project")

# mount static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# include routers
from app.routers import expenses, views
app.include_router(expenses.router)
app.include_router(views.router)
