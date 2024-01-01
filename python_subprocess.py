import subprocess
import argparse

def extract_numeric(text):
    for line in text.splitlines():
        if line.strip().isdigit() or (line.strip().lstrip('-').isdigit() and '-' in line):
            return int(line.strip())
    return 0

def run_firstpy(num, XX=7):
    command = ["python", "firstpy.py", "--num", str(num), "--XX", str(XX)]
    output = subprocess.run(command, capture_output=True)
    result = extract_numeric(output.stdout.decode('utf-8'))
    
    # Use argparse to get values from firstpy.py
    args = argparse.Namespace(num=num, XX=XX)
    
    if num == 100 and XX == 90:
        print("first run")
    elif num == -10 and XX == -90:
        print("second run")
    elif XX == 7:
        print("third run")
    else:
        print(f"another run with num={num} and XX={XX}")

    print(f"the input XX is {XX}")
    print("We are in the main function")
    print(result)
    print("Hello world!")
    print("---------------------------------------------")
    return result, args

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, help="Value for --num")
    parser.add_argument("--XX", type=int, help="Value for --XX")
    args = parser.parse_args()

    # Perform the original runs
    runs = [
        (100, 90),
        (-10, -90),
        (1, 7),  # Specify both num and XX for the third run
                # Add more runs as needed
    ]

    results = []
    for num, XX in runs:
        result, _ = run_firstpy(num, XX)
        results.append(result)

    # Handle additional run
    if args.num is not None and args.XX is not None:
        result, _ = run_firstpy(args.num, args.XX)
        results.append(result)
        print(f"Result for additional run: {result}")

    print("Results:")
    for i, result in enumerate(results, start=1):
        print(f"Result {i}: {result}")

    result_sum = sum(results)
    print(f"Summation of all results is: {result_sum}")   