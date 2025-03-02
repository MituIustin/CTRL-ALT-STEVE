import os
import sqlite3
from dotenv import load_dotenv

dotenv_path = os.path.join(os.getcwd(), '..', 'credentials.env')
load_dotenv(dotenv_path)
DB_NAME = os.getenv("DB_NAME")

# Create
def insert_row(table_name, columns_values):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    columns = ", ".join(columns_values.keys())
    placeholders = ", ".join("?" for _ in columns_values)
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    cursor.execute(query, tuple(columns_values.values()))
    conn.commit()
    conn.close()

    return {"message": f"Row inserted into '{table_name}' successfully!"}

"""
curl -X POST http://127.0.0.1:5000/tables/students/rows -H "Content-Type: application/json" -d "{\"data\": {\"name\": \"John Doe\", \"age\": 22}}"
"""

# Read
def select_rows(table_name, columns=None, condition=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    columns_str = ", ".join(columns) if columns else "*"
    query = f"SELECT {columns_str} FROM {table_name}"

    if condition:
        query += f" WHERE {condition}"

    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    return {"rows": rows}

"""
curl -X GET http://127.0.0.1:5000/tables/students/rows
"""

# Edit 
def update_row(table_name, columns_values, condition):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    set_clause = ", ".join([f"{col} = ?" for col in columns_values.keys()])
    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"

    cursor.execute(query, tuple(columns_values.values()))
    conn.commit()
    conn.close()

    return {"message": f"Row(s) updated in '{table_name}' successfully!"}

"""
curl -X PUT http://127.0.0.1:5000/tables/students/rows/1 -H "Content-Type: application/json" -d "{\"data\": {\"name\": \"John Smith\"}}"
"""

# Delete
def delete_row(table_name, condition):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = f"DELETE FROM {table_name} WHERE {condition}"

    cursor.execute(query)
    conn.commit()
    conn.close()

    return {"message": f"Row(s) deleted from '{table_name}' successfully!"}

"""
curl -X DELETE http://127.0.0.1:5000/tables/students/rows/1
"""