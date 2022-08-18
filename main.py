#!/usr/bin/python3
import general
import fetchPrice
import dbHandler
import time


#filenames
SETTINGS_FILE = "settings.json"
ITEMS_FILE = "items.json"


#start
def start():
    getSettings()
    getItems()

    db = None
    if(save_to_db):
        db = dbHandler.createDBConnector()
        dbHandler.readyDB(items, db)

    loop(db)


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
    items = general.readJSON(ITEMS_FILE)["items"]


#get lowest price from fetched data
def getLowestPrice(data):
    if data["success"] == 0:
        raise Exception("Could not get data from servers")

    price_str = general.removeNonDec(data["lowest_price"])
    return int(price_str)


#master function for all processing of item
def processItem(item, db):
    if not item["enable"]:
        return
    data = fetchPrice.fetch(item["url"], currency)
    print(item["name"], end = ": ")
    try:
        print (getLowestPrice(data))
    except Exception as ex:
        print(ex)
    else:
        if item["track_database"]:
            dbHandler.saveDB(item["name"], data, db)


#main loop of program
def loop(db):
    while True:
        for item in items:
            processItem(item, db)
            time.sleep(0.1)
        print("")
        time.sleep(refreshtime)



start()