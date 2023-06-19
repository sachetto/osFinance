from infra.Config.Base import Base
from sqlalchemy import Column, Integer, String\
    , Float, ForeignKey
from sqlalchemy.orm import relationship

# Define the class representing the table
class Stock(Base):
    __tablename__ = 'stock'

    Id = Column(Integer, primary_key=True)
    Symbol = Column(String)
    Company_Name = Column(String)
    Current_Price = Column(Float)
    Category_Id = Column(Integer, ForeignKey('Category.Id'))

    Category = relationship("Category")

    def __repr__(self):
        return f"<Stock: Id='{self.Id}',\
            Symbol='{self.Symbol}',\
            Company_Name='{self.Company_Name}',\
            Current_Price='{self.Current_Price}',\
            Category='{self.Category}'\n>"