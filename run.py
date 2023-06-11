from infra.Repository.Share_Repository import ShareRepository

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
print(data)