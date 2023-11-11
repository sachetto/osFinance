from datetime import datetime
import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from Config.Connection import DBConnectionHandler
from Entities.Asset import Asset
from Entities.Category import Category
from Entities.Share import Share
from Repository.Category_Repository import CategoryRepository
from Repository.Asset_Repository import AssetRepository
from Repository.Share_Repository import ShareRepository

# ***********************************************
path = "share_it_db.db"

def __CreateTestDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Category.metadata.create_all(engine)
        Asset.metadata.create_all(engine)
        Share.metadata.create_all(engine)

def __RemoveTableFromDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Share.metadata.drop_all(engine)
        Asset.metadata.drop_all(engine)
        Category.metadata.drop_all(engine)

def SelectAll_Test(repo):
    shares = repo.Select()

    if shares[0].Asset.Symbol == "B3SA3" and\
       shares[0].Asset.Company_Name == "B3 SA" and\
       shares[0].Date == date_obj1 and\
       shares[0].Amount == 10 and\
       shares[0].Total_Value == 300.00 and\
       shares[0].Type == "BUY" and\
       shares[1].Asset.Symbol == "KNCR11" and\
       shares[1].Asset.Company_Name == "FII KINEA RI CI" and\
       shares[1].Date == date_obj2 and\
       shares[1].Amount == 100 and\
       shares[1].Total_Value == 200.00 and\
       shares[1].Type == "BUY" and\
       shares[2].Asset.Symbol == "KNCR11" and\
       shares[2].Asset.Company_Name == "FII KINEA RI CI" and\
       shares[2].Date == date_obj2 and\
       shares[2].Amount == 50 and\
       shares[2].Total_Value == 200.00 and\
       shares[2].Type == "SELL" and\
       shares[3].Asset.Symbol == "KNCR11" and\
       shares[3].Asset.Company_Name == "FII KINEA RI CI" and\
       shares[3].Date == date_obj2 and\
       shares[3].Amount == 50 and\
       shares[3].Total_Value == 200.00 and\
       shares[3].Type == "BUY":
        print("Select_Test - PASSED")
    else:
        print("Select_Test - FAILED")
    return shares


def SelectBySymbol_Test(repo):
    shares = repo.Select(symbol="B3SA3")

    if shares[0].Asset.Symbol == "B3SA3" and\
       shares[0].Asset.Company_Name == "B3 SA" and\
       shares[0].Date == date_obj1 and\
       shares[0].Amount == 10 and\
       shares[0].Total_Value == 300.00 and\
       shares[0].Type == "BUY":
          print("SelectBySymbol_Test - PASSED")
    else:
        print("SelectBySymbol_Test - FAILED")
    return shares


def SelectByType_Test(repo):
    shares = repo.Select(
        symbol="KNCR11", operation_type="SELL")

    if shares[0].Asset.Symbol == "KNCR11" and\
       shares[0].Asset.Company_Name == "FII KINEA RI CI" and\
       shares[0].Date == date_obj2 and\
       shares[0].Amount == 50 and\
       shares[0].Total_Value == 200.00 and\
       shares[0].Type == "SELL":
          print("SelectByType_Test - PASSED")
    else:
        print("SelectByType_Test - FAILED")
    return shares


def Print_Select(shares):
    for share in shares:
        print(share.Date, share.Asset.Symbol,\
          share.Asset.Company_Name, \
          share.Amount, share.Total_Value,\
          share.Type)

def GetLastShareDate_Test(repo):
    if repo.GetLastShareDate() == date_obj2:
        print("GetLastShareData_Test - PASSED")

# ***********************************************
date1 = "2023-06-13"
date_obj1 = datetime.strptime(date1, '%Y-%m-%d').date()
date2 = "2023-06-23"
date_obj2 = datetime.strptime(date2, '%Y-%m-%d').date()

__CreateTestDatabase()
print()

ca1 = Category(Category="STOCKS")
ca2 = Category(Category="REIT")
repo = CategoryRepository(DBConnectionHandler(path))
repo.Insert(ca1)
repo.Insert(ca2)

a1 = Asset("B3SA3", "B3 SA", 0.00, 1)
a2 = Asset("KNCR11", "FII KINEA RI CI", 0.00, 2)
repo = AssetRepository(DBConnectionHandler(path))
repo.Insert(a1)
repo.Insert(a2)

share1 = Share(date_obj1, 10, 300.00, "BUY", 1)
share2 = Share(date_obj2, 100, 200.00, "BUY", 2)
share3 = Share(date_obj2, 50, 200.00, "SELL", 2)
share4 = Share(date_obj2, 50, 200.00, "BUY", asset=a2)
repo = ShareRepository(DBConnectionHandler(path))
repo.Insert(share1)
repo.Insert(share2)
repo.Insert(share3)
repo.Insert(share4)

# ***********************************************
GetLastShareDate_Test(repo)
print()
shares = SelectAll_Test(repo)
Print_Select(shares)
print()
shares = SelectBySymbol_Test(repo)
Print_Select(shares)
print()
shares = SelectByType_Test(repo)
Print_Select(shares)
print()

__RemoveTableFromDatabase()