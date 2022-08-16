import json
import requests

#The given url is in the form of:
#https://steamcommunity.com/market/listings/730/StatTrak%E2%84%A2%20M4A1-S%20%7C%20Hyper%20Beast%20%28Minimal%20Wear%29
#This code changes it to the form:
#https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=StatTrak%E2%84%A2%20M4A1-S%20%7C%20Hyper%20Beast%20%28Minimal%20Wear%29
#and then returns the fetched data from the market


offset = 43
jsonurl = ["https://steamcommunity.com/market/priceoverview/?appid=", "&currency=", "&market_hash_name="]

#convert url
def getFetchURL(url, currency):
    shortened = url[offset:]
    split = shortened.split('/')
    appid = split[0]
    market_hash_name = split[1]
    newurl = jsonurl[0] + appid + jsonurl[1] + str(currency) + jsonurl[2] + market_hash_name
    
    return newurl


#get data from Steam servers
def fetch(url, currency):
    fetchurl = getFetchURL(url, currency)
    r = requests.get(fetchurl)
    data = json.loads(r.text)
    return data