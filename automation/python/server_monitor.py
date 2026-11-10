
import psutil
import datetime
import os

# Thresholds
CPU_LIMIT = 80
RAM_LIMIT = 80
DISK_LIMIT = 80


def check_server_health():

    print("=" * 45)
    print("       SERVER HEALTH MONITOR")
    print("=" * 45)

    # CPU usage
    cpu = psutil.cpu_percent(interval=1)

    # RAM usage
    ram = psutil.virtual_memory().percent

    # Disk usage
    disk = psutil.disk_usage("/").percent

    # System uptime
    uptime_seconds = int(
        datetime.datetime.now().timestamp()
        - psutil.boot_time()
    )

    uptime_hours = uptime_seconds // 3600

    print(f"CPU Usage  : {cpu}%")
    print(f"RAM Usage  : {ram}%")
    print(f"Disk Usage : {disk}%")
    print(f"Uptime     : {uptime_hours} hours")

    print("-" * 45)

    # Health checks
    if cpu > CPU_LIMIT:
        print("WARNING: High CPU usage!")

    if ram > RAM_LIMIT:
        print("WARNING: High RAM usage!")

    if disk > DISK_LIMIT:
        print("WARNING: High Disk usage!")

    if cpu <= CPU_LIMIT and ram <= RAM_LIMIT and disk <= DISK_LIMIT:
        print("STATUS: SERVER HEALTHY")

    print("=" * 45)


if __name__ == "__main__":
    check_server_health()
