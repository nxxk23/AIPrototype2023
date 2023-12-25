import subprocess # for execute terminal command

if __name__ == "__main__":
    #basic terminal command
    #subprocess.run(["ls","-ltr"]) #look on file
    #subprocess.run(["rm","-r","/home/thisisninkspaces/testfolder1"]) # remove file
    print(f"first run num=100 XX=90")
    subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"])
    print(f"------------------------------------------------------------")
    print(f"first run num=-10 XX=-90")
    subprocess.run(["python", "firstpy.py", "--num" ,"-10", "--XX", "-90"])
    print(f"------------------------------------------------------------")
    print(f"first run num=0")
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print(f"------------------------------------------------------------")

    
    #use output from other program
    process_output = subprocess.Popen(["python","firstpy.py","--num","0"], #ดึง output ออกมาทำงานต่อแต่ต้อง decode ก่อน
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.PIPE)
    out, err = process_output.communicate()
    print(out.decode('utf-8'))
    print(len(out.decode('utf-8')))

    ##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello World!)