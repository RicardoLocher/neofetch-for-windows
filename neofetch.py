import psutil

cpu = psutil.cpu_percent(interval=1)
cpu_freq = psutil.cpu_freq()

print("\nCPU Information:")
print(f"CPU usage:      {cpu}%")
print(f"CPU frequency:  {cpu_freq.current}MHz")
print("######################################")

print("\nMemory Information:")
print(f"Total:          {round(psutil.virtual_memory().total / 1024 / 1024, 2)}MB")
print(f"Used:           {round(psutil.virtual_memory().used / 1024 / 1024, 2)}MB")
print(f"Available:      {round(psutil.virtual_memory().available / 1024 / 1024, 2)}MB")
print(f"Percentage:     {round(psutil.virtual_memory().percent, 2)}%")
print("######################################")

print("\nDisk Information:")
print(f"Total:          {round(psutil.disk_usage('/').total / 1024 / 1024 / 1024, 2)}GB")
print(f"Used:           {round(psutil.disk_usage('/').used / 1024 / 1024 / 1024, 2)}GB")
print(f"Free:           {round(psutil.disk_usage('/').free / 1024 / 1024 / 1024, 2)}GB")
print(f"Percentage:     {round(psutil.disk_usage('/').percent, 2)}%")
print("######################################")

print("\nNetwork Information:")
print(f"Total Bytes Sent:   {round(psutil.net_io_counters().bytes_sent / 1024 / 1024, 2)}MB")
print(f"Total Bytes Recv:   {round(psutil.net_io_counters().bytes_recv / 1024 / 1024, 2)}MB")
print(f"Total Packets Sent: {psutil.net_io_counters().packets_sent}")
print(f"Total Packets Recv: {psutil.net_io_counters().packets_recv}")
print("######################################")