#!/usr/bin/python3
import fetchPrice
import re
import time
import json




#start
def start():
    getSettings()
    getURLS()

    for url in urls:
        data = fetchPrice.fetch(url, currency)
        print(getLowestPrice(data))
        time.sleep(1)


#set settings from settings.json
def getSettings():
    f = open("settings.json", "r")
    text = f.read()
    f.close()
    settings = json.loads(text)
    
    global url_filename
    global currency
    global save_to_db
    global db_filename

    url_filename = settings["url_filename"]
    currency = settings["currency"]
    save_to_db = settings["database"]["save_to_db"]
    db_filename = settings["database"]["db_filename"]


#get lowest price from fetched data
def getLowestPrice(data):
    price_str = data["lowest_price"]
    price_str = re.sub(r'[^0-9]', '', price_str)
    return int(price_str)



#get urls from file
urls = []
def getURLS():
    f = open(url_filename, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        line = line.replace("\n", "")
        line = line.replace("http:", "https:")
        urls.append(line)


start()