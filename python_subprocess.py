#import subprocess # for execute terminal command

#if __name__ == "__main__":
    #basic terminal command
    #subprocess.run(["ls","-ltr"]) #look on file
    #subprocess.run(["rm","-r","/home/thisisninkspaces/testfolder1"]) # remove file
    #print(f"first run num=100 XX=90")
    #subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"])
    #print(f"------------------------------------------------------------")
    #print(f"first run num=-10 XX=-90")
    #subprocess.run(["python", "firstpy.py", "--num" ,"-10", "--XX", "-90"])
    #print(f"------------------------------------------------------------")
    #print(f"first run num=0")
    #subprocess.run(["python", "firstpy.py", "--num", "0"])
    #print(f"------------------------------------------------------------")

    
    #use output from other program
    #process_output = subprocess.Popen(["python","firstpy.py","--num","0"], #ดึง output ออกมาทำงานต่อแต่ต้อง decode ก่อน
                                      #stdout = subprocess.PIPE,
                                      #stderr = subprocess.PIPE)
    #out, err = process_output.communicate()
    #print(out.decode('utf-8'))
    #print(len(out.decode('utf-8')))

    ##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello World!)
import subprocess

def run_firstpy_and_get_output(num, XX):
    process_output = subprocess.Popen(["python", "firstpy.py", "--num", str(num), "--XX", str(XX)],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    return int(out.decode('utf-8').strip())

if __name__ == "__main__":
    sum_result = 0

    # First run
    result = run_firstpy_and_get_output(100, 90)
    print(f"First run num=100 XX=90, result={result}")
    sum_result += result
    print(f'----------------------------------------')

    # Second run
    result = run_firstpy_and_get_output(-10, -90)
    print(f"Second run num=-10 XX=-90, result={result}")
    sum_result += result
    print(f'----------------------------------------')

    # Third run
    result = run_firstpy_and_get_output(0, 0)
    print(f"Third run num=0, result={result}")
    sum_result += result
    print(f'----------------------------------------')

    # Use output from other program
    process_output = subprocess.Popen(["python", "firstpy.py", "--num", "0"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
    out, err = process_output.communicate()
    result = int(out.decode('utf-8').strip())

    print(f"Output from other program: {result}")
    sum_result += result
    print(f"Sum of all results: {sum_result}")