# Stôker
**Internet Connectivity Checker**

## Description
Stoker script is designed to ping different DNS services and check if the internet is up or down. The script can be used to monitor internet connectivity and log the results to a file for future reference.

## Features
- DNS server is randomly selected to avoid false results
- The script checks for internet connection before each test
- The script logs various system information
- The script will create a log file with the date as its name, organized in a neat structure by year/month

## Usage
```
python3 stoker.py
```

Use ctrl+c to exit

## Log File Results (sample)
```
Stoker Internet Connectivity Checker Log File

Date & Time: 2022-12-13 16:35:28
Stoker Machine: xxxxxxxxx
MAC Address: xx:xx:xx:xx:xx:xx
Public IP: 0.0.0.0
Private IP: 0.0.0.0

Time: 16:35:29 DNS Server: 149.112.112.112
Results: 
[+] Host is up
[+] Ping Times: 19, 15, 14, 15

Time: 16:36:05 DNS Server: 8.26.56.26
Results: 
[+] Host is up
[+] Ping Times: 19, 15, 14, 15

Time: 16:36:27 DNS Server: 176.103.130.130
Results: 
[+] Host is up
[+] Ping Times: 19, 15, 14, 15
```

## Changelog
### v1.0 (2022-12-08)
- Initial release

#### v1.1.0 (2022-12-09)
- Created a new function to check if the internet connection is available.
- Added ping time average
- Cleaned up the log result to make it easier to read.
- Cleaned up the code to make it easier to read.
- Added banner and visual improvements.

#### v1.1.1 (2022-12-12)
- Code clean up (It's not perfect but It's better than before).
- There was problem with outputting ping results and averaging them so I temporary took it out of the code.

#### v1.1.2 (2022-12-13)
- Got the ping times list to work in both Linux and Windows.
- Result file now contains ping times.

## Todo
- Fix Linux issue to return the summary of ping time.
- Logging the results if internet is down. (In currenct version it exits the script)
- Fix the private ip
