import sqlite3

DB_NAME = "database.db"

# Create
def create_table(table_name, columns):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    column_defs = ", ".join([f"{col['name']} {col['type']}" for col in columns])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"

    cursor.execute(query)
    conn.commit()
    conn.close()
    return {"message": f"Table '{table_name}' created successfully!"}

"""
curl -X POST http://127.0.0.1:5000/tables \
     -H "Content-Type: application/json" \
     -d '{
          "table_name": "students",
          "columns": [
              {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
              {"name": "name", "type": "TEXT"},
              {"name": "age", "type": "INTEGER"}
          ]
        }'
"""

# Read
def list_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return {"tables": tables}

"""
curl -X GET http://127.0.0.1:5000/tables
"""

def modify_table(table_name, add_columns=None, drop_columns=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if drop_columns:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]

        for col in drop_columns:
            if col not in column_names:
                return {"error": f"Column '{col}' does not exist in table '{table_name}'."}

        new_columns = [col for col in column_names if col not in drop_columns]
        new_columns_str = ", ".join(new_columns)
        temp_table_name = f"{table_name}_temp"

        cursor.execute(f"CREATE TABLE {temp_table_name} AS SELECT {new_columns_str} FROM {table_name}")

        cursor.execute(f"DROP TABLE {table_name}")
        cursor.execute(f"ALTER TABLE {temp_table_name} RENAME TO {table_name}")

    if add_columns:
        for col in add_columns:
            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {col['name']} {col['type']}")

    conn.commit()
    conn.close()
    return {"message": f"Table '{table_name}' modified successfully!"}

"""
curl -X PUT http://127.0.0.1:5000/tables/students \
     -H "Content-Type: application/json" \
     -d '{
          "add_columns": [
              {"name": "grade", "type": "TEXT"}
          ],
          "drop_columns": ["age"]
        }'
"""
# Delete
def delete_table(table_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    conn.close()
    return {"message": f"Table '{table_name}' deleted successfully!"}

"""
curl -X DELETE http://127.0.0.1:5000/tables/students
"""