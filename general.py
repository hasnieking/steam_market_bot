import json

#read json file
def readJSON(filename):
    f = open(filename, "r")
    text = f.read()
    return json.loads(text)