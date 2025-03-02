import requests

BASE_URL = "http://127.0.0.1:5000/tables"

tables = [
    {
        "table_name": "users",
        "columns": [
            {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
            {"name": "username", "type": "TEXT UNIQUE NOT NULL"},
            {"name": "email", "type": "TEXT UNIQUE NOT NULL"},
            {"name": "password_hash", "type": "TEXT NOT NULL"},
            {"name": "created_at", "type": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"}
        ]
    },
    {
        "table_name": "problems",
        "columns": [
            {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
            {"name": "title", "type": "TEXT NOT NULL"},
            {"name": "description", "type": "TEXT NOT NULL"},
            {"name": "created_at", "type": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"}
        ]
    },
    {
        "table_name": "test_cases",
        "columns": [
            {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
            {"name": "problem_id", "type": "INTEGER NOT NULL"},
            {"name": "input_data", "type": "TEXT NOT NULL"},
            {"name": "expected_output", "type": "TEXT NOT NULL"},
            {"name": "FOREIGN KEY (problem_id)", "type": "REFERENCES problems(id) ON DELETE CASCADE"}
        ]
    },
    {
        "table_name": "submissions",
        "columns": [
            {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
            {"name": "user_id", "type": "INTEGER NOT NULL"},
            {"name": "problem_id", "type": "INTEGER NOT NULL"},
            {"name": "code", "type": "TEXT NOT NULL"},
            {"name": "score", "type": "INTEGER DEFAULT 0"},
            {"name": "created_at", "type": "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"},
            {"name": "FOREIGN KEY (user_id)", "type": "REFERENCES users(id) ON DELETE CASCADE"},
            {"name": "FOREIGN KEY (problem_id)", "type": "REFERENCES problems(id) ON DELETE CASCADE"}
        ]
    },
    {
        "table_name": "test_results",
        "columns": [
            {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
            {"name": "submission_id", "type": "INTEGER NOT NULL"},
            {"name": "test_case_id", "type": "INTEGER NOT NULL"},
            {"name": "passed", "type": "BOOLEAN NOT NULL"},
            {"name": "FOREIGN KEY (submission_id)", "type": "REFERENCES submissions(id) ON DELETE CASCADE"},
            {"name": "FOREIGN KEY (test_case_id)", "type": "REFERENCES test_cases(id) ON DELETE CASCADE"}
        ]
    }
]

for table in tables:
    response = requests.post(BASE_URL, json=table)

    if response.status_code == 200:
        print(f"{table['table_name']} created successfully!")
    else:
        print(f"Error creating {table['table_name']}: {response.json()}")
