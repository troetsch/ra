######################################
# Disk + Host + Prometheus Push      #
######################################

import shutil
import socket
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Disk usage
total, used, free = shutil.disk_usage("/")

# Host info
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Prometheus registry
registry = CollectorRegistry()

g_total = Gauge('disk_total_gb', 'Total disk space in GB', registry=registry)
g_used = Gauge('disk_used_gb', 'Used disk space in GB', registry=registry)
g_free = Gauge('disk_free_gb', 'Free disk space in GB', registry=registry)
g_ip = Gauge('machine_ip_as_int', 'Machine IP converted to integer', registry=registry)

# Set values
g_total.set(total // (1024**3))
g_used.set(used // (1024**3))
g_free.set(free // (1024**3))

# Convert IP to integer (Prometheus does not accept strings)
ip_int = int.from_bytes(socket.inet_aton(ip_address), 'big')
g_ip.set(ip_int)

# Push to Pushgateway
push_to_gateway('localhost:9091', job='disk_metrics', registry=registry)

print("Metrics pushed to Prometheus Pushgateway")
