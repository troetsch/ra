######################################
# shutil + socket                    #
######################################

import shutil
import socket

# Disk usage
total, used, free = shutil.disk_usage("/")

# Hostname
hostname = socket.gethostname()

# IP address
try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    ip_address = "Unable to resolve IP"

print("Hostname:", hostname)
print("IP Address:", ip_address)
print("Total:", total // (1024**3), "GB")
print("Used:", used // (1024**3), "GB")
print("Free:", free // (1024**3), "GB")
