## 💰 ExpenseTracker

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

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ExpenseTracker.git
   cd expense-tracker
   
2. **Install Dependencies**
   ```python
   pip install -r requirements.txt

3. **Run the Application**
   ```python
   uvicorn app.main:app --reload

4. **Open in Browser**
   👉 http://127.0.0.1:8000

## 🌐 Endpoints Overview

| **Route**            | **Method** | **Description**                  |
|----------------------|------------|----------------------------------|
| `/`                  | GET        | Home page (list all expenses)    |
| `/add_expense_page`  | GET        | Form to add a new expense        |
| `/add_expense`       | POST       | Submit a new expense             |
| `/summary_page`      | GET        | Expense summary page             |


👨‍💻 Author : Aitijhya Mondal
Made with ❤️ using FastAPI, SQLite and HTML + Jinja2.

