import sqlite3
from sqlite3 import *

class DBManager:
    def __init__(self):
        self.conn = None

    def createTable(self):
        try:
            #primary property id & address
            pidTable = '''
                        CREATE TABLE IF NOT EXISTS pidTable(
                        primary_id TEXT PRIMARY KEY UNIQUE NOT NULL,
                        address TEXT NOT NULL
                        )       
                        '''
            #cash inflow table, property ID, date, $ amount, payment category (rent, late fee, etc)
            cashInflowTable = '''
                        CREATE TABLE IF NOT EXISTS cashInflowTable(
                        primary_id TEXT UNIQUE NOT NULL,
                        paymentDate TEXT NOT NULL,
                        dollarAmount MONEY NOT NULL,
                        paymentCategory TEXT NOT NULL,
                        FOREIGN KEY (primary_id)
                            REFERENCES pidTable (primary_id)
                            ON DELETE SET NULL
                            ON UPDATE CASCADE
                        )
                        '''
            #cash outflow table, property ID, date, $ amount, payment category (rent, late fee, etc), payment category
            #others, and payment type (how did they pay)
            cashOutflowTable = '''
                        CREATE TABLE IF NOT EXISTS cashOutflowTable(
                        primary_id TEXT UNIQUE NOT NULL,
                        paymentDate TEXT NOT NULL,
                        dollarAmount MONEY NOT NULL,
                        paymentCategory TEXT NOT NULL,
                        paymentCategoryOthers TEXT NOT NULL,
                        paymentType TEXT NOT NULL,
                        FOREIGN KEY (primary_id)
                            REFERENCES pidTable (primary_id)
                            ON DELETE SET NULL
                            ON UPDATE CASCADE          
                        )
                        '''

            reader = self.conn.cursor()
            reader.execute(pidTable)
            reader.execute(cashInflowTable)
            reader.execute(cashOutflowTable)

        except sqlite3.Error as e:
            print('Error occurred: {0}'.format(e))

    def setUpDB(self):
        try:
            dbName = 'Property_Management.db'
            self.conn = sqlite3.connect(dbName)
            print('Database successfully connected!')
            self.conn.execute('PRAGMA foreign_keys = 1')
            self.createTable()
            #return True

        except sqlite3.Error as e:
            self.conn.close()
            print('Error occurred: {0}'.format(e))
            #return False

    def addProperties(self, PID, newaddress):
        query = '''
                INSERT INTO pidTable VALUES ('{0}', '{1}')'''.format(PID, newaddress)
        try:
            reader = self.conn.cursor()
            reader.execute(query)
            self.conn.commit()
            print('Property at {0} added as {1}'.format(newaddress, PID))

        except sqlite3.IntegrityError as e:
            print('Error occurred: {0}'.format(e))

    def addCashInflow(self, PID, Date, Amount, Type):
        query = '''
                INSERT INTO cashInflowTable VALUES ('{0}', '{1}', '{2}', '{3}')'''.format(PID, Date, Amount, Type)
        try:
            reader = self.conn.cursor()
            reader.execute(query)
            self.conn.commit()
            print('Payment (Inflow) successfully added to property ID {0}'.format(PID))

        except sqlite3.IntegrityError as e:
            print('Error occurred: {0}'.format(e))

    def addCashOutflow(self, PID, Date, Amount, Type, TypeOthers, PaymentType):
        query = '''
                INSERT INTO cashOutflowTable VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')'''.format(PID, Date, Amount, Type, TypeOthers, PaymentType)
        try:
            reader = self.conn.cursor()
            reader.execute(query)
            self.conn.commit()
            print('Payment (Outflow) successfully added to property ID {0}'.format(PID))

        except sqlite3.IntegrityError as e:
            print('Error occurred: {0}'.format(e))