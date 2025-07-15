import time
import psutil
from colorama import init, Fore, Style

init(autoreset=True)

def get_color(percent):
    if percent < 50:
        return Fore.GREEN
    elif percent < 80:
        return Fore.YELLOW
    else:
        return Fore.RED

def show_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_color = get_color(cpu_percent)

    mem = psutil.virtual_memory()
    ram_percent = mem.percent
    ram_color = get_color(ram_percent)

    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    disk_color = get_color(disk_percent)

    print("=" * 40)
    print(f"CPU usage : {cpu_color}{cpu_percent}%{Style.RESET_ALL}")
    print(f"RAM Usage : {ram_color}{ram_percent}%{Style.RESET_ALL}")
    print(f"Disk Usage : {disk_color}{disk_percent}%{Style.RESET_ALL}")
    print("=" * 40)

if __name__ == "__main__":
    try:
        while True:
            show_stats()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExisting Sysmon.")