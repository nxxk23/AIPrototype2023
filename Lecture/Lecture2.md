# **working on Virtual Machine Cloud ☁**

> Create VM in Azure
![ssh-auth](https://github.com/nxxk23/AIPrototype2023/assets/108257495/5f66bf2e-a618-4416-b602-42bac01dd3f2)

>> Lecture
![Lecture-2](https://github.com/nxxk23/AIPrototype2023/assets/108257495/a63e921b-df0a-4376-b66e-e3492690b900)

* คำสั่ง SSH ใช้เพื่อเข้าไปบน CloudVM จะเหมือนเราทำงานบนเครื่องของเรา
   ```
   ssh thisisninksoaces@20.70.14.212
   pass: 1Q2w3e4r5t--
   ```

* คำสั่ง SCP เพื่อ copy file ขึ้นไปบน internet 
   ```
   scp file.png user@ip:/{ปลายทาง} #ส่งไฟล์จากเครื่องเรา
   scp user@ip:/{ต้นทาง} #ดึงไฟล์มาVM
   ```
   
* คำสั่ง htop ดู cpu / storage memory >> task manager of windows

* คำสั่ง exit ใช้เพื่อออกจากตัว VM
---
> Test working on cloud

* adduser
```
sudo adduser # test adduser into cloud and ssh with friends'ip
```

* chmod
```
sudo chmod 755 user # change permission into readable/executable
```

![vkxuqbatopk21](https://github.com/nxxk23/AIPrototype2023/assets/108257495/7be41a45-8aa0-45e7-b9a9-68cb1fd48424)

  



