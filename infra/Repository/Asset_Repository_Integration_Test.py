import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from Config.Connection import DBConnectionHandler
from Entities.Asset import Asset
from Entities.Category import Category
from Repository.Asset_Repository import AssetRepository
from Repository.Category_Repository import CategoryRepository

# ***********************************************
path = "asset_it_db.db"

def __CreateTestDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Category.metadata.create_all(engine)
        Asset.metadata.create_all(engine)

def __RemoveTableFromDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Asset.metadata.drop_all(engine)
        Category.metadata.drop_all(engine)

def SelectAll_Test(repo):
    assets = repo.Select()

    if assets[0].Symbol == "B3SA3" and\
       assets[0].Company_Name == "B3 SA" and\
       assets[0].Category.Category == "STOCKS" and\
       assets[1].Symbol == "KNCR11" and\
       assets[1].Company_Name == "FII KINEA RI CI" and\
       assets[1].Category.Category == "REIT":
        print("Select_Test - PASSED")
    else:
        print("Select_Test - FAILED")
    return assets

def Print_Select(assets):
    for asset in assets:
        print(asset)

# ***********************************************
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

assets = SelectAll_Test(repo)
Print_Select(assets)

__RemoveTableFromDatabase()