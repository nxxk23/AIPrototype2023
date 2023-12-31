##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello World!)
import subprocess

def run_command(command):
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    out, err = process.communicate()
    return out.strip()

if __name__ == "__main__":
    # Basic terminal command
    #subprocess.run(["ls", "-ltr"])  # look on file
    #subprocess.run(["rm", "-r", "/home/thisisninkspaces/testfolder1"])  # remove file

    # Run firstpy.py with different inputs
    commands = [
        ["python", "firstpy.py", "--num", "100", "--XX", "90"],
        ["python", "firstpy.py", "--num", "-10", "--XX", "-90"],
        ["python", "firstpy.py", "--num", "0"]
    ]

    results = []

    for command in commands:
        result = run_command(command)
        print(result)
        results.append(int(result))

    # Summation of results
    total_sum = sum(results)

    print(f"------------------------------------------------------------")
    print(f"Summation of results: {total_sum}")
