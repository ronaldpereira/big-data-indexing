#!/usr/bin/python3

import databaseConnection as dbConn

db = dbConn.databaseConnection()

selectResp = db.select("select * from user_information")[:]

for row in selectResp:
    print(row['id'])

