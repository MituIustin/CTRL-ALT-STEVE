import os
import requests

API_URL = "http://localhost:5000/tables/test_cases/rows"  

def solve(input_file):
    with open(input_file, 'r') as f:
        input_data = f.read().strip()

    a, b = map(int, input_data.split())
    result = a * b
    return str(result)

def run_all_tests(problem_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    test_folders = [d for d in os.listdir(current_dir) if d.lower().startswith("test") and os.path.isdir(os.path.join(current_dir, d))]

    if not test_folders:
        print("❌ No test folders found.")
        return

    for test_folder in sorted(test_folders):  
        input_file = os.path.join(current_dir, test_folder, "input.txt")
        expected_output_file = os.path.join(current_dir, test_folder, "expected_output.txt")

        if not os.path.exists(input_file):
            print(f"⚠️ Skipping {test_folder}: No input.txt found.")
            continue

        with open(input_file, 'r') as f:
            input_data = f.read().strip()

        output = solve(input_file)

        with open(expected_output_file, 'w') as f:
            f.write(output)

        test_number = int(test_folder[4:])  

        payload = {
            "row": {
                "problem_id": problem_id,
                "test_number": test_number,
                "input_data": input_data,
                "expected_output": output
            }
        }

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                print(f"✅ {test_folder}: Test inserted into database successfully!")
            else:
                print(f"❌ {test_folder}: Failed to insert test. {response.json()}")
        except Exception as e:
            print(f"❌ {test_folder}: Error during API request - {str(e)}")
