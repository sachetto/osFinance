from infra.Config.Connection import DBConnectionHandler
from infra.Entities.Asset import Asset
from sqlalchemy import update

class AssetRepository:
    def Select(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Asset).all()
            return data

    def SelectSpecific(self, ticker):
        with DBConnectionHandler() as db:
            data = db.Section.query(Asset).\
                   filter(Asset.Ticker==ticker).all()
            return data
    
    def Insert(self, new_asset):
        with DBConnectionHandler() as db:
            entry = self.__checkIfAssetExistInDatabase(\
                new_asset)
            
            if entry is None:
                db.Section.add(new_asset)
                db.Section.commit()

    def Delete(self, ticker):
        with DBConnectionHandler() as db:
            db.Section.query(Asset).\
                filter(Asset.Ticker==ticker).delete()
            db.Section.commit()

    def Update(self, ticker, new_asset):
        with DBConnectionHandler() as db:
            query = update(Asset).\
                where(Asset.Ticker == ticker).\
                values(Company = new_asset.Company,\
                       Price = new_asset.Price,\
                       Category = new_asset.Category)

            db.Section.execute(query)
            db.Section.commit()

    def __checkIfAssetExistInDatabase(self, asset):
        with DBConnectionHandler() as db:
            existing_entry = db.Section.\
                query(Asset).\
                filter_by(Ticker=asset.Ticker).\
                first()
            
            return existing_entry
