# [🚩Python Subprocess 📝](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module)

💬 using python to command another program file
 ⇨ create using ```code python_subprocess.py``` file
## 1) the first modify
  ```
    if __name__ == "__main__":
    #basic terminal command
      subprocess.run(["ls","-ltr"]) #look on file
      subprocess.run(["rm","-r","/home/thisisninkspaces/testfolder1"]) # run python ไปลบ testfolder1 ที่อยู่ใน home
    #**ต้องใช้ pwd path ไม่ใช้ตัวหนอน**
  ```
  ⇨ พอเราลบไฟล์ไปแล้ว ถ้าเรารันอีกรอบก็จะรันไม่ได้แล้ว แต่ยัง ls ได้อยู่
    
## 2) the second modify
  ```
    if __name__ == "__main__":
      print(f"first run num=100 XX=90")
      subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"])
      print(f"------------------------------------------------------------")
      print(f"first run num=-10 XX=-90")
      subprocess.run(["python", "firstpy.py", "--num" ,"-10", "--XX", "-90"])
      print(f"------------------------------------------------------------")
      print(f"first run num=0")
      subprocess.run(["python", "firstpy.py", "--num", "0"])
      print(f"------------------------------------------------------------")
  ```
⇨ test run input: ```python python_subprocess.py```

⇨ output:
  ```
      first run num=100 XX=90
      We are in the main function
      900
      Hello World!
      ------------------------------------------------------------
      second run num=-10 XX=-90
      We are in the main function
      -90
      Hello World!
      ------------------------------------------------------------
      third run num=0
      We are in the main function
      0
      Hello World!
      ------------------------------------------------------------      
   ```
### hw1 ⇨ เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน Hello world!)
