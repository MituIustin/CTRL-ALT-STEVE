def solve():
    input_file = 'input.txt'  

    with open(input_file, 'r') as f:
        input_data = f.read().strip()

    a, b = map(int, input_data.split())

    result = a * b
    return str(result)
