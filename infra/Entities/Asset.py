from Config.Base import Base
from sqlalchemy import Column, Integer, String\
    , Float, ForeignKey
from sqlalchemy.orm import relationship

# Define the class representing the table
class Asset(Base):
    __tablename__ = 'Asset'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Symbol = Column(String)
    Company_Name = Column(String)
    Current_Price = Column(Float)
    Category_Id = Column(Integer, ForeignKey('Category.Id'))

    Category = relationship("Category")

    def __init__(self, symbol, company_name, current_price, category_id):
        self.Symbol = symbol
        self.Company_Name = company_name
        self.Current_Price = current_price
        self.Category_Id = category_id

    def __str__(self):
        return f"{self.Symbol} - {self.Category.Category}"

    def __repr__(self):
        return f"<Asset: Id='{self.Id}',\
            Symbol='{self.Symbol}',\
            Company_Name='{self.Company_Name}',\
            Current_Price='{self.Current_Price}',\
            Category='{self.Category}'\n>"