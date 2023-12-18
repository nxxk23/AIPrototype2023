# **Run Python File 📃**
- data sciences ส่วนใหญ่จะอยู่ในรูปของ report แต่เวลาเราใช้งานจริงๆ จะอยู่ในรูปของ script
  
 > code แบบ .ipynb ที่สามารถเขียนและตกแต่งได้ มี header, section

 > code แบบ .py เป็น script สำหรับรัน

## Process this on CMD

![image](https://github.com/nxxk23/AIPrototype2023/assets/108257495/b659ead2-6f2a-4749-a436-bbf7f55aa58f)

**on nink@DESKTOP-AB2T90E:~/outside/ubuntu/AIPrototype2023$**
 * Step 1: Create file.py 
```
code firstpy.py #enter จะเปิด vscode ที่สามารถเขียนโค้ดลงไปได้ then press ctrl+s 
```
 * Step 2: Commit to GitHub
**make sure to bind your GitHub account first**
```
git pull
git add fisrtpy.py
git commit -m "{commit describe}"
git push #enter username and password of youe GH
```
 * Step 3: Test execute file
**on Virtual Machine path that we already ssh into server**
```
git pull
python firstpy.py
```

--- 

## [Test edit file (ครั้งที่ 2)](https://github.com/nxxk23/AIPrototype2023/commit/f86fd74746b7fd4fbcdfe10d8b2edf4ba46edb5f)
```
code {ชื่อไฟล์}  #create แต่ถ้าชื่อไฟล์ที่มีอยู่แล้วก็จะเปิดไฟล์ให้เราแก้ไข
```
```
git status #show file status that had been edited or created 
```
 * **after check status just do the same process to commit file**
```
git add fisrtpy.py
git commit -m "{commit describe}"
git push # save on internet
```
 * **on Virtual Machine path that we already ssh into server**
```
git pull
python firstpy.py
```
---

## [Test edit file (ครั้งที่ 3)](firstpy.py)
```
code {ชื่อไฟล์}  #create แต่ถ้าชื่อไฟล์ที่มีอยู่แล้วก็จะเปิดไฟล์ให้เราแก้ไข
```

📌 **เราจะไม่แก้โค้ดเพื่อ commit ใหม่ ปกติจะเปิดช่องให้คนใส่ input ได้**
```
cat firstpy.py #on vm >> display code in file
```

- this is the input:
  ```
  python firstpy.py --num1 -XX 10
  ```
- this is the output:
  ```
  the input XX is 10
  we are in the main function
  9
  Hello World!
  ```

