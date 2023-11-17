# **💻 Basic Linux Command Line**

### **1. การจัดการ Folder และ File 📁**


- สร้าง folder
    ```
    $mkdir {folder name}
    ```
    
- สร้าง file
    ```
    $vi {file name} #>> สร้าง editor file >> ไม่จะเป็นต้องเลือก folder
    # vi มี 2 โหมด คือ Modify & Command
    #press i to edit >> press esc
    # :wq to write and quit
    # :q! to quit >> do not save edit file
    ```
    
- เปลี่ยนชื่อ folder หรือ file
    ```
    $mv {folder เดิม} {folder ใหม่}
    ```
- ย้าย file หรือ folder
    ```
    $mv file ~/{folder name}/
    or
    $mv file ~/{folder name}/. #>> dot will represents the current directory
    ```
    
- เช็ค path ของ folder ที่กำลังดำเนินการอยู่ตำแหน่งปัจจุบัน
    ```
    $pwd
    ```
    
- เช็ครายละเอียดของ file
    ```
    $ls -ltr #>> บอก permission and create time
    ```
    
- ลบ folder or file
    ```
    $rmdir {folder name}
    $rm -rf {folder name}
    $rm {fileName.py}
    ```
    
- jump เข้า-ออก folder
    ```
    $cd {folder name} # >> jump into Folder
    $cd       #>> jump to start position
    $cd ..    #>> jump out 1 position 
    $cd ../.. #>> jump out 2 position  
    ```
    
- เรียกดู file/folder ใน Folder
    ```
    ls
    ```  
- copy file
    ```
    $cp ./{path ต้นทาง}/{path ปลายทาง}
    ```
    
