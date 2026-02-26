# Your task is to take the CPU threshold from the user
# Check the current CPU usage
# If the CPU usage exceeds the threshold, send an email

import psutil
def check_cpu_threshold():
    cpu_threshold = float(input("Enter the CPU usage threshold (in percentage): "))
    
    current_cpu = psutil.cpu_percent(interval=1)
    if current_cpu > cpu_threshold:
        print(f"CPU usage is {current_cpu}%, which exceeds the threshold of {cpu_threshold}%. Sending email alert...")
        # Code to send email goes here
    else:
        print(f"CPU usage is {current_cpu}%, which is within the threshold of {cpu_threshold}%.")
    
check_cpu_threshold()

