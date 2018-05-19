#!/usr/bin/python3

import pymysql

class databaseConnection():
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "", "big_data_indexing")
        self.cursor = self.db.cursor()
    
    def closeConnection(self):
        self.db.close()

    def create(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            return "Success"
        except:
            return "Error: unable to create. From sql:" + sqlCommand

    def delete(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            self.db.commit()
            return "Success"
        except:
            self.db.rollback()
            return "Error: unable to delete. From sql:" + sqlCommand

    def insert(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            self.db.commit()
            return "Success"
        except:
            self.db.rollback()
            return "Error: unable to insert data. From sql:" + sqlCommand

    def select(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            return self.cursor.fetchall()
        except:
            return "Error: unable to fetch data. From" + sqlCommand

    def update(self, sqlCommand):
        try:
            self.cursor.execute(sqlCommand)
            self.db.commit()
            return "Success"
        except:
            self.db.rollback()
            return "Error: unable to update. From sql: " + sqlCommand