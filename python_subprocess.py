##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello World!)
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
    parser.add_argument("--num1", type=int, default=100, help="Input for the first subprocess")
    parser.add_argument("--XX1", type=int, default=90, help="Input for the first subprocess")
    parser.add_argument("--num2", type=int, default=-10, help="Input for the second subprocess")
    parser.add_argument("--XX2", type=int, default=-90, help="Input for the second subprocess")
    parser.add_argument("--num3", type=int, default=0, help="Input for the third subprocess")
    parser.add_argument("--XX3", type=int, default=7, help="Input for the third subprocess")

    args = parser.parse_args()

    output1 = run_command(args)
    output2 = run_command(args)
    output3 = run_command(args)

    result_sum = output1 + output2 + output3
    print(f"Summation of results: {result_sum}")



