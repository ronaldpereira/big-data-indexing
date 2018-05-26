#!/usr/bin/python3

import databaseConnection as dbConn

db = dbConn.databaseConnection()

selectResp = db.select("select max(id) from user_information")

print("The last inserted id is:", selectResp[0]['id'], "\nThe next id to insert is:", selectResp[0]['id']+1)
