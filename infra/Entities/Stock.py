from infra.Config.Base import Base
from sqlalchemy import Column, Integer, String\
    , Float

# Define the class representing the table
class Stock:
    __tablename__ = 'stock'

    Id = Column(Integer, primary_key=True)
    Ticker = Column(String)
    Company_name = Column(String)
    Current_price = Column(Float)
    Category = Column(String)

    def __repr__(self):
        return f"<Stock: Id='{self.Id}',\
            Ticker='{self.Ticker}',\
            Company='{self.Company_name}',\
            Price='{self.Current_price}',\
            Category='{self.Category}'>"