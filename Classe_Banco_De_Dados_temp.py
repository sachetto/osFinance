import sqlite3

class DataBase:
  def __init__(self, db):
    self.database = db
    
  def Connect(self):
    self.conn = sqlite3.connect(self.database)
    self.cursor = self.conn.cursor()

  def QueryWithWhere(self, table, column, option):
    query = "SELECT * FROM {} WHERE {} = ?".format(table, column)
    
    self.cursor.execute(query, (option,))
    results = self.cursor.fetchall()
    
    return results

  def GetDistinctValues(self, table, column):
    query = "SELECT DISTINCT {} FROM {}".format(column, table)
    self.cursor.execute(query)
    companies = self.cursor.fetchall()
    return companies

  def Disconnect(self):
    self.cursor.close()
    self.conn.close()


# ********************************************
#               Classes de Testes:
# ********************************************  
class Test_Database:
  def __init__(self):
    self.db = DataBase("bancodedados.db")

  def Test_QueryWhithWhere(self):
    self.db.Connect()
    my_list = self.db.QueryWithWhere("ordens", "Symbol", "MOVI3")

    for line in my_list:
      print(line)

    self.db.Disconnect()

  def Test_GetDistinctValues(self):
    self.db.Connect()

    companies = self.db.GetDistinctValues("ordens", "Symbol")
    for company in companies:
      print(company[0])

    self.db.Disconnect()
