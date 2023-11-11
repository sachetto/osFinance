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
from Repository.Share_Repository import ShareRepository

# ***********************************************
path = "share_test_db.db"

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

def InsertAndSelect_Test(s1, s2):
    repo = ShareRepository(DBConnectionHandler(path))

    dt1 = s1.Date
    am1 = s1.Amount
    tv1 = s1.Total_Value
    tp1 = s1.Type
    dt2 = s2.Date
    am2 = s2.Amount
    tv2 = s2.Total_Value
    tp2 = s2.Type

    repo.Insert(s1)
    repo.Insert(s2)

    selection = repo.Select()

    if selection[0].Date == dt1 and\
       selection[0].Amount == am1 and\
       selection[0].Total_Value == tv1 and\
       selection[0].Type == tp1 and\
       selection[1].Date == dt2 and\
       selection[1].Amount == am2 and\
       selection[1].Total_Value == tv2 and\
       selection[1].Type == tp2:
        print("InsertAndSelect_Test - PASSED")
    else:
        print("InsertAndSelect_Test - FAILED")


# ***********************************************
date = "2023-06-13"
date_obj = datetime.strptime(date, '%Y-%m-%d').date()

__CreateTestDatabase()
print()
share1 = Share(date_obj, 10, 300.00, "Buy", 1)
share2 = Share(date_obj, 100, 200.00, "Sale", 1)

InsertAndSelect_Test(share1, share2)
__RemoveTableFromDatabase()