# Stôker
This is a Python script for pinging various DNS services and writing the results to a log file.

## Description
The script will create subdirectories for the year and month, and then create a log file with the date in its name. The log file will be added to the month's directory. The log file will include your public IP address and the current date at the top, and will include the time and the DNS server being pinged before each entry.

## Latest changes
- Version 1.0 added

## Changelog
### v1.1 (2022-12-09)
- Created a new function to check if the internet connection is available.
- Added ping time average
- Cleaned up the log result to make it easier to read.
- Cleaned up the code to make it easier to read.
- Added banner and visual improvements.
### v1.0 (2022-12-08)
- Initial release

## Todo
- Cleaning up the ping results for smaller log files
- Adding "Host is up" and "Host is down" to the log file
- future stuff ...
