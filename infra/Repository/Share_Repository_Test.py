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
        Asset.metadata.drop_all(engine)


date = "2023-06-13"
date_obj = datetime.strptime(date, '%Y-%m-%d').date()

share1 = Share(date_obj, 10, 300.00, "Buy", 1)
print(share1)