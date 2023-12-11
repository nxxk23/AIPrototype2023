# **working on Virtual Machine Cloud ☁**

> install program into linux
```
linux ใช้ร่วมกันหลายๆ คน
  sudo install #จะอยู่ใน VM ของเรา
  แต่ถ้าอยากใช้คนเดียว ต้องสร้าง environment แยก
```

* โปรแกรมจัดการวิดีโอ ต่อรูปเป็นคลิป หรือแตกคลิปเป็น frame
```
$sudo snap install ffmpeg
```

* manual check
```
- man ffmpeg
- ffmpeg -h
- man ls
```

> **Create environment** + install python
```
conda create -n mypy38{ชื่อenvi} python=3.9 #(base) envi ของเราเป็น python 3.11.5
- conda activate mypy38
- conda deactivate
install python package
- conda install pandas #check
```
    *****เวลาเรา login เข้า vm จะสร้าง session ไว้ พอเราออก อะไรที่รันไว้มันจะหายไปเลย*****
---

> **Create Screen**
* สร้าง session
```
screen -S sc1 (สร้างสกรีนชื่อ sc1)
#screen คำสั่งสำหรับการสร้าง session ขึ้นมาอีกอัน แล้วก็รันต่อไปเรื่อยๆจนกว่าเราจะปิด screen หรือปิด vm
```

* ออกจาก screen
```
ctrl+A ยกนิ้ว press D >> detached
```

* เข้า screen
```
screen -R sc1 >> retached
```

* ลบ screen
```
ctrl+A ยกนิ้ว press K (kill)
```

* ดูว่าเรามี screen อะไรบ้าง
```
screen -ls
```
---
> **Tunnel** --> เวลารันเราอยากให้โน้ตบุคเราต่อเข้าไป browser ของเครื่องบน cloud
![ssh-lpf-1](https://github.com/nxxk23/AIPrototype2023/assets/108257495/79ffaf2f-824d-46d1-8355-f3cc2b5da7e7)

* ต่อเข้า local host จาก window เราก่อน
```
sh -L 8866:localhost:8888 thisisninkspaces@ip
pass: # สร้างช่องเชื่อมต่อจากโน้ตบุคเราโดยตรงไปที่ตัว vm เลย
```
    แล้วก็อป link มาวางใน browser เปลี่ยน tunnel เป็น 8866 เครื่องเรา เข้าสู่ jupyter notebook
---

> github บน command line
```
git config --global user.name  "nxxk23"
git config --global user.email "narakorn.v@kkumail.com"
mkdir codes/
git clone https://github.com/nxxk23/AIPrototype2023.git # load repository ลงมาที่เครื่อง
```
![image](https://github.com/nxxk23/AIPrototype2023/assets/108257495/1839fa23-664d-4678-96bf-11d07718d389)


>>**มาแก้ README.md -- vi README.md**
```
กด i ขึ้น insert พิมพ์ชื่อ esc :wq
git status # ดูว่าไฟล์ไหนถูกแก้ไขไปบ้าง
git add ชื่อไฟล์ #เอาไฟล์ที่จะอัพบนกิต
git commit -m "add my name"
git push
  ใส่ Username: nxxk23
  ใส่ Password: ไม่สามารถใส่ password ของเว็บ เพิ่มความยุ่งยากส์
  github > setting > dev mode > personal access tokens > tokens (classic) > new personal access token(classic)
  note : test , expiration date, repo as full control >> generate tokens
```
    ****then go to git push again fill password: ----****

* map drive path บน windows ให้ตรงกันก่อน
```
cd /mnt จะเห็นไฟล์ทุกอย่างในเครื่อง
cd c >> mkdir ubuntu ไปสร้างไว้ในไดรฟ์ c
cd ubuntu/ pwd ไปเอา path มาก่อน cd home/outside pwd path outside
แล้วเราจะสามารถ ls ดูไฟล์ในเครื่องเราได้
```
![image](https://github.com/nxxk23/AIPrototype2023/assets/108257495/b02314f6-55a5-4a21-868b-d8a006a31e36)

* VSCode
