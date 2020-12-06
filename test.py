import Database
from Database import DBManager

manager = DBManager()
manager.setUpDB()
manager.addProperties('A', '1401 Ridgecrest Dr., Plano, TX 75074')
manager.addCashInflow('B', '12/05/2020', 1500, 'Rent')
manager.addCashOutflow('A', '12/07/2020', 400, 'Maintenance', '', 'Checking 4147')