#!/usr/bin/python3

import databaseConnection as dbConn

db = dbConn.databaseConnection()

selectResp = db.select("select max(id) from user_information")

print(selectResp)
