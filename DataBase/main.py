import os
import importlib.util
import requests

BASE_URL = "http://127.0.0.1:5000/tables"
PROBLEMS_DIR = "Problems"
test_number = 1  

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
            return True
        else:
            print(f"❌ Error: Insertion failed, unexpected response: {response_data}")
            return False
    else:
        print(f"❌ Error inserting problem into DB: {response.json()}")
        return False

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

    problem_name = problem_folder.split('/')[-1]
    problem_description = ""
    test_dirs = [d for d in os.listdir(problem_folder) if os.path.isdir(os.path.join(problem_folder, d))]

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


    for test_dir in test_dirs:
        input_file = os.path.join(problem_folder, test_dir, "input.txt")
        expected_output_file = os.path.join(problem_folder, test_dir, "expected_output.txt")

        if not os.path.exists(input_file) or not os.path.exists(expected_output_file):
            print(f"❌ Skipping {test_dir} due to missing input or expected_output file.")
            continue

        with open(input_file, "r") as f:
            input_data = f.read().strip()

        problem_main_path = os.path.join(problem_folder, 'main.py')

        spec = importlib.util.spec_from_file_location("solve", problem_main_path)
        problem_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(problem_module)

        result = problem_module.solve()

        with open(expected_output_file, "w") as f:
            f.write(result)

        insert_test_case(problem_id, input_data, result, test_number)
        print(f"✅ Test from {test_dir} added successfully!")

        test_number += 1 


def process_problems():
    for problem_folder in os.listdir(PROBLEMS_DIR):
        problem_path = os.path.join(PROBLEMS_DIR, problem_folder)
        if os.path.isdir(problem_path):
            run_tests(problem_path)

if __name__ == "__main__":
    process_problems()
