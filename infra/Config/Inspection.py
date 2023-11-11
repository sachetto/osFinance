from sqlalchemy.engine import reflection

class DBInspection:
    def __init__(self, db):
        self.__engine = db.GetEngine()
        self.inspec = reflection.\
            Inspector.\
            from_engine(self.__engine)
        
    def TableExists(self, table):
        if self.inspec.has_table(table):
            return True
        else:
            return False