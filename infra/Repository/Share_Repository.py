from datetime import datetime
from Entities.Share import Share
from Entities.Asset import Asset
from Entities.Category import Category
from sqlalchemy.orm import joinedload

class ShareRepository:
    def __init__(self, conn_handler) -> None:
        self.__ConnectionHandler = conn_handler

    def Select(self, symbol=None, operation_type=None):
        with self.__ConnectionHandler as db:
            if symbol is None:
                rows = db.Section.query(Share).\
                       join(Asset).\
                       join(Category).\
                       options(joinedload(Share.Asset).\
                       joinedload(Asset.Category)).\
                       all()
            elif operation_type is None:
                rows = db.Section.query(Share).\
                       join(Asset).\
                       join(Category).\
                       options(joinedload(Share.Asset).\
                       joinedload(Asset.Category)).\
                       filter(Asset.Symbol == symbol).\
                       all()
            else:
                rows = db.Section.query(Share).\
                       join(Asset).\
                       join(Category).\
                       options(joinedload(Share.Asset).\
                       joinedload(Asset.Category)).\
                       filter(Asset.Symbol == symbol, \
                              Share.Type == operation_type).\
                       all()
            return rows

    def Insert(self, new_share):
        with self.__ConnectionHandler as db:
            db.Section.add(new_share)
            db.Section.commit()

    def GetLastShareDate(self):
        with self.__ConnectionHandler as db:
            data = db.Section.query(Share.Date)\
                .order_by(Share.Id.desc()).first()
            
            if data is None:
                return datetime.min.date()
            else:
                return data[0]            