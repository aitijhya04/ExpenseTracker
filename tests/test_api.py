from fastapi.testclient import TestClient
from app.main import app
from app.db import init_db
from app.db import engine
from sqlmodel import SQLModel
import os

client = TestClient(app)

def setup_module(module):
    # create tables in test DB (uses same DB path by default)
    SQLModel.metadata.create_all(engine)

def test_add_and_summary():
    # add expense
    resp = client.post("/api/add_expense", data={
        "amount": "123.45",
        "category": "Test",
        "date_str": "2025-10-01",
        "description": "pytest entry"
    }, allow_redirects=False)
    assert resp.status_code in (303, 307, 201)

    # get expenses listing
    r = client.get("/api/expenses")
    assert r.status_code == 200
    data = r.json()
    # there should be at least one entry
    assert any(item["category"] == "Test" for item in data)

    # get summary
    s = client.get("/api/summary")
    assert s.status_code == 200
    js = s.json()
    assert "total" in js and "per_category" in js
