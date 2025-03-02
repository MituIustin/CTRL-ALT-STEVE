import sqlite3
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.getcwd(), '..', 'credentials.env')
load_dotenv(dotenv_path)
DB_NAME = os.getenv("DB_NAME")

if DB_NAME is None:
    print("Error: DB_NAME environment variable is not set.")
    exit(1)

def create_database():
    if not os.path.exists(DB_NAME):
        try:
            conn = sqlite3.connect(DB_NAME)
            print(f"Database '{DB_NAME}' created successfully!")
        except sqlite3.Error as e:
            print(f"Error creating database: {e}")
        finally:
            if conn:
                conn.close()
    else:
        print(f"Database '{DB_NAME}' already exists.")

if __name__ == "__main__":
    create_database()
