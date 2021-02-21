# sshman

Hi, thank you for using sshMan, this is a very basic tool that can help to get information from remote machines
In order to use this script you need to have pexpect installed

you can do so by typing in your terminal:

pip install pexpect

Or you can download the pexpect library from PyPi
https://pypi.org/project/pexpect/#files

This script only works in linux machines and has to be launched from a Linux OS too

The script was also thought for machines that share the same user and password

How it works:

This program needs 3 parameters to run, the remote user, remote password and the command that will be launched in the remote machine,
You also need a file called server.txt where you have the IP of the servers that you want to connect to

The script runs the command in the remote machine and writes the output in a file called info, 
if you have any feedback on how to improve it, feel free to share it or to make a branch and contribute to it 

An example on how to run this command

python sshConnect.py user password "df -h"