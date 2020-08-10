import os
import time
import paramiko
path = os.getcwd()
dirs = os.listdir(path)
f = open("1.txt","r")
c = f.read()
d = ""
for i in dirs :
    d = d + i + "\n"
f.close()
if(d != c):
    c = c.split()
    d = d.split()
    for i in range(len(c)):
        d.remove(c[i])
    print(d)
    for i in d:
        print("发现新备份文件，开始上传")
        client = paramiko.Transport(('192.168.0.0',22))
        client.connect( username="abcde",password="12345")
        sftp = paramiko.SFTPClient.from_transport(client)
        sftp.put(localpath=i,remotepath="路径/{0}".format(i))
        client.close()
        print("上传结束")
    f = open("1.txt","a")
    for i in d:
        f.write(i)
    f.close

    
