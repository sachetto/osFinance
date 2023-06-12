from infra.Repository.Share_Repository import ShareRepository
from infra.Config.Connection import DBConnectionHandler
from infra.Config.Inspection import DBInspection

repo = ShareRepository()

# data = repo.Select()
# print(data)

stocks_ticker = repo.SelectDistinctSymbols()
# print(stocks_ticker)

stock_and_name = repo.SelectDistinctSymbolsAndName()
# print(stock_and_name)

stock = repo.SelectOperationsFrom("BOVA11")
# print(stock)

data = repo.GetLastShareData()
# print(data)

# ********** TESTE DO INSPECTOR **********
with DBConnectionHandler() as db:
    inspec = DBInspection(db)

    if inspec.TableExists("stock"):
        print("exist")
    else:
        print("does not exist")