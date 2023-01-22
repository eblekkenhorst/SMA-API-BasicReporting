import requests, json, argparse, time
from datetime import datetime
from configparser import ConfigParser
import os.path

progname='sma-basicreporting'
version = "0.04"

class BasicReporting:
  def __init__(self, version):
    self.version = version

  def get_config(self, configFile='config.ini'):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_filepath = dir_path+"/"+configFile
    # check if the config file exists
    exists = os.path.exists(config_filepath)
    config = None
    if exists:
      config = ConfigParser()
      config.read(config_filepath)
      # Retrieve config details
      sma_api_config = config["SMA-API"]
      pvoutput_config = config["PVOUTPUT"]
      self.clientId = sma_api_config["clientId"].strip("\'")
      self.clientSecret = sma_api_config["clientSecret"].strip("\'")
      self.loginHint = sma_api_config["loginHint"].strip("\'")
      self.pvApiKey = pvoutput_config["pvApiKey"].strip("\'")
      self.pvSystemId = pvoutput_config["pvSystemId"].strip("\'")
      self.plantID = "0000"
      self.bcState = "unknown"
      self.bearerToken = ""
      self.refreshToken = ""
    else:
      #print("config.ini file not found at ", config_filepath)
      raise ValueError('config.ini file not found at: ' + config_filepath)

  def token_request(self):
    # Step 1 - Token request
    url = "https://auth.smaapis.de/oauth2/token"
    payload='grant_type=client_credentials&client_id=' + self.clientId + '&client_secret=' + self.clientSecret
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        self.bearerToken = "Bearer " + responseObj["access_token"]
        self.refreshToken = responseObj["refresh_token"]
    else:
        print(response.text)
        raise ValueError('Token request returned HTTP code: ' + str(response.status_code))

  def token_refresh(self):
    # Step 2 - Token refresh
    url = "https://auth.smaapis.de/oauth2/token"
    payload='grant_type=refresh_token&client_id=' + self.clientId + '&client_secret=' + self.clientSecret + '&refresh_token=' + self.refreshToken
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'authorization': self.bearerToken
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        self.bearerToken = "Bearer " + responseObj["access_token"]
        self.refreshToken = responseObj["refresh_token"]
    else:
        print(response.text)
        raise ValueError('Token refresh returned HTTP code: ' + str(response.status_code))

  def consent_init(self):
    # Step 3 - BC auth init
    url = "https://async-auth.smaapis.de/oauth2/v2/bc-authorize"
    payload = json.dumps({
      "loginHint": self.loginHint
    })
    headers = {
      'Content-Type': 'application/json',
      'authorization': self.bearerToken
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200 and response.status_code != 201:
        print(response.text)
        raise ValueError('Consent init returned HTTP code: ' + str(response.status_code))

  def consent_status(self):
    # Step 4 - BC Auth Status
    url = "https://async-auth.smaapis.de/oauth2/v2/bc-authorize/" + self.loginHint
    payload = ""
    headers = {
      'Content-Type': 'application/json',
      'authorization': self.bearerToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        self.bcState = responseObj["state"]
        if self.bcState != 'Accepted':
            raise ValueError('Consent status returned state: ' + self.bcState)
        else: return True
    else:
        print(response.text)
        raise ValueError('Consent status returned HTTP code: ' + str(response.status_code))

  def get_plantID(self):
    # Step 5 - Plant overview
    url = "https://basicreporting.smaapis.de/v1/plants"
    payload={}
    headers = {
        'authorization': self.bearerToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        self.plantID = responseObj["plants"][0]["plantId"]
    else:
        print(response.text)
        raise ValueError('Get plantId returned HTTP code: ' + str(response.status_code))

  def PVgeneration_day(self, pvDate):
    # Step 6a - PV Generation on date
    url = "https://basicreporting.smaapis.de/v1/plants/" + self.plantID + "/measurements/sets/PvGeneration/Day?Date=" + pvDate
    payload={}
    headers = {
        'authorization': self.bearerToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        return responseObj
    else:
        print(response.text)
        raise ValueError('API PVgeneration Day returned HTTP code: ' + str(response.status_code))

  def PVgeneration_week(self, pvWeek):
    # Step 6b - PV Generation on date
    url = "https://basicreporting.smaapis.de/v1/plants/" + self.plantID + "/measurements/sets/PvGeneration/Week?Date=" + pvWeek
    payload={}
    headers = {
        'authorization': self.bearerToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        return responseObj
    else:
        print(response.text)
        raise ValueError('API PVgeneration Week returned HTTP code: ' + str(response.status_code))

  def PVgeneration_month(self, pvDate):
    # Step 6c - PV Generation on date
    url = "https://basicreporting.smaapis.de/v1/plants/" + self.plantID + "/measurements/sets/PvGeneration/Month?Date=" + pvDate
    payload={}
    headers = {
        'authorization': self.bearerToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        return responseObj
    else:
        print(response.text)
        raise ValueError('API PVgeneration Month returned HTTP code: ' + str(response.status_code))

  def PVgeneration_year(self, pvYear):
    # Step 6d - PV Generation on date
    url = "https://basicreporting.smaapis.de/v1/plants/" + self.plantID + "/measurements/sets/PvGeneration/Year?Date=" + pvYear
    payload={}
    headers = {
        'authorization': self.bearerToken
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        responseObj = response.json()
        return responseObj
    else:
        print(response.text)
        raise ValueError('API PVgeneration Year returned HTTP code: ' + str(response.status_code))

  def logout(self):
    # Step 7 - Logout
    url = "https://auth.smaapis.de/oauth2/logout"
    payload='client_id=' + self.clientId + '&client_secret=' + self.clientSecret + '&refresh_token=' + self.refreshToken
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200 and response.status_code != 204:
        print(response.text)
        raise ValueError('API logout returned HTTP code: ' + str(response.status_code))

  def pvoutputUpload(self, pvDate, pvGen):
    # Step 8 - upload to pvoutput.org
    # curl -d "data=20210830,15000" -H "X-Pvoutput-Apikey: Your-API-Key" -H "X-Pvoutput-SystemId: Your-System-Id" https://pvoutput.org/service/r2/addoutput.jsp
    url = "https://pvoutput.org/service/r2/addoutput.jsp"
    payload = 'data=' + pvDate + ',' + pvGen
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-Pvoutput-Apikey': self.pvApiKey,
      'X-Pvoutput-SystemId': self.pvSystemId
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
        print(response.text)
        raise ValueError('PVoutput upload returned HTTP code: ' + str(response.status_code))


# Read command line args
parser = argparse.ArgumentParser(prog=progname)
parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version, help="show program's version number")
parser.add_argument('-c', action='store', dest='configFile', default='config.ini', required=False, help="configuration file which defaults to 'config.ini' if none provided")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-y", action='store', dest='pvYear', type=str, default=False, help="get PV generation for a year: YYYY")
group.add_argument("-m", action='store', dest='pvMonth', type=str, default=False, help="get PV generation for a month: YYYY-MM")
group.add_argument("-w", action='store', dest='pvWeek', type=str, default=False, help="get PV generation for a week: YYYY-MM-DD")
group.add_argument("-d", action='store', dest='pvDay', type=str, default=False, help="get PV generation for a day: YYYY-MM-DD")
group.add_argument("-t", action='store_true', dest='pvToday', default=False, help="get PV generation for today")
group.add_argument("-T", action='store_true', dest='pvoutToday', default=False, help="get PV generation for today and upload to pvoutput.org")
args = parser.parse_args()

# Main program logic follows:
if __name__ == '__main__':

  try:
    myBasicReporting = BasicReporting(version)
    myBasicReporting.get_config(args.configFile)
    myBasicReporting.token_request()
    myBasicReporting.token_refresh()
    myBasicReporting.consent_init()
    time.sleep(1) # Looks like the API sometimes fails if we continue too quick

    if myBasicReporting.consent_status():
      myBasicReporting.get_plantID()
      if args.pvYear:
        pvOutput =  myBasicReporting.PVgeneration_year(args.pvYear)
        pvSet = pvOutput["set"]
        for x in pvSet:
          time = x["time"]
          print(time[0:10] + ";" + str(x["pvGeneration"]))
      elif args.pvMonth:
        pvOutput =  myBasicReporting.PVgeneration_month(args.pvMonth)
        pvSet = pvOutput["set"]
        for x in pvSet:
          time = x["time"]
          print(time[0:10] + ";" + str(x["pvGeneration"]))
      elif args.pvWeek:
        pvOutput =  myBasicReporting.PVgeneration_week(args.pvWeek)
        pvSet = pvOutput["set"]
        for x in pvSet:
          time = x["time"]
          print(time[0:10] + ";" + str(x["pvGeneration"]))
      elif args.pvDay:
        pvOutput =  myBasicReporting.PVgeneration_day(args.pvDay)
        pvSet = pvOutput["set"]
        for x in pvSet:
          time = x["time"]
          print(time + ";" + str(x["pvGeneration"]))
      elif args.pvToday or args.pvoutToday:
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        thisMonth = '%02d-%02d' % (currentYear, currentMonth)
        thisDay = '%02d-%02d-%02d' % (currentYear, currentMonth, currentDay)
        pvOutput =  myBasicReporting.PVgeneration_month(thisMonth)
        pvSet = pvOutput["set"]
        for x in pvSet:
          time = x["time"]
          if time == thisDay + "T00:00:00":
            print(time[0:10] + ";" + str(x["pvGeneration"]))
            if args.pvoutToday:
              pvDay = '%02d%02d%02d' % (currentYear, currentMonth, currentDay)
              pvGen = '%d' % int(x["pvGeneration"])
              myBasicReporting.pvoutputUpload(pvDay, pvGen)


      myBasicReporting.logout()
    else: print('Not authorized\n')

  except Exception as error:
    print('Error caught: ' + repr(error))

