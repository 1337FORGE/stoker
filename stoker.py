#!/bin/bash/env python3

# This is a Python script for pinging various DNS services and writing the results to a log file.
# # This code is available on GitHub https://github.com/sacredbeacon/stoker

#TODO: Filter the result for cleaner output
#TODO: Fix the log file directorty structure
#TODO: test on Linux

import os
import time
import subprocess
from datetime import datetime
import random
import socket
import urllib.request

# Variables
## Date and Time Variables
full_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
full_date = datetime.now().strftime("%d-%m-%y")
day_date = datetime.now().day
month_date = datetime.now().month
year_date = datetime.now().year
year_folder_name = str(year_date)
month_folder_name = str(month_date)
def sleep_time():
    sleep_time = random.randint(10, 30)
    return sleep_time


#FIXME: Create a simple list of DNS servers to ping, do not name them.
## DNS Variables
google_dns = "8.8.8.8"
google_secondary_dns = "8.8.4.4"
cloudflare_dns = "1.1.1.1"
quad9_dns = "9.9.9.9"
opendns_dns = "208.67.222.222"
cisco_dns = "208.67.222.222"
dns_servers = [google_dns, google_secondary_dns, cloudflare_dns, quad9_dns, opendns_dns, cisco_dns]
chosen_dns_server = random.choice(dns_servers)

## Network Variables
public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# OS Type
os_type = os.name

# Print initial message
print("Stoker is running...")
print("Public IP: " + public_ip)
print("Start time: " + full_date_time)

# Check for the OS type
operation_system = os.name
if operation_system == 'nt':
    operation_system = 'Windows'
elif operation_system == 'posix':
    operation_system = 'Linux'


# Print the value of the os_type variable
print("OS type: " + operation_system)

    

# Run the ping command in a loop
while True:
    #FIXME: Fix the log file directory structure based on Windows or linux
    # Create the year folder
    if not os.path.exists(year_folder_name):
        os.makedirs(year_folder_name)
        print("Year folder created")
    else:
        print("Year folder already exists. Skipping...")
    
    # Create the month folder in the year folder
    if not os.path.exists(year_folder_name + "/" + month_folder_name):
        os.makedirs(year_folder_name + "/" + month_folder_name)
        print("Month folder created")
    else:
        print("Month folder already exists. Skipping...")
        
    # Create the log file
    if not os.path.exists(year_folder_name + "/" + month_folder_name + "/" + full_date + ".log"):
        log_file = open(year_folder_name + "/" + month_folder_name + "/" + full_date + ".log", "a")
        log_file.write("Stoker logs file for " + str(public_ip) + "\nLog file created at: " + str(full_date_time) + " \n")
        log_file.close()
        print("Log file created")
    else:
        print("Log file already exists. Skipping...")
        
    # Check the operating system type and ping the IP using the appropriate command
    if operation_system == "Windows":
        # Windows
        ping_command = f"ping {chosen_dns_server}"
    elif operation_system == "Linux":
        # Linux
        ping_command = f"ping -c 4 {chosen_dns_server}"
    else:
        print("OS type not recognized. Exiting...")
        exit()
    # Ping the IP address
    ping_output = os.popen(ping_command).read()

# if ping output contains "%" and numbers betweek 50 and 100, then "Host is up"
    if "0%" in ping_output:
        ping_results = "Host is up"
    elif "100%" in ping_output:
        ping_results = "Host is down"
    else:
        ping_results = "Trying another DNS server"

    # Print the results
    print(ping_results)
    
    # Append the results to the log file
    log_file = open(year_folder_name + "/" + month_folder_name + "/" + full_date + ".log", "a")
    
    log_file.write("\nTime: " + datetime.now().strftime("%H:%M:%S") +
                   " DNS Server: " + chosen_dns_server +
                   "\nResults: " + ping_results)
    log_file.close()

    # Wait 10 seconds before repeating the loop
    print("Sleeping for " + str(sleep_time()) + " seconds...")
    
    time.sleep(sleep_time())
    
    #change the dns server
    chosen_dns_server = random.choice(dns_servers)
    
    # Print the new DNS server
    print("New DNS server: " + chosen_dns_server)
    
