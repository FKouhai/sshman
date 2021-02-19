import getpass
import pexpect
from pexpect import pxssh
servers = open('server.txt','r') 
inf=open('info','a')

def action(cmnd):
  with open("server.txt") as servers:
    for ip in servers:
      print ip
      user = input('username:')
      password=getpass.getpass('password:')
      invoke(ip,user,password,cmnd,)
      

def invoke(ip,usr,passw,command):
  s = pxssh.pxssh()
  s.login(ip, usr, passw)
  inf.write(ip)
  s.sendline(command)
  s.prompt()
  inf.write(s.before)
  s.logout

action("cat /etc/resolv.conf")
