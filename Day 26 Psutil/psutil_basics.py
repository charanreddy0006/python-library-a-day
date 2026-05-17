import psutil

# --- CPU usage ---
cpu = psutil.cpu_percent(interval=1)

print("CPU Usage:", cpu, "%")

# --- RAM usage ---
memory = psutil.virtual_memory()

print("\nRAM Usage:")
print("Total:", round(memory.total / (1024**3), 2), "GB")
print("Used:", round(memory.used / (1024**3), 2), "GB")
print("Percentage:", memory.percent, "%")

# --- Disk usage ---
disk = psutil.disk_usage('/')

print("\nDisk Usage:")
print("Total:", round(disk.total / (1024**3), 2), "GB")
print("Used:", round(disk.used / (1024**3), 2), "GB")

# --- Battery info ---
battery = psutil.sensors_battery()

if battery:
    print("\nBattery Percentage:", battery.percent, "%")

# --- Running processes count ---
processes = len(psutil.pids())

print("\nRunning Processes:", processes)