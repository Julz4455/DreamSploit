#Simple Port Scanner
#www.youtube.com/priyankgada
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# RAW_INPUT IP / HOST
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer) #getserver IP

print("Please wait, scanning remote host", remoteServerIP)

#Specify Range - From 1 to 8081
try:
    for port in range(1,8081):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()
# If interrupted
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
# If Host is wrong
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
# If server is down
except socket.error:
    print("Couldn't connect to server")
    sys.exit()
