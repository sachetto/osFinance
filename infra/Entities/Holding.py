from Config.Base import Base
from sqlalchemy import Column, Integer\
    , Date, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Holding(Base):
    __tablename__ = 'Holding'

    Id = Column(Integer, primary_key=True, autoincrement=True)
    Asset_Id = Column(Integer, ForeignKey('Asset.Id'))
    Amount = Column(Integer)
    Average_Price = Column(Float)

    Asset = relationship("Asset")

    def __init__(
            self, asset_id=None, asset=None,
            amount=None, average_price=None):
        if asset_id == None and asset is not None:
            self.Asset = asset
            self.Amount = amount
            self.Average_Price = average_price
        elif asset_id is not None and asset == None\
                and amount is not None and\
                average_price is not None:    
            self.Asset_Id = asset_id
            self.Amount = amount
            self.Average_Price = average_price

    def __str__(self):
        return (self.Asset.Symbol + "\t" + \
                str(self.Amount) + "\t" + \
                str(self.Average_Price) + "\t" +\
                self.Asset.Category.Category)

    def __repr__(self):
        return f"<Holding: Id='{self.Id}', \
                Asset='{self.Asset}',\
                Amount='{self.Amount}', \
                Average_Price='{self.Average_Price}'\n>"
        