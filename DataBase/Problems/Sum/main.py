import os

def main():
    problem_dir = "Problem_1"
    test_dirs = [d for d in os.listdir(problem_dir) if os.path.isdir(os.path.join(problem_dir, d))]

    for test_dir in test_dirs:
        input_file = os.path.join(problem_dir, test_dir, "input.txt")
        expected_output_file = os.path.join(problem_dir, test_dir, "expected_output.txt")

        with open(input_file, "r") as f:
            num1 = int(f.readline().strip())
            num2 = int(f.readline().strip())

        result = num1 + num2

        with open(expected_output_file, "w") as f:
            f.write(str(result))

if __name__ == "__main__":
    main()
