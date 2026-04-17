import psutil
import datetime

def system_health_check():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = (
        f"System Health Check - {timestamp}\n"
        f"CPU Usage: {cpu}%\n"
        f"Memory Usage: {memory}%\n"
        f"Disk Usage: {disk}%\n"
        "-----------------------------\n"
    )

    print(report)

    with open("health_report.txt", "a") as file:
        file.write(report)

if __name__ == "__main__":
    system_health_check()