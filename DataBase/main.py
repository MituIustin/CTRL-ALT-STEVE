import os
import importlib.util
import requests
from unittest.mock import patch
from io import StringIO

BASE_URL = "http://127.0.0.1:5000/tables"
PROBLEMS_DIR = "Problems"
test_number = 1  
problem_number = 0

def insert_row(table_name, row_data):
    response = requests.post(f"{BASE_URL}/{table_name}/rows", json={"row": row_data})
    if response.status_code == 200:
        print(f"✅ Row inserted into {table_name} successfully!")
    else:
        print(f"❌ Error inserting row into {table_name}: {response.json()}")

def insert_problem(problem_name, description, difficulty='medium'):
    row_data = {
        "title": problem_name,
        "description": description,
        "difficulty": difficulty
    }

    print(f"⏳ Inserting problem: {problem_name}...")

    response = requests.post(f"{BASE_URL}/problems/rows", json={"row": row_data})

    if response.status_code == 200:
        response_data = response.json()
        if 'message' in response_data and 'successfully' in response_data['message']:
            print(f"✅ Problem '{problem_name}' added to database successfully!")

            problem_id = get_problem_id_by_title(problem_name)
            if problem_id:
                return problem_id
            else:
                print(f"❌ Error: Could not find 'problem_id' for '{problem_name}' after insertion.")
                return None
        else:
            print(f"❌ Error: Insertion failed, unexpected response: {response_data}")
            return None
    else:
        print(f"❌ Error inserting problem into DB: {response.json()}")
        return None

def get_problem_id_by_title(problem_name):
    response = requests.get(f"{BASE_URL}/problems/rows")

    if response.status_code == 200:
        rows = response.json().get('rows')
        for row in rows:
            if row[1] == problem_name:
                return row[0]  

        print(f"❌ Error: Problem with title '{problem_name}' not found in the database.")
        return None
    else:
        print(f"❌ Error fetching problems from DB: {response.json()}")
        return None


def insert_test_case(problem_id, input_data, expected_output, test_number):
    row_data = {
        "problem_id": problem_id,
        "test_number": test_number, 
        "input_data": input_data,
        "expected_output": expected_output
    }
    insert_row("test_cases", row_data)

def run_tests(problem_folder):
    global test_number

    problem_name = os.path.basename(problem_folder)
    problem_description = ""

    problem_txt_path = os.path.join(problem_folder, "problem.txt")
    if not os.path.exists(problem_txt_path):
        print(f"❌ Error: 'problem.txt' missing for {problem_name}. Skipping this problem.")
        return

    with open(problem_txt_path, "r") as f:
        problem_description = f.read().strip()

    problem_id = insert_problem(problem_name, problem_description)

    if problem_id is None:
        print(f"❌ Skipping {problem_name}: Could not insert problem into DB.")
        return

    problem_main_path = os.path.join(problem_folder, 'main.py')

    if not os.path.exists(problem_main_path):
        print(f"❌ Error: 'main.py' missing in {problem_name}. Skipping this problem.")
        return

    spec = importlib.util.spec_from_file_location("problem_module", problem_main_path)
    problem_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(problem_module)

    if hasattr(problem_module, "run_all_tests"):
        print(f"Running tests for {problem_name}...")
        problem_module.run_all_tests(problem_id)  
    else:
        print(f"❌ Error: 'run_all_tests()' not found in {problem_name}/main.py")


def process_problems():
    for problem_folder in os.listdir(PROBLEMS_DIR):
        problem_path = os.path.join(PROBLEMS_DIR, problem_folder)
        if os.path.isdir(problem_path):
            run_tests(problem_path)

if __name__ == "__main__":
    process_problems()
