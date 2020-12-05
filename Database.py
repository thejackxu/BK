import sqlite3
from sqlite3 import *

class DBManager:
    def __init__(self):
        self.conn = None

    def setUpDB(self):
        try:
            dbName = 'Property_Management.db'
            self.conn = sqlite3.connect(dbName)

        except Error as e:
            print('Error occurred: {0}'.format(e))

    def createTable(self):
        try:
            #primary property id & address
            pidTable = '''
                        CREATE TABLE IF NOT EXIST property_id(
                        primary_id TEXT PRIMARY KEY UNIQUE NOT NULL,
                        address TEXT NOT NULL
                        )             
                        '''

            cashInflowTable = '''
                        CREATE TABLE IF NOT EXIST cashInflow(
                        primary_id TEXT UNIQUE NOT NULL,
                        FOREIGN KEY (primary_id)
                            REFERENCES pidTable (primary_id),
                        date TEXT NOT NULL,
                        dollarAmount money NOT NULL,
                        paymentCategory text NOT NULL
                        )
                        '''



        except Error as e:
            print('Error occurred: {0}'.format(e))