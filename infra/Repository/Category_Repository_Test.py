import os
import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

import sqlite3
from Config.Connection import DBConnectionHandler
from Entities.Category import Category
from Repository.Category_Repository import CategoryRepository

# ***********************************************
path = "category_test_db.db"

def __CreateTestDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Category.metadata.create_all(engine)

def __RemoveTableFromDatabase():
    with DBConnectionHandler(path) as db_connection:
        engine = db_connection.GetEngine()
        Category.metadata.drop_all(engine)


# Adding tow categories
def InsertAndSelect_Test(c1, c2):
    with DBConnectionHandler(path) as db_connection:
        _c1 = Category(Category=c1)
        _c2 = Category(Category=c2)

        repo = CategoryRepository(db_connection)
        repo.Insert(_c1)
        repo.Insert(_c2)

        # Selecting data
        selection = repo.Select()
        if selection[0].Category == c1 and\
            selection[1].Category == c2:
            print("PASSED")

__CreateTestDatabase()

c1 = "ETF"
c2 = "BRD"
InsertAndSelect_Test(c1, c2)

__RemoveTableFromDatabase()
