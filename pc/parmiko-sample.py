import paramiko

p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
p.connect("192.168.1.x", port=22, username="xx", password="xx")
stdin, stdout, stderr = p.exec_command("ls")
opt = stdout.readlines()
opt = "".join(opt)
print(opt)
