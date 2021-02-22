import getpass
import pexpect
import sys
from pexpect import pxssh

if len(sys.argv) == 3:
  user = sys.argv[1]
  pasw = sys.argv[2]
  cmnd = sys.argv[3]


def action(cmnd):
 with open('info') as inf:
   with open("server.txt") as servers:
     for ip in servers:
       print (ip)
       invoke(ip,user,pasw,cmnd,inf)
      

def invoke(ip,usr,passw,command,inf):
  s = pxssh.pxssh()
  s.login(ip, usr, passw)
  inf.write(ip)
  s.sendline(command)
  s.prompt()
  inf.write(s.before)
  s.logout

try:
 action(cmnd)
except NameError:
  if sys.argv[1]== '-h' or sys.argv[1] == '--help':
     print("""
     This program needs 3 arguments to work, the remote user,
     its password and the command you want to execute,
     you also need a file called server.txt where the remote IP's are
     this program only works in windows so far
     """)
  elif len(sys.argv) < 3:
     print("You need to pass 3 args which are the user, the ssh pass and the command you want to run on the remote machine")