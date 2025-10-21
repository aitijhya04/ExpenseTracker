# ExpenseTracker
A simple expense tracking web application built with FastAPI, SQLModel, and SQLite. You can add, view, and summarize expenses by category.

🚀 Features

Add new expenses (amount, category, description, date)

View all expenses

View summary (total and per-category spending)

Automatically records creation timestamps

🧩 Tech Stack

Backend: FastAPI

Database: SQLite

ORM: SQLModel

Templating: Jinja2

Server: Uvicorn

🗂️ Project Structure
expense-tracker/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── models.py            # SQLModel for Expense
│   ├── services.py          # Database logic
│   ├── routers/
│   │   ├── expenses.py      # API routes for expenses
│   │   └── views.py         # Routes for HTML pages
│   ├── templates/
│   │   ├── index.html
│   │   ├── add_expense.html
│   │   └── summary.html
│   └── static/              # (Optional) CSS/JS files
│
├── requirements.txt         # Python dependencies
├── pyproject.toml           # (Optional) project metadata
├── README.md                # Project documentation
└── venv/                    # Virtual environment (not uploaded)

⚙️ Setup Instructions

Clone the repository

git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker


Create & activate virtual environment

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run the application

uvicorn app.main:app --reload


Open in browser

http://127.0.0.1:8000

📊 Endpoints
Route	Method	Description
/	GET	Home page (list all expenses)
/add_expense_page	GET	Form to add a new expense
/add_expense	POST	Submit new expense
/summary_page	GET	Expense summary view
🧠 Author

Developed by Aitijhya Mondal
For educational purposes – FastAPI mini-project.
