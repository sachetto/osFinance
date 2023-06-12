from infra.Config.Base import Base
from sqlalchemy import Column, Integer, String\
    , Float

# Define the class representing the table
class Stock(Base):
    __tablename__ = 'stock'

    Id = Column(Integer, primary_key=True)
    Ticker = Column(String)
    Company = Column(String)
    Price = Column(Float)
    Category = Column(String)

    def __repr__(self):
        return f"<Stock: Id='{self.Id}',\
            Ticker='{self.Ticker}',\
            Company='{self.Company}',\
            Price='{self.Price}',\
            Category='{self.Category}'\n>"