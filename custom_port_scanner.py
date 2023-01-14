#!usr/bin/python3

import socket
import sys
import time 

try:
   target = socket.gethostbyname(sys.argv[1])

except sockket.gaierror:
   print("Error in name resolution, please check once again..")
   sys.exit()

first_port = int(sys.argv[2])
last_port = int(sys.argv[3])

print("Scanning IP", target)

for port in range(first_port, last_port+1):

    print("Scanning port:",port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    c = s.connect_ex((target, port))
    if(not c):
        print("PORT {} IS OPEN".format(port))
    s.close()



