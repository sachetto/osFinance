from infra.Config.Connection import DBConnectionHandler
from infra.Entities.Stock import Stock

class StockRepository:
    def Select(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Stock).all()
            return data
        
    def Insert(self, new_stock):
        with DBConnectionHandler() as db:
            entry = self.__checkIfStockExistInDatabase(\
                new_stock)
            
            if entry is None:
                db.Section.add(new_stock)
                db.Section.commit()

    def __checkIfStockExistInDatabase(self, stock):
        with DBConnectionHandler() as db:
            existing_entry = db.Section.\
                query(Stock).\
                filter_by(Ticker=stock.Ticker).\
                first()
            
            return existing_entry
            
            