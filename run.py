from infra.Repository.Share_Repository import ShareRepository
from infra.Repository.Stock_Repository import StockRepository
from infra.Entities.Stock import Stock
from infra.Config.Connection import DBConnectionHandler
from infra.Config.Inspection import DBInspection

share_repo = ShareRepository()
stock_repo = StockRepository()

# data = share_repo.Select()
# print(data)

stocks_ticker = share_repo.SelectDistinctSymbols()
# print(stocks_ticker)

stock_and_name = share_repo.SelectDistinctSymbolsAndName()
# print(stock_and_name)

stock = share_repo.SelectOperationsFrom("BOVA11")
# print(stock)

data = share_repo.GetLastShareData()
# print(data)

# *******************************************************
# From all orders, get distincts Stock and sabe in a 
# table
# *******************************************************
def UpdateStockTable(stock_list, stock_repo):
    for stock in stock_list:
        stock_to_insert = Stock(Ticker=stock[0],\
                                 Company=stock[1],\
                                 Price=0.0,\
                                 Category="UNDEFINED")

        stock_repo.Insert(stock_to_insert)

# UpdateStockTable(stock_and_name, stock_repo)
# data = stock_repo.Select()
# print(data)


# *******************************************************
# Test update table
# *******************************************************
def Test_Update():
    data = stock_repo.SelectSpecific("B3SA3")
    print(data[0])
    
    stock = stock_repo.SelectSpecific("B3SA3")

    new_stock = Stock(Ticker=stock[0].Ticker,\
                      Company=stock[0].Company,\
                      Price=0.0,\
                      Category="STOCK")
    
    stock_repo.Update("B3SA3", new_stock)

    data = stock_repo.SelectSpecific("B3SA3")
    print(data[0])

# Test_Update()

# *******************************************************
# Test delete table
# *******************************************************
def Test_Delete():
    data = stock_repo.Select()
    print(data)
    
    stock_repo.Delete("B3SA3")

    data = stock_repo.Select()
    print(data)

# Test_Delete()


# ********** TESTE DO INSPECTOR **********
with DBConnectionHandler() as db:
    inspec = DBInspection(db)

    if inspec.TableExists("stock"):
        print("exist")
    else:
        print("does not exist")