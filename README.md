# Stôker
**Internet Connectivity Checker**

## Description
Stoker script is designed to ping different DNS services and check if the internet is up or down. The script can be used to monitor internet connectivity and log the results to a file for future reference.

## Latest changes
- Version 1.1 added
- Version 1.0 added

## Features
- The script logs machine name, operating system, MAC address, and both public and private IP addresses
- DNS server is randomly selected from a list of providers to avoid false results
- The delay between tests is randomly set between 10-30 seconds
- The script creates a log file structure organized by year/month and names each log file using the date it was created
- The script checks for internet connection and notifies the user if not connected, continuously checking every 5 seconds until a connection is established
- The script prints the results in the terminal as they are logged

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
