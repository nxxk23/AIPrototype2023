import subprocess # for execute terminal command

if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls","-ltr"]) #look on file
    subprocess.run(["rm","-r","/home/thisisninkspaces/testfolder1"]) # remove file