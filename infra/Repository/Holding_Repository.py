from Entities.Category import Category
from Entities.Asset import Asset
from Entities.Holding import Holding
from sqlalchemy import update
from sqlalchemy.orm import joinedload

class HoldingRepository:
    def __init__(self, conn_handler) -> None:
        self.__ConnectionHandler = conn_handler

    def Select(self, symbol=None, category=None):
        with self.__ConnectionHandler as db:
            if symbol == None and category == None:
                data = db.Section.query(Holding).\
                    join(Asset).\
                    join(Category).\
                    options(joinedload(Holding.Asset).\
                    joinedload(Asset.Category)).\
                    all()
            elif symbol != None:
                data = db.Section.query(Holding).\
                    join(Asset).\
                    join(Category).\
                    options(joinedload(Holding.Asset).\
                    joinedload(Asset.Category)).\
                    filter(Asset.Symbol==symbol).all()
            else:
                data = db.Section.query(Holding).\
                    join(Asset).\
                    join(Category).\
                    options(joinedload(Holding.Asset).\
                    joinedload(Asset.Category)).\
                    filter(Category.Category==category).all()
                
            return data
        
    def Insert(self, new_Holding):
        with self.__ConnectionHandler as db:
            db.Section.add(new_Holding)
            db.Section.commit()