# SMA-API-BasicReporting
Python script for using the new SMA BasicReporting API

A simple python script that implements some of the BasciReporting's PlantMonitoring functionality of the new SMA API. Follow the developers guide to get access on https://developer.sma.de/sma-apis.html.
The API's sandbox swagger can be found here: https://sandbox.smaapis.de/basicreporting/index.html

I'm not a professional developer so there's plenty room for improvement.

The script can get PV generation for your plant for a year, month, week or day. The current daily generation can be automatically uploaded to pvoutput.org.
```
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
```
```
> SMA-API-BasicReporting.py -t
2023-01-22;532.0
```
```
> SMA-API-BasicReporting.py -m 2022-12 
2022-12-01;1917.0
2022-12-02;423.0
2022-12-03;339.0
2022-12-04;116.0
2022-12-05;178.0
2022-12-06;1153.0
2022-12-07;1464.0
2022-12-08;759.0
2022-12-09;803.0
2022-12-10;271.0
2022-12-11;438.0
2022-12-12;1964.0
2022-12-13;1113.0
2022-12-14;2187.0
2022-12-15;1514.0
2022-12-16;2062.0
2022-12-17;1132.0
2022-12-18;601.0
2022-12-19;162.0
2022-12-20;106.0
2022-12-21;637.0
2022-12-22;1175.0
2022-12-23;28.0
2022-12-24;699.0
2022-12-25;167.0
2022-12-26;888.0
2022-12-27;1165.0
2022-12-28;176.0
2022-12-29;707.0
2022-12-30;257.0
2022-12-31;120.0
```