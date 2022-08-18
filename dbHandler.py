import general
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
    createTables(db)
    itemNameReg(items, db)

#create tables that will be used
def createTables(db):
    cursor = db.cursor()
    cursor.execute("SELECT TABLE_NAME FROM information_schema.TABLES")
    tables = cursor.fetchall()

    if ("items",) not in tables:
        sql = general.readText("db/items.sql")
        cursor.execute(sql)

    if ("itemvalues",) not in tables:
        sql = general.readText("db/itemvalues.sql")
        cursor.execute(sql)


#register item in items table if it does not exist
def itemNameReg(items,db):
    cursor = db.cursor()
    for item in items:
        if item["track_database"]:
            sql = "SELECT item_id FROM items WHERE name = %s"
            cursor.execute(sql, (item["name"], ))
            result = cursor.fetchone()
            if result == None:
                sql = "INSERT INTO items (name) VALUES (%s)"
                cursor.execute(sql, (item["name"], ))
                db.commit()


#save data from steam server to database
def saveDB(name, data, db):
    if not data["success"]:
        return
    cursor = db.cursor()
    sql = "SELECT item_id FROM items WHERE name = %s"
    cursor.execute(sql, (name, ))
    id = cursor.fetchone()[0]

    sql = "INSERT INTO itemvalues (item_id, lowest_price, \
        volume, median_price) VALUES (%s, %s, %s, %s)"
    lowest = general.removeNonDec(data["lowest_price"])
    volume = general.removeNonDec(data["volume"])
    median = general.removeNonDec(data["median_price"])
    values = (id, lowest, volume, median)

    cursor.execute(sql, values)
    db.commit()