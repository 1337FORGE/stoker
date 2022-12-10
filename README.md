# Stôker
**Internet Connectivity Checker**

## Description
Stoker script is designed to ping different DNS services and check if the internet is up or down. The script can be used to monitor internet connectivity and log the results to a file for future reference.

## Latest changes
- Version 1.1 added
- Version 1.0 added

## Features
- The script will log the machine name, operating system, MAC address, and both public and private IP addresses.
- The script will create a neat log file structure organized by year/month/ (yyyy/mm/). Each log file will then be named using the date it was created (dd-mm-yy.log).
- The script will notify you if your system is not connected to the internet, and will continuously check for a connection every 5 seconds until it is successful.
- The script will print the results in the terminal as it logs them.

## Changelog
### v1.1.0 (2022-12-09)
- Created a new function to check if the internet connection is available.
- Added ping time average
- Cleaned up the log result to make it easier to read.
- Cleaned up the code to make it easier to read.
- Added banner and visual improvements.
### v1.0 (2022-12-08)
- Initial release

## Todo
- Fix Linux issue to return the summary of ping time.
- Logging the results if internet is down. (In currenct version it exits the script)
- Fix the private ip
