import paramiko
private_key = paramiko.RSAKey.from_private_key_file("D:\Python_Workspace\sshconnection\id_rsa")
transport = paramiko.Transport(('192.168.43.127',22))
transport.connect(username='root',pkey=private_key)
ssh = paramiko.SSHClient()
ssh._transport = transport
stdin,stdout,stderr = ssh.exec_command("df -h")
for x in stdout:
    print(x,end='')
ssh.close()