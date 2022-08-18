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


#create tables in case they don't exist
def readyDB(items, db):
    needed_tables = ["items", "values"]
    cursor = db.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.TABLES")
    tables = cursor.fetchall()

    if ("items",) not in tables:
        sql = "CREATE TABLE items (\
                    item_id INT NOT NULL AUTO_INCREMENT,\
                    name VARCHAR(255),\
                    PRIMARY KEY (item_id)\
                )"
        cursor.execute(sql)

    if ("itemvalues",) not in tables:
        sql = "CREATE TABLE itemvalues (\
                    id INT NOT NULL AUTO_INCREMENT,\
                    item_id INT,\
                    lowest_price INT,\
                    volume INT,\
                    median_price INT,\
                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\
                    PRIMARY KEY (id)\
                )"
        cursor.execute(sql)