import paramiko
def ssh_command(ip,user,command):
    private_key = paramiko.RSAKey.from_private_key_file("D:\Python_Workspace\sshconnection\id_rsa")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip,port=22,username=user,pkey=private_key,timeout=3)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            ssh_session.exec_command(command)
            print(ssh_session.recv(1024))
    except Exception as e:
        print('%s connection %s' % (ip,e))
    return

ssh_command('192.168.43.127','root','df -h')