from Entities.Share import Share
from Entities.Asset import Asset

class ShareRepository:
    def __init__(self, conn_handler) -> None:
        self.__ConnectionHandler = conn_handler

    def Select(self, symbol=None):
        with self.__ConnectionHandler as db:
            if symbol is None:
                rows = db.Section.query(Share).all()
            else:
                rows = db.Section.query(Share)\
                       .join(Asset)\
                       .filter(Asset.symbol == symbol)\
                       .all()
            return rows

    def Insert(self, new_share):
        with self.__ConnectionHandler as db:
            db.Section.add(new_share)
            db.Section.commit()

    def GetLastShareData(self):
        with self.__ConnectionHandler as db:
            data = db.Section.query(Share.Date)\
                .order_by(Share.indice.desc()).first()
            
            return data[0]            