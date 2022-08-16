import requests

#def get()


#def getAppID(url):
#    code!




def getNums(url):
    #id = getAppID(url)
    r = requests.get(url)
    print(r.text)