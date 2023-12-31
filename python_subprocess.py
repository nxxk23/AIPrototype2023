##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello World!)
import subprocess

if __name__ == "__main__":
    # Basic terminal command
    #subprocess.run(["ls", "-ltr"])  # look on file
    #subprocess.run(["rm", "-r", "/home/thisisninkspaces/testfolder1"])  # remove file

    # Capture the output of each subprocess.run command
    print(f"first run num=100 XX=90")
    output1 = subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"], capture_output=True)
    print(f"------------------------------------------------------------")
    print(f"second run num=-10 XX=-90")
    output2 = subprocess.run(["python", "firstpy.py", "--num", "-10", "--XX", "-90"], capture_output=True)
    print(f"------------------------------------------------------------")
    print(f"third run num=0")
    output3 = subprocess.run(["python", "firstpy.py", "--num", "0"], capture_output=True)
    print(f"------------------------------------------------------------")

    # Print the captured output for reference
    print("Output 1:", output1.stdout.decode('utf-8'))
    print("Output 2:", output2.stdout.decode('utf-8'))
    print("Output 3:", output3.stdout.decode('utf-8'))

    # Summation of the results
    result_sum = sum(map(int, [output1.stdout.decode('utf-8'), output2.stdout.decode('utf-8'), output3.stdout.decode('utf-8')]))

    print(f"Summation of results: {result_sum}")


