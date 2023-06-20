from datetime import datetime
from infra.Repository.Share_Repository import ShareRepository
from infra.Repository.Asset_Repository import AssetRepository
from infra.Entities.Asset import Asset
from infra.Entities.Share import Share
from infra.Config.Connection import DBConnectionHandler
from infra.Config.Inspection import DBInspection

share_repo = ShareRepository()
asset_repo = AssetRepository()

# data = share_repo.Select()
# print(data)

assets_ticker = share_repo.SelectDistinctSymbols()
# print(assets_ticker)

asset_and_name = share_repo.SelectDistinctSymbolsAndName()
# print(asset_and_name)

asset = share_repo.SelectOperationsFrom("BOVA11")
# print(asset)

data = share_repo.GetLastShareData()
# print(data)

# *******************************************************
# Test add new share into repo
# *******************************************************
def Test_Add_Share():
    date = "2023-06-13"
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    new_share = Share(data=date_obj,
                      tipo="C",
                      titulo="OI ON N1",
                      ticker="OIBR3",
                      qnt=30.0,
                      preco=1.2)
    
    share_repo.Insert(new_share)

    data = share_repo.Select()
    print(data[-2])
    print(data[-1])

# Test_Add_Share()

# *******************************************************
# From all orders, get distincts Asset and sabe in a 
# table
# *******************************************************
def UpdateAssetTable(asset_list, asset_repo):
    for asset in asset_list:
        asset_to_insert = Asset(Ticker=asset[0],\
                                 Company=asset[1],\
                                 Price=0.0,\
                                 Category="UNDEFINED")

        asset_repo.Insert(asset_to_insert)

# UpdateAssetTable(asset_and_name, asset_repo)
# data = asset_repo.Select()
# print(data)


# *******************************************************
# Test update table
# *******************************************************
def Test_Update():
    data = asset_repo.SelectSpecific("B3SA3")
    print(data[0])
    
    asset = asset_repo.SelectSpecific("B3SA3")

    new_asset = Asset(Ticker=asset[0].Ticker,\
                      Company=asset[0].Company,\
                      Price=0.0,\
                      Category="asset")
    
    asset_repo.Update("B3SA3", new_asset)

    data = asset_repo.SelectSpecific("B3SA3")
    print(data[0])

# Test_Update()

# *******************************************************
# Test delete table
# *******************************************************
def Test_Delete():
    data = asset_repo.Select()
    print(data)
    
    asset_repo.Delete("B3SA3")

    data = asset_repo.Select()
    print(data)

# Test_Delete()


# ********** TESTE DO INSPECTOR **********
with DBConnectionHandler() as db:
    inspec = DBInspection(db)

    if inspec.TableExists("asset"):
        print("exist")
    else:
        print("does not exist")