#!/usr/bin/python3

import databaseConnection as dbConn

db = dbConn.databaseConnection()

print(db.select("select * from user_information limit 1000")[0])