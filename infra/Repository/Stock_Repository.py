from infra.Config.Connection import DBConnectionHandler
from infra.Entities.Stock import Stock
from sqlalchemy import update

class StockRepository:
    def Select(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Stock).all()
            return data

    def SelectSpecific(self, ticker):
        with DBConnectionHandler() as db:
            data = db.Section.query(Stock).\
                   filter(Stock.Ticker==ticker).all()
            return data
    
    def Insert(self, new_stock):
        with DBConnectionHandler() as db:
            entry = self.__checkIfStockExistInDatabase(\
                new_stock)
            
            if entry is None:
                db.Section.add(new_stock)
                db.Section.commit()

    def Delete(self, ticker):
        with DBConnectionHandler() as db:
            db.Section.query(Stock).\
                filter(Stock.Ticker==ticker).delete()
            db.Section.commit()

    def Update(self, ticker, new_stock):
        with DBConnectionHandler() as db:
            query = update(Stock).\
                where(Stock.Ticker == ticker).\
                values(Company = new_stock.Company,\
                       Price = new_stock.Price,\
                       Category = new_stock.Category)

            db.Section.execute(query)
            db.Section.commit()

    def __checkIfStockExistInDatabase(self, stock):
        with DBConnectionHandler() as db:
            existing_entry = db.Section.\
                query(Stock).\
                filter_by(Ticker=stock.Ticker).\
                first()
            
            return existing_entry
