import mysql.connector
import json


#create connector for database
def createDBConnector():
    f = open("settings.json")
    text = f.read()
    settings = json.loads(text)
    f.close()

    db = mysql.connector.connect(
        host = settings["database"]["host"],
        user = settings["database"]["user"],
        password = settings["database"]["password"],
        database = settings["database"]["database"]
    )

    return db