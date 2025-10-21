import sqlite3

# Path to your database
db_path = "expenses.db"

# Connect and clear
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("DELETE FROM expense;")
conn.commit()
conn.close()

print("✅ All expense records cleared from expenses.db")
