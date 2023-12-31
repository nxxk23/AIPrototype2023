##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello World!)
import subprocess

def get_numeric_value(output):
    try:
        return int(output.strip())
    except ValueError:
        return 0

if __name__ == "__main__":
    # Basic terminal command
    #subprocess.run(["ls", "-ltr"])  # look on file
    #subprocess.run(["rm", "-r", "/home/thisisninkspaces/testfolder1"])  # remove file

    # Capture the output of each subprocess.run command
    output1 = subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"], capture_output=True)
    output2 = subprocess.run(["python", "firstpy.py", "--num", "-10", "--XX", "-90"], capture_output=True)
    output3 = subprocess.run(["python", "firstpy.py", "--num", "0"], capture_output=True)

    # Print the captured output for reference
    print("Output 1:", output1.stdout.decode('utf-8'))
    print("Output 2:", output2.stdout.decode('utf-8'))
    print("Output 3:", output3.stdout.decode('utf-8'))

    # Get numeric values and sum the results
    result_sum = sum([get_numeric_value(output1.stdout.decode('utf-8')),
                     get_numeric_value(output2.stdout.decode('utf-8')),
                     get_numeric_value(output3.stdout.decode('utf-8'))])

    print(f"Summation of results: {result_sum}")



