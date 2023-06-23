from Entities.Asset import Asset
from sqlalchemy import update

class AssetRepository:
    def __init__(self, conn_handler) -> None:
        self.__ConnectionHandler = conn_handler

    def Select(self, symbol=None):
        with self.__ConnectionHandler as db:
            if symbol == None:
                data = db.Section.query(Asset).all()
            else:
                data = db.Section.query(Asset).\
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

    def Update(self, symbol, new_asset):
        with self.__ConnectionHandler as db:
            query = update(Asset).\
                where(Asset.Symbol == symbol).\
                values(Company_Name = new_asset.Company_Name,\
                       Current_Price = new_asset.Current_Price,\
                       Category_Id = new_asset.Category_Id)

            db.Section.execute(query)
            db.Section.commit()

    def __checkIfAssetExistInDatabase(self, asset):
        with self.__ConnectionHandler as db:
            existing_entry = db.Section.\
                query(Asset).\
                filter_by(Symbol=asset.Symbol).\
                first()
            
            return existing_entry
