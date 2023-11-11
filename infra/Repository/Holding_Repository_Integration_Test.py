import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from Config.Connection import DBConnectionHandler
from Entities.Holding import Holding
from Entities.Asset import Asset
from Entities.Category import Category
from Repository.Holding_Repository import HoldingRepository
from Repository.Asset_Repository import AssetRepository
from Repository.Category_Repository import CategoryRepository

# ***********************************************
path = "holding_it_db.db"

def __CreateTestDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Category.metadata.create_all(engine)
        Asset.metadata.create_all(engine)
        Holding.metadata.create_all(engine)

def __RemoveTableFromDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Holding.metadata.drop_all(engine)
        Asset.metadata.drop_all(engine)
        Category.metadata.drop_all(engine)

def SelectAll_Test(repo):
    Holdings = repo.Select()

    if Holdings[0].Asset.Symbol == "B3SA3" and\
       Holdings[0].Asset.Company_Name == "B3 SA" and\
       Holdings[0].Asset.Category.Category == "STOCK" and\
       Holdings[0].Amount == 10 and\
       Holdings[1].Asset.Symbol == "KNCR11" and\
       Holdings[1].Asset.Company_Name == "FII KINEA RI CI" and\
       Holdings[1].Asset.Category.Category == "REIT" and\
       Holdings[1].Amount == 20:
        print("Select_Test - PASSED")
    else:
        print("Select_Test - FAILED")
    return Holdings

def SelectBySymbol_Test(repo):
    Holdings = repo.Select(symbol="B3SA3")

    if Holdings[0].Asset.Symbol == "B3SA3" and\
       Holdings[0].Asset.Company_Name == "B3 SA" and\
       Holdings[0].Asset.Category.Category == "STOCK" and\
       Holdings[0].Amount == 10:
        print("SelectBySymbol_Test - PASSED")
    else:
        print("SelectBySymbol_Test - FAILED")

    return Holdings


def SelectByCategory_Test(repo):
    Holdings = repo.Select(category="REIT")

    if Holdings[0].Asset.Symbol == "KNCR11" and\
       Holdings[0].Asset.Company_Name == "FII KINEA RI CI" and\
       Holdings[0].Asset.Category.Category == "REIT" and\
       Holdings[0].Amount == 20:
        print("SelectByCategory_Test - PASSED")
    else:
        print("SelectByCategory_Test - FAILED")

    return Holdings


# ***********************************************
__CreateTestDatabase()
print()

ca1 = Category(Category="STOCK")
ca2 = Category(Category="REIT")
repo = CategoryRepository(DBConnectionHandler(path))
repo.Insert(ca1)
repo.Insert(ca2)

a1 = Asset("B3SA3", "B3 SA", 0.00, 1)
a2 = Asset("KNCR11", "FII KINEA RI CI", 0.00, 2)
repo = AssetRepository(DBConnectionHandler(path))
repo.Insert(a1)
repo.Insert(a2)

h1 = Holding(asset_id=1, amount=10, average_price=100.00)
h2 = Holding(asset_id=2, amount=20, average_price=300.00)
h3 = Holding(asset=a1, amount=20, average_price=300.00)
repo = HoldingRepository(DBConnectionHandler(path))
repo.Insert(h1)
repo.Insert(h2)
repo.Insert(h3)

shareholding = SelectAll_Test(repo)
SelectBySymbol_Test(repo)
SelectByCategory_Test(repo)
print()

for h in shareholding:
    print(h)

__RemoveTableFromDatabase()