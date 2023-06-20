# ********************************************
#               Asset:
# ********************************************
class Asset:
  def __init__(self, symbol, company_name):
    self.symbol = symbol
    self.company_name = company_name
    self.current_price = 0.0
    self.category = "UNDEFINED"
    
  def Print(self):
    print("Empresa: " + self.company_name)
    print("Ticker: " + self.symbol)
    print("Preço de tela: R$" + str(self.current_price))
    print("Categoria: " + self.category)


# ********************************************
#               Share:
# This class represents each line of the 
# database from B3
# ********************************************
class Share:
  def __init__(self):
    self.id


# ********************************************
#               ShareTracker:
# It will store all sares for each company
# ********************************************  
class ShareTracker:
  def __init__(self, company):
    self.company = company
    self.share_jumps = []
    self.total_shares = 0
    self.total_cost = 0.0
    self.average_price = 0.0


# ********************************************
#               ShareTracker:   TO DO!!!!!!!!!
# ******************************************** 
class Wallet:
  def __init__(self):
    self.company_share_tracker = []
  
# ********************************************
#               Classes de Testes:
# ********************************************  
class Test_Asset:
  def __init__(self):
    self.XPTO11 = Asset("XPTO11", "XP Tolando")
    
  def Test_Print(self): 
    self.XPTO11.Print()