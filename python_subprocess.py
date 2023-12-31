##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello World!)
import subprocess
import re

def run_firstpy(num, XX):
    print(f"Running firstpy.py with num={num} XX={XX}")
    result = subprocess.run(["python", "firstpy.py", "--num", str(num), "--XX", str(XX)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Extract numeric part using regular expression
    numeric_part = re.search(r'\b\d+\b', result.stdout.decode('utf-8').strip())
    
    if numeric_part:
        return int(numeric_part.group())
    else:
        return 0  # Return 0 if no numeric part is found

if __name__ == "__main__":
    # Basic terminal command
    #subprocess.run(["ls", "-ltr"])  # Look on file
    #subprocess.run(["rm", "-r", "/home/thisisninkspaces/testfolder1"])  # Remove file

    # Store output from each run
    outputs = []

    print(f"first run num=100 XX=90")
    outputs.append(run_firstpy(100, 90))

    print(f"------------------------------------------------------------")
    print(f"first run num=-10 XX=-90")
    outputs.append(run_firstpy(-10, -90))

    print(f"------------------------------------------------------------")
    print(f"first run num=0")
    outputs.append(run_firstpy(0, 0))

    print(f"------------------------------------------------------------")

    # Use output from other program
    process_output = subprocess.Popen(["python", "firstpy.py", "--num", "0"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    outputs.append(int(out.decode('utf-8').strip()))  # Convert output to int

    # Summation of the numeric values from the outputs
    total_sum = sum(outputs)
    print(f"Total sum of all outputs: {total_sum}")


