#!/usr/bin/python3

import pymysql

class databaseConnection():
    def __init__(self):
        self.db = pymysql.connect("localhost", "ronald", "", "big_data_indexing")
        self.cursor = self.db.cursor()
    
    def closeConnection(self):
        self.db.close()

    def create(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            return "Success"
        except:
            return "Error: unable to create. From sql: " + sqlCommand

    def delete(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            self.db.commit()
            return "Success"
        except:
            self.db.rollback()
            return "Error: unable to delete. From sql: " + sqlCommand

    def execute(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            self.db.commit()
            return "Success"
        except:
            self.db.rollback()
            return "Error: unable to execute. From sql: " + sqlCommand

    def insert(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            self.db.commit()
            return "Success"
        except:
            self.db.rollback()
            return "Error: unable to insert data. From sql: " + sqlCommand

    def select(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            selectResponse = self.cursor.fetchall()
            self.cursor.execute("DESCRIBE user_information;")
            columns = self.cursor.fetchall()
            
            responseArray = [dict() for i in range(len(selectResponse))]
            for rowIndex, row in enumerate(selectResponse):
                for columnIndex, _ in enumerate(row):
                    responseArray[rowIndex][columns[columnIndex][0]] = row[columnIndex]

            return responseArray
        except:
            return "Error: unable to fetch data. From sql: " + sqlCommand

    def update(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            self.db.commit()
            return "Success"
        except:
            self.db.rollback()
            return "Error: unable to update. From sql: " + sqlCommand

    def getIndexes(self, tableName):
        try:
            self.cursor.execute("SHOW INDEXES FROM %s;" %tableName)
            return self.cursor.fetchall()
        except:
            return "Error: unable to get indexes from table " + tableName
            