import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "theplanetisflat",
    database = "ev_charging_db"
)

cursorObject = dataBase.cursor()





