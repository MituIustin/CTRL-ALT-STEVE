def check_interval(a, b, x):
    return "YES" if a <= x <= b else "NO"

def process_file(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            a, b, x = map(float, line.split())  
            result = check_interval(a, b, x)
            outfile.write(result + "\n")
        
if __name__ == "__main__":
    process_file("input.txt", "output.txt")
