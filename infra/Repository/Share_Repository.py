from infra.Config.Connection import DBConnectionHandler
from infra.Entities.Share import Share

class ShareRepository:
    def Select(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Share).all()
            return data
        
    def SelectOperationsFrom(self, symbol):
        with DBConnectionHandler() as db:
            rows = db.Section.query(Share)\
                .filter(Share.ticker == symbol).all()
            return rows
        
    def SelectDistinctSymbols(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Share.ticker).distinct().all()
            
            # Get the distinct values as a list using list comprehension
            data = [value[0] for value in data]
            return data
   
    def SelectDistinctSymbolsAndName(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Share.ticker, Share.titulo)\
                .distinct().all()
            
            # Get the distinct values as a list using list comprehension
            data = [[value[0], value[1]] for value in data]
            return data

    def Insert(self, new_share):
        with DBConnectionHandler() as db:
            db.Section.add(new_share)
            db.Section.commit()

    def GetLastShareData(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Share.data)\
                .order_by(Share.indice.desc()).first()
            
            return data[0]            