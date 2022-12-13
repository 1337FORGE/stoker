#!/bin/bash/env python3


# Stoker is a simple internet connectivity checker that logs the results to a file
# You can find the latest release on GitHub https://github.com/sacredbeacon/stoker


import os
import time
import subprocess
from datetime import datetime
import random
import socket
import urllib.request
import uuid
import re


# Banner
banner = """
 ____  _   //\  _             
/ ___|| |_|/_\|| | _____ _ __ 
\___ \| __/ _ \| |/ / _ \ '__|
 ___) | || (_) |   <  __/ |   
|____/ \__\___/|_|\_\___|_|   
Internet Connectivity Checker
"""
divider = "==============================="


# Print Script Name
print(banner)


# Variables
# Date and Time Variables
full_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
full_date = datetime.now().strftime("%d-%m-%y")
day_date = datetime.now().day
month_date = datetime.now().month
year_date = datetime.now().year
year_folder_name = str(year_date)
month_folder_name = str(month_date)


# DNS Variables
dns_servers = ["8.8.8.8", "8.8.4.4", "1.1.1.1", "9.9.9.9", "208.67.222.222",
               "149.112.112.112", "208.67.220.220", "1.0.0.1", "8.20.247.20",
               "8.26.56.26", "185.228.169.168", "185.225.168.168", "76.76.19.19",
               "76.223.122.150", "176.103.130.130", "176.103.130.131", "64.6.64.6",
               "64.6.65.6", "216.87.84.211", "77.88.8.8", "84.200.69.80", "84.200.70.40"]
chosen_dns_server = random.choice(dns_servers)


# Print divider
print(divider)


# Main Functions
# Defining sleep time function
def sleep_time():
    sleep_time = random.randint(10, 30)
    return sleep_time

  
# FIXME: Fix the log file directory structure based on Windows or linux
# Creating the year folder function
def create_year_folder():
    if not os.path.exists(year_folder_name):
        os.makedirs(year_folder_name)


# Creating the month folder in the year folder
def create_month_folder():
    if not os.path.exists(year_folder_name + "/" + month_folder_name):
        os.makedirs(year_folder_name + "/" + month_folder_name)


# Creating the log file
def create_log_file():
    if not os.path.exists(year_folder_name + "/" + month_folder_name + "/" + full_date + ".log"):
        log_file = open(year_folder_name + "/" +
                        month_folder_name + "/" + full_date + ".log", "a")
        log_file.write(
            "Stoker Internet Connectivity Checker Log File\n"
            "\nDate & Time: " + str(full_date_time) +
            "\nStoker Machine: " + str(machine_name) +
            "\nMAC Address: " + str(mac_address_str) +
            "\nPublic IP: " + str(public_ip) +
            "\nPrivate IP: " + str(private_ip) +
            "\n"
        )
        log_file.close()
        print("[+] Log file created")
    else:
        print("[-] Log file already exists")


# Internet Connectivity Check``
def internet_connectivity():
    while True:
        try:
            urllib.request.urlopen('https://google.com', timeout=10)
            print("[+] Internet is up")
            return True
        except urllib.request.URLError:
            print("[-] Internet is down, trying again in 5 seconds")
            time.sleep(5)
            continue


# Checking for the OS type
operation_system = os.name
if operation_system == 'nt':
    operation_system = 'Windows'
elif operation_system == 'posix':
    operation_system = 'Linux'
else:
    print("OS type not recognized. Exiting...")
    exit()

if operation_system == "Windows":
    # Windows
    ping_command = f"ping {chosen_dns_server}"
elif operation_system == "Linux":
    # Linux
    ping_command = f"ping -c 4 {chosen_dns_server}"
else:
    print("OS type not recognized. Exiting...")
    exit()


# filter out the result between time= and ms and print it
def ping_time():
    if operation_system == "Windows":
        ping_time = re.findall(r"time=(\d+)ms", ping_output)
    elif operation_system == "Linux":
        ping_time = re.findall(r"time=(\d+\.\d+) ms", ping_output)
    return ping_time


# Checking if the host is up or down
def ping_results():
    if "0%" in ping_output:
        ping_results = "[+] Host is up"
    elif "100%" in ping_output:
        ping_results = "[-] Host is down"
    else:
        ping_results = "[!] Host seems down, trying another DNS server"
    return ping_results


# Internet Connectivity Check on start
internet_connectivity()


# Public IP
public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
# Private IP
private_ip = socket.gethostbyname(socket.gethostname())
# MAC Address
mac_address = uuid.getnode()
mac_address_str = ':'.join(['{:02x}'.format(
    (mac_address >> ele) & 0xff) for ele in range(0, 8*6, 8)][::-1])


# Machine Name
machine_name = socket.gethostname()


# Print initial messages
print("[*] Start time: " + full_date_time)
print("[*] Machine name: " + machine_name)
print("[*] OS type: " + operation_system)
print("[*] MAC Address: " + mac_address_str)
print("[*] Public IP: " + public_ip)
print("[*] Private IP: " + private_ip)


# Main loop
while True:
    # Print divider
    print(divider)

   
    # Internet Connectivity Check
    internet_connectivity()

    
    # Printing DNS server
    print("[!] DNS server: " + chosen_dns_server)

    
    # Creating the year folder
    create_year_folder()

    
    # Creating the month folder in the year folder
    create_month_folder()

    
    # Creating the log file
    create_log_file()

    
    # Print ping results
    # I'm currently working on this function

    
    # Ping the IP address
    ping_output = os.popen(ping_command).read()

    
    # Appending the results to the log file
    log_file = open(year_folder_name + "/" +
                    month_folder_name + "/" + full_date + ".log", "a")
    
    log_file.write("\nTime: " + datetime.now().strftime("%H:%M:%S") +
                   " DNS Server: " + chosen_dns_server +
                   "\nResults: \n" +
                   ping_results() +
                   "\n"
                   )
    log_file.close()

    
    # Random wait time
    print("[!] Sleeping for " + str(sleep_time()) + " seconds")

    time.sleep(sleep_time())

    
    # Changing the DNS server
    chosen_dns_server = random.choice(dns_servers)

    
    # Printing exit message
    print("[*] To exit the script, press CTRL+C")
