from crud_table import *
from crud_row import *

def create_row_example():
    result = insert_row("students", {"name": "John", "age": 22})
    print(result)

def create_table_example():
    result = create_table("students", [
        {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
        {"name": "name", "type": "TEXT"},
        {"name": "age", "type": "INTEGER"}
    ])
    print(result)

def delete_row_example():
    result = delete_row("students", "age < 20")
    print(result)

def delete_table_example():
    result = delete_table("students")
    print(result)

def edit_row_example():
    result = update_row("students", {"name": "Jonathan", "age": 23}, "id = 1")
    print(result)

def edit_table_example():
    result = modify_table("students", add_columns=[{"name": "grade", "type": "TEXT"}], drop_columns=["age"])
    print(result)

def read_row_example():
    result = select_rows("students", columns=["id", "name"], condition="age > 20")
    print(result)

def read_table_example():
    result = list_tables()
    print(result)

if __name__ == "__main__":
    read_table_example()
