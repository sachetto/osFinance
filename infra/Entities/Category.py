from Config.Base import Base
from sqlalchemy import Column, Integer, String

# Define the class representing the table
class Category(Base):
    __tablename__ = 'Category'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Category = Column(String)

    def __repr__(self):
        return f"<Category: Id='{self.Id}',\
            Category='{self.Category}'\n>"