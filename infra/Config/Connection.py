from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///bancodedados.db"
        self.__engine = self.__create_database_engine()
        self.Section = None

        
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def GetEngine(self):
        return self.__engine
    
    def __enter__(self):
        section_maker = sessionmaker(bind=self.__engine)
        self.Section = section_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Section.close()

