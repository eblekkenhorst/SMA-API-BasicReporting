# SMA-API-BasicReporting
Python3 script for using the new SMA BasicReporting API

A simple python3 script that implements some of the BasciReporting's (limited, but free) PlantMonitoring functionality of the new SMA API. Follow the developers guide to get access on https://developer.sma.de/sma-apis.html.
The API's sandbox swagger can be found here: https://sandbox.smaapis.de/basicreporting/index.html

I'm not a professional developer so there's plenty room for improvement.

The script can get PV generation for your plant for a year, month, week or day. See the SMA API documentation for the API's limitations. The current daily generation can be automatically uploaded to pvoutput.org. Add to crontab for easy automation.

It implements the token init and refresh requests and starts the authorisation consent request flow.
Add your SMA API credentials and pvoutput.org API key (if applicable) to the configuration file.

Known issues:
- The script assumes you have a single plant. It chooses the first one in the list.
- Error handling can be improved.

```
usage: sma-api-basicreporting [-h] [-v] [-c CONFIGFILE] (-y PVYEAR | -m PVMONTH | -w PVWEEK | -d PVDAY | -t | -T)

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number
  -c CONFIGFILE  configuration file which defaults to 'config.ini' if none provided
  -y PVYEAR      get PV generation for a year: YYYY
  -m PVMONTH     get PV generation for a month: YYYY-MM
  -w PVWEEK      get PV generation for a week: YYYY-MM-DD
  -d PVDAY       get PV generation for a day: YYYY-MM-DD
  -t             get PV generation for today
  -T             get PV generation for today and upload to pvoutput.org
```
Today:
```
> python3 SMA-API-BasicReporting.py -t
2023-01-22;532.0
```
A full week:
```
> python3 SMA-API-BasicReporting.py -w 2022-12-25
2022-12-25T10:00:00;11.0
2022-12-25T11:00:00;1.0
2022-12-25T12:00:00;36.0
2022-12-25T13:00:00;70.0
2022-12-25T14:00:00;44.0
2022-12-25T15:00:00;13.0
2022-12-25T16:00:00;0.0
2022-12-25T17:00:00;0.0
2022-12-26T11:00:00;69.0
2022-12-26T12:00:00;171.0
2022-12-26T13:00:00;226.0
2022-12-26T14:00:00;197.0
2022-12-26T15:00:00;158.0
2022-12-26T16:00:00;67.0
2022-12-26T17:00:00;14.0
2022-12-27T10:00:00;43.0
2022-12-27T11:00:00;150.0
2022-12-27T12:00:00;318.0
2022-12-27T13:00:00;272.0
2022-12-27T14:00:00;172.0
2022-12-27T15:00:00;155.0
2022-12-27T16:00:00;49.0
2022-12-27T17:00:00;4.0
2022-12-28T11:00:00;10.0
2022-12-28T12:00:00;20.0
2022-12-28T13:00:00;24.0
2022-12-28T14:00:00;29.0
2022-12-28T15:00:00;67.0
2022-12-28T16:00:00;31.0
2022-12-28T17:00:00;0.0
2022-12-29T10:00:00;9.0
2022-12-29T11:00:00;24.0
2022-12-29T12:00:00;115.0
2022-12-29T13:00:00;141.0
2022-12-29T14:00:00;252.0
2022-12-29T15:00:00;136.0
2022-12-29T16:00:00;35.0
2022-12-29T17:00:00;0.0
2022-12-30T10:00:00;14.0
2022-12-30T11:00:00;49.0
2022-12-30T12:00:00;74.0
2022-12-30T13:00:00;37.0
2022-12-30T14:00:00;46.0
2022-12-30T15:00:00;48.0
2022-12-30T16:00:00;2.0
2022-12-31T10:00:00;14.0
2022-12-31T11:00:00;20.0
2022-12-31T12:00:00;25.0
2022-12-31T13:00:00;32.0
2022-12-31T14:00:00;21.0
2022-12-31T15:00:00;19.0
2022-12-31T16:00:00;0.0
```
A month:
```
> python3 SMA-API-BasicReporting.py -m 2022-12 
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
A year:
```
> python3 SMA-API-BasicReporting.py -y 2022
2022-01-01;27867.0
2022-02-01;69995.0
2022-03-01;203735.0
2022-04-01;219379.0
2022-05-01;262242.0
2022-06-01;273071.0
2022-07-01;266322.0
2022-08-01;251877.0
2022-09-01;165880.0
2022-10-01;104691.0
2022-11-01;51302.0
2022-12-01;24721.0
```
