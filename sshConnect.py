import getpass
import pexpect
from pexpect import pxssh
servers = open('server.txt','r') 

inf=open('info','a')

for ip in servers:
  print(ip)
  user = input('username:' )
  password = getpass.getpass('password: ')
  s = pxssh.pxssh()
  s.login(ip,user,password)
  inf.write(ip)
  s.sendline('df -h')
  s.prompt()
  inf.write(s.before)
  s.sendline('free -h')
  s.prompt()
  inf.write(s.before)
  s.logout()

