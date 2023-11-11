from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
engine = create_engine('sqlite:///your_database.db')
Base = declarative_base()

# Define the class representing the table
class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    indice = Column(String)
    data = Column(Date)
    tipo = Column(String)
    titulo = Column(String)
    symbol = Column(String)
    qnt = Column(Integer)
    preco = Column(Float)

    def __repr__(self):
        return f"<Operation(id={self.id}, indice='{self.indice}', data='{self.data}', tipo='{self.tipo}', titulo='{self.titulo}', symbol='{self.symbol}', qnt={self.qnt}, preco={self.preco})>"

# Create the table in the database (if it doesn't exist)
Base.metadata.create_all(engine)




# ***********************************************
# Define the options
options = [
    ('option 1', 'Option 1'),
    ('option 2', 'Option 2'),
    ('option 3', 'Option 3'),
]

# Show the radiolist dialog
selected_option = radiolist_dialog(
    title='Select an option:',
    text='',
    values=options,
).run()

print(f'Selected option: {selected_option}')