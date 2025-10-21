# 💰 ExpenseTracker

A simple expense tracking web application built with **FastAPI**, **SQLModel**, and **SQLite**.  
You can add, view, and summarize expenses by category.

---

## 🚀 Features

- ➕ **Add new expenses** (amount, category, description, date)  
- 👀 **View all expenses**  
- 📊 **View summary** (total and per-category spending)  
- 🕒 **Automatically records creation timestamps**

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | FastAPI |
| **Database** | SQLite |
| **ORM** | SQLModel |
| **Templating** | Jinja2 |
| **Server** | Uvicorn |

---

## 🗂️ Project Structure
expense-tracker/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── models.py # SQLModel for Expense
│ ├── services.py # Database logic
│ ├── routers/
│ │ ├── expenses.py # API routes for expenses
│ │ └── views.py # Routes for HTML pages
│ ├── templates/
│ │ ├── index.html
│ │ ├── add_expense.html
│ │ └── summary.html
│ └── static/ # (Optional) CSS/JS files
│
├── requirements.txt # Python dependencies
├── pyproject.toml # (Optional) project metadata
├── README.md # Project documentation
└── venv/ # Virtual environment (not uploaded)


---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/expense-tracker.git
   cd expense-tracker

