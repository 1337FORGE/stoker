# Stôker
**Internet Connectivity Checker**

## Description
Stoker script is designed to ping different DNS services and check if the internet is up or down. The script can be used to monitor internet connectivity and log the results to a file for future reference.

## Latest changes
- Version 1.1 added
- Version 1.0 added

## Features
- DNS server is randomly selected to avoid false results
- The script checks for internet connection before each test
- The script logs various system information
- The script will create a log file with the date as its name, organized in a neat structure by year/month

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
