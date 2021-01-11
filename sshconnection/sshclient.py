import paramiko
private_key = paramiko.RSAKey.from_private_key_file("D:\Python_Workspace\id_rsa")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.43.127',port=22,username='root',pkey=private_key)
stdin,stdout,stderr = ssh.exec_command("df -h")
for x in stdout:
    print(x,end='')
ssh.close()