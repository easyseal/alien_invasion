import paramiko
private_key = paramiko.RSAKey.from_private_key_file("D:\Python_Workspace\sshconnection\id_rsa")
transport = paramiko.Transport(('192.168.43.127',22))
transport.connect(username='root',pkey=private_key)
sfp = paramiko.SFTPClient.from_transport(transport)
sfp.get('/root/anaconda-ks.cfg','anaconda-ks.cfg')
sfp.put('test.cfg','/root/test.cfg')
transport.close()