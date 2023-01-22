# SMA-API-BasicReporting
Python script for using the new SMA BasicReporting API

A simple python script that implements some of the BasciReporting's PlantMonitoring functionality of the new SMA API. Follow the developers guide to get access on https://developer.sma.de/sma-apis.html.
The API's sandbox swagger can be found here: https://sandbox.smaapis.de/basicreporting/index.html

I'm not a professional developer so there's plenty room for improvement.

usage: sma-basicreporting [-h] [-v] [-c CONFIGFILE] (-y PVYEAR | -m PVMONTH | -w PVWEEK | -d PVDAY | -t | -T)

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c CONFIGFILE, --config CONFIGFILE
                        Configuration file
  -y PVYEAR             Get PV generation for a year: YYYY
  -m PVMONTH            Get PV generation for a month: YYYY-MM
  -w PVWEEK             Get PV generation for a week: YYYY-MM-DD
  -d PVDAY              Get PV generation for a day: YYYY-MM-DD
  -t                    Get PV generation for today
  -T                    Get PV generation for today and upload to pvoutput.org
