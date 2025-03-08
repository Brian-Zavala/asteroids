import psutil

def get_cpu_usage(interval=1):
    """Returns the current CPU usage percentage over the specified interval."""
    return psutil.cpu_percent(interval=interval)

def get_memory_usage():
    """
    Returns a tuple with memory usage percentage and the total memory in bytes.
    You can convert the total memory to MB or GB as needed.
    """
    mem = psutil.virtual_memory()
    return mem.percent, mem.total

def get_disk_usage(path='/'):
    """Returns the disk usage percentage for the given path."""
    disk = psutil.disk_usage(path)
    return disk.percent

# This part is only run when resource_monitor.py is executed directly.
if __name__ == "__main__":
    print("Resource Monitor Test")
    print("CPU Usage:", get_cpu_usage())
    mem_percent, mem_total = get_memory_usage()
    print(f"Memory Usage: {mem_percent}% of {mem_total / (1024**2):.2f} MB")
    print("Disk Usage:", get_disk_usage(), "%")
