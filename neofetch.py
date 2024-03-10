import psutil

cpu = psutil.cpu_percent(interval=1)
cpu_freq = psutil.cpu_freq()

output = [
    "CPU Information:                       ",
    f"CPU usage:            {cpu}%                ",
    f"CPU frequency:        {cpu_freq.current}MHz ",

    "Memory Information:                    ",
    f"Total:                {round(psutil.virtual_memory().total / 1024 / 1024, 2)}MB",
    f"Used:                 {round(psutil.virtual_memory().used / 1024 / 1024, 2)}MB",
    f"Available:            {round(psutil.virtual_memory().available / 1024 / 1024, 2)}MB",
    f"Percentage:           {round(psutil.virtual_memory().percent, 2)}%",

    "Disk Information:                      ",
    f"Total:                {round(psutil.disk_usage('/').total / 1024 / 1024 / 1024, 2)}GB",
    f"Used:                 {round(psutil.disk_usage('/').used / 1024 / 1024 / 1024, 2)}GB",
    f"Free:                 {round(psutil.disk_usage('/').free / 1024 / 1024 / 1024, 2)}GB",
    f"Percentage:           {round(psutil.disk_usage('/').percent, 2)}%",

    "Network Information:                   ",
    f"Total Bytes Sent:     {round(psutil.net_io_counters().bytes_sent / 1024 / 1024, 2)}MB",
    f"Total Bytes Recv:     {round(psutil.net_io_counters().bytes_recv / 1024 / 1024, 2)}MB",
    f"Total Packets Sent:   {psutil.net_io_counters().packets_sent}",
    f"Total Packets Recv:   {psutil.net_io_counters().packets_recv}",
]

# Implementation of the Windows Logo to be displayed on the console

logo = [
"                             .oodMMMM",
"                    .oodMMMMMMMMMMMMM",
"        ..oodMMM  MMMMMMMMMMMMMMMMMMM",
"  oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"                                     ",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM",
"  `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM",
"        ````^^^^  ^^MMMMMMMMMMMMMMMMM",
"                       ````^^^^^^MMMM",
]

# printing the output
# the useful output should be in an array to join them together more easily

print("\n\n\n")

for i in range(len(logo)):
    print(logo[i] + "\t\t" + output[i])

print("\n\n\n")