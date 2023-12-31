import subprocess
import argparse

def extract_numeric(text):
    for line in text.splitlines():
        if line.strip().isdigit() or (line.strip().lstrip('-').isdigit() and '-' in line):
            return int(line.strip())
    return 0

def run_command(args):
    command = ["python", "firstpy.py", "--num", str(args.num), "--XX", str(args.XX)]
    output = subprocess.run(command, capture_output=True)
    result = extract_numeric(output.stdout.decode('utf-8'))
    print(f"Output for command {command}: {result}")
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run subprocesses and sum numeric output.")
    
    for i in range(1, 4):  # Assuming you want to handle 3 subprocesses, adjust the range accordingly
        parser.add_argument(f"--num{i}", type=int, default=0, help=f"Input for subprocess {i}")
        parser.add_argument(f"--XX{i}", type=int, default=0, help=f"Input for subprocess {i}")

    args = parser.parse_args()

    outputs = [run_command(args) for i in range(1, 4)]  # Assuming you want to handle 3 subprocesses
    result_sum = sum(outputs)
    
    print(f"Summation of results: {result_sum}")