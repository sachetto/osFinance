from infra.Config.Connection import DBConnectionHandler
from infra.Entities.Share import Share

class ShareRepository:
    def Select(self):
        with DBConnectionHandler() as db:
            data = db.Section.query(Share).all()
            return data