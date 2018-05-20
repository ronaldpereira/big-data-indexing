#!/usr/bin/python3

import databaseConnection as dbConn

db = dbConn.databaseConnection()

selectResp = db.select("select * from user_information")

for row in selectResp:
    print(row['id'])

createIndex = db.execute("CREATE SPATIAL INDEX primary_index2 ON user_information(id)")

print(db.getIndexes("user_information"))