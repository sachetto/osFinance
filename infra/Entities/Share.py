from infra.Config.Base import Base
from sqlalchemy import Column, Integer, String\
    , Date, Float

# Define the class representing the table
class Share(Base):
    __tablename__ = 'ordens'

    indice = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    tipo = Column(String)
    titulo = Column(String)
    symbol = Column(String)
    qnt = Column(Float)
    preco = Column(Float)

    def __repr__(self):
        return f"<Share (indice='{self.indice}', \
                data='{self.data}', tipo='{self.tipo}', \
                titulo='{self.titulo}', symbol='{self.symbol}', \
                qnt={self.qnt}, preco={self.preco})>\n"
