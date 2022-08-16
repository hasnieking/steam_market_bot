#!/usr/bin/python3
from cgi import print_exception
import fetchPrice
import re
import time


filename = "urls.txt"
currency = 3 #USD = 1, GPB = 2, EUR = 3, etc


#start
def start():
    getURLS()

    for url in urls:
        data = fetchPrice.fetch(url, currency)
        print(getLowestPrice(data))
        time.sleep(1)




#get lowest price from fetched data
def getLowestPrice(data):
    price_str = data["lowest_price"]
    price_str = re.sub(r'[^0-9]', '', price_str)
    return int(price_str)



#get urls from file
urls = []
def getURLS():
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        line = line.replace("\n", "")
        line = line.replace("http:", "https:")
        urls.append(line)

    return



start()