import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from Config.Connection import DBConnectionHandler
from Entities.Asset import Asset
from Entities.Category import Category
from Repository.Asset_Repository import AssetRepository

# ***********************************************
path = "asset_test_db.db"

def __CreateTestDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Category.metadata.create_all(engine)
        Asset.metadata.create_all(engine)

def __RemoveTableFromDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Asset.metadata.drop_all(engine)

def InsertAndSelect_Test(a1, a2, a3):
    repo = AssetRepository(DBConnectionHandler(path))

    s1 = a1.Symbol
    s2 = a2.Symbol
    cn1 = a1.Company_Name
    cn2 = a2.Company_Name
    cp1 = a1.Current_Price
    cp2 = a2.Current_Price
    cid1 = a1.Category_Id
    cid2 = a2.Category_Id

    repo.Insert(a1)
    repo.Insert(a2)
    # Used to check if will not add 2 times the same
    # asset
    repo.Insert(a3)

    # Selecting data
    selection = repo.Select()

    if selection[0].Symbol == s1 and\
        selection[0].Company_Name == cn1 and\
        selection[0].Current_Price == cp1 and\
        selection[0].Category_Id == cid1 and\
        selection[1].Symbol == s2 and\
        selection[1].Company_Name == cn2 and\
        selection[1].Current_Price == cp2 and\
        selection[1].Category_Id == cid2:

        if len(selection) == 2:
            print("InsertAndSelect_Test - PASSED")
            return
    
    print("InsertAndSelect_Test - FAILED")
            
def SelectSpecificSymbol_Test(asset):
    repo = AssetRepository(DBConnectionHandler(path))
    
    symb = asset.Symbol
    cn = asset.Company_Name
    cp = asset.Current_Price
    cid = asset.Category_Id
    
    selection = repo.Select(symb)
    
    if selection[0].Symbol == symb and\
       selection[0].Company_Name == cn and\
       selection[0].Current_Price == cp and\
       selection[0].Category_Id == cid:
        print("SelectSpecificSymbol_Test - PASSED")
    else:
        print("SelectSpecificSymbol_Test - FAILED")

def Update_Test(symbol_to_update, new_asset):
    repo = AssetRepository(DBConnectionHandler(path))

    symb = new_asset.Symbol
    cn = new_asset.Company_Name
    cp = new_asset.Current_Price
    cid = new_asset.Category_Id
    
    repo.Update(symbol_to_update, new_asset)

    # Selecting data
    selection = repo.Select(symbol_to_update)
    
    if selection[0].Symbol == symb and\
        selection[0].Company_Name == cn and\
        selection[0].Current_Price == cp and\
        selection[0].Category_Id == cid:
        print("Update_Test - PASSED")
    
    else:
        print("Update_Test - FAILED")

def Delete_Test(symbol_to_be_deleted):
    repo = AssetRepository(DBConnectionHandler(path))
    selection = repo.Select(symbol_to_be_deleted)

    if len(selection) != 0:
        repo.Delete(symbol_to_be_deleted)

        selection = repo.Select(symbol_to_be_deleted)
        if len(selection) == 0:
            print("Delete_Test - PASSED")
        
    else:
        print("Delete_Test - FAILED")

            
        





# ***********************************************
__CreateTestDatabase()
print()

asset1 = Asset("OIBR3", "OI SA", 0.0, 1)
asset2 = Asset("B3SA3", "B3 SA", 0.0, 1)
# Used to check if will not add 2 times the same
# asset
asset3 = Asset("B3SA3", "B3 SA", 0.4, 1)
InsertAndSelect_Test(asset1, asset2, asset3)

asset1 = Asset("OIBR3", "OI SA", 0.0, 1)
SelectSpecificSymbol_Test(asset1)

asset4 = Asset("OIBR3", "OI S/A", 1.0, 1)
Update_Test(asset1.Symbol, asset4)

Delete_Test("B3SA3")

__RemoveTableFromDatabase()