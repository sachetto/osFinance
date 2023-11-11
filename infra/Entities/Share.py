from Config.Base import Base
from sqlalchemy import Column, Integer\
    , Date, Float, String, ForeignKey
from sqlalchemy.orm import relationship

# Define the class representing the table
class Share(Base):
    __tablename__ = 'Share'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Date)
    Amount = Column(Integer)
    Total_Value = Column(Float)
    Type = Column(String)
    Asset_Id = Column(Integer, ForeignKey('Asset.Id'))

    Asset = relationship("Asset")

    def __init__(self, date, amout, total_value, type, 
                 asset_id=None, asset=None):
        if asset_id is not None:
            self.Date = date
            self.Amount = amout
            self.Total_Value = total_value
            self.Type = type
            self.Asset_Id = asset_id
        elif asset is not None:
            self.Date = date
            self.Amount = amout
            self.Total_Value = total_value
            self.Type = type
            self.Asset = asset

    def __repr__(self):
        return f"<Share: Id='{self.Id}', \
                Date='{self.Date}', Asset='{self.Asset}',\
                Amount='{self.Amount}', \
                Total_Value='{self.Total_Value}',\
                Type='{self.Type}'\n>"
