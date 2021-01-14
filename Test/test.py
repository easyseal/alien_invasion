import paramiko
def ssh_command(ip,user,command):
    private_key = paramiko.RSAKey.from_private_key_file("D:\Python_Workspace\sshconnection\id_rsa")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect()
    ssh.connect(hostname=ip,port=22,username=user,pkey=private_key)
    ssh_session = ssh.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return

ssh_command('192.168.43.128','root','df -h')