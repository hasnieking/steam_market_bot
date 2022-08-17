#!/usr/bin/python3
import general
import fetchPrice
import dbHandler
import re
import time


#filenames
SETTINGS_FILE = "settings.json"
ITEMS_FILE = "items.json"


#start
def start():
    getSettings()
    getItems()

    if(save_to_db):
        db = dbHandler.createDBConnector()

    loop()


#set settings from settings.json
def getSettings():
    settings = general.readJSON(SETTINGS_FILE)
    
    global currency
    global save_to_db
    global refreshtime

    currency = settings["currency"]
    save_to_db = settings["database"]["save_to_db"]
    refreshtime = settings["refreshtime"]


#get items
def getItems():
    global items
    items = general.readJSON(ITEMS_FILE)


#get lowest price from fetched data
def getLowestPrice(data):
    if data["success"] == 0:
        raise Exception("Could not get data from servers")

    price_str = data["lowest_price"]
    price_str = re.sub(r'[^0-9]', '', price_str)
    return int(price_str)

def processItem(item):
    if item["enable"] == False:
        return
    data = fetchPrice.fetch(item["url"], currency)
    print (getLowestPrice(data))



def loop():
    while True:
        for item in items["items"]:
            processItem(item)
            time.sleep(0.1)
        time.sleep(refreshtime)



start()