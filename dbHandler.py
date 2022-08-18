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
        sql = "CREATE TABLE items (\
                    item_id INT NOT NULL AUTO_INCREMENT,\
                    name VARCHAR(255),\
                    PRIMARY KEY (item_id),\
                    UNIQUE (name)\
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