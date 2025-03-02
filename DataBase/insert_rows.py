import os
import requests

BASE_URL = "http://127.0.0.1:5000/tables"
PROBLEMS_DIR = "Problems"

def insert_row(table_name, row_data):
    response = requests.post(f"{BASE_URL}/{table_name}/rows", json={"row": row_data})
    if response.status_code == 200:
        print(f"Row inserted into {table_name} successfully!")
    else:
        print(f"Error inserting row into {table_name}: {response.json()}")

def insert_tests(problem_folder):
    problem_name = problem_folder.split('/')[-1]
    test_dirs = [d for d in os.listdir(problem_folder) if os.path.isdir(os.path.join(problem_folder, d))]

    for test_dir in test_dirs:
        input_file = os.path.join(problem_folder, test_dir, "input.txt")
        expected_output_file = os.path.join(problem_folder, test_dir, "expected_output.txt")

        with open(input_file, "r") as f:
            input_data = f.read().strip()

        os.chdir(os.path.join(problem_folder)) 
        from main import solution
        result = solution()

        with open(expected_output_file, "w") as f:
            f.write(result)

        problem_id = insert_problem(problem_name, f"Description for {problem_name}")
        insert_test_case(problem_id, input_data, result)

        print(f"Test from {test_dir} added successfully!")

def insert_problem(name, description):
    row_data = {
        "name": name,
        "description": description
    }
    insert_row("problems", row_data)
    return 1  

def insert_test_case(problem_id, input_data, expected_output):
    row_data = {
        "problem_id": problem_id,
        "input_file": input_data,
        "expected_output_file": expected_output
    }
    insert_row("tests", row_data)

def process_problems():
    for problem_folder in os.listdir(PROBLEMS_DIR):
        problem_path = os.path.join(PROBLEMS_DIR, problem_folder)
        if os.path.isdir(problem_path):
            insert_tests(problem_path)

if __name__ == "__main__":
    process_problems()
