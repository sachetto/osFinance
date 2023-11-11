from Entities.Asset import Asset
from Entities.Category import Category
from sqlalchemy import update
from sqlalchemy.orm import joinedload

class AssetRepository:
    def __init__(self, conn_handler) -> None:
        self.__ConnectionHandler = conn_handler

    def Select(self, symbol=None):
        with self.__ConnectionHandler as db:
            if symbol == None:
                data = db.Section.query(Asset).\
                    join(Category).\
                    options(joinedload(Asset.Category)).\
                    all()
            else:
                data = db.Section.query(Asset).\
                    join(Category).\
                    options(joinedload(Asset.Category)).\
                    filter(Asset.Symbol==symbol).all()
            return data
  
    def Insert(self, new_asset):
        with self.__ConnectionHandler as db:
            entry = self.__checkIfAssetExistInDatabase(\
                new_asset)
            
            if entry is None:
                db.Section.add(new_asset)
                db.Section.commit()

    def Delete(self, symbol):
        with self.__ConnectionHandler as db:
            db.Section.query(Asset).\
                filter(Asset.Symbol==symbol).delete()
            db.Section.commit()

    def Update(self, symbol, new_asset=None, new_price=None, new_category_id=None):
        with self.__ConnectionHandler as db:
            if new_asset:
                query = update(Asset).\
                where(Asset.Symbol == symbol).\
                values(Company_Name = new_asset.Company_Name,\
                       Current_Price = new_asset.Current_Price,\
                       Category_Id = new_asset.Category_Id)
            elif new_price:
                query = update(Asset).\
                where(Asset.Symbol == symbol).\
                values(Current_Price = new_price)
            elif new_category_id:
                query = update(Asset).\
                where(Asset.Symbol == symbol).\
                values(Category_Id = new_category_id)

            db.Section.execute(query)
            db.Section.commit()

    def __checkIfAssetExistInDatabase(self, asset):
        with self.__ConnectionHandler as db:
            existing_entry = db.Section.\
                query(Asset).\
                filter_by(Symbol=asset.Symbol).\
                first()
            
            return existing_entry
