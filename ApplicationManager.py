from datetime import datetime
from infra.Config.Connection import DBConnectionHandler
from infra.DataHandler.Data_Check import DataCheck
from infra.DataHandler.Data_Importer import DataImporter
from infra.Repository.Asset_Repository import AssetRepository, Asset
from infra.Repository.Category_Repository import CategoryRepository, Category
from infra.Repository.Share_Repository import ShareRepository, Share
from infra.Repository.Holding_Repository import HoldingRepository, Holding

class ApplicationManager:
    def __init__(self, screen_state):
        self.data_path = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra\Data'
        self.data_check = DataCheck(self.data_path)
        self.screen_state = screen_state
        self.no_valid_xlsx_file = 'Nenhum arquivo válido encontrado'
        self.my_wallet_db_name = ''
        self.xlsx_asset_list = []
        self.asset_as_object_position = 0
        self.asset_as_string_position = 1
        self.holding_list = []
    
    def SetupFirstState(self):
        if not self.data_check.IsThereWalletFile():
            return ['ask_to_create_wallet_screen', None]
        else:
            wallets = self.data_check.ListDotDBFiles()
            wallets.insert(0, 'Criar nova carteira')

            return ['screen1', wallets]
        
    def CreateMyWalletDatabase(self, wallet_db_name):
        self.my_wallet_db_name = wallet_db_name
        with DBConnectionHandler(wallet_db_name) as db_conn:
            engine = db_conn.GetEngine()
            Category.metadata.create_all(engine)
            Asset.metadata.create_all(engine)
            Share.metadata.create_all(engine)

            CategoryRepository(db_conn).InsertUndefinedCategory()

    def GetShareFiles(self):
        xlsx = self.data_check.ListDotXlsxFiles()
        if xlsx:
            return xlsx
        else:
            return [self.no_valid_xlsx_file]
        
    def UpdateAssetTable(self, wallet_db_name, share_file_name):
        data_importer = DataImporter(self.data_path +'\\'+ share_file_name)
        self.xlsx_asset_list = data_importer.GetAssetList()
        
        with DBConnectionHandler(wallet_db_name) as db_conn:
            asset_repository = AssetRepository(db_conn)
            undefined_category_id = CategoryRepository(db_conn)\
                .SelectUndefinedCategoryID()
            
            for asset_info in self.xlsx_asset_list:
                asset = Asset(
                    asset_info[0],
                    asset_info[1],
                    0.0,
                    category_id = undefined_category_id
                )
                asset_repository.Insert(asset)

    def UpdateShareTable(self, wallet_db_name, share_file_name):
        data_importer = DataImporter(self.data_path +'\\'+ share_file_name)

        with DBConnectionHandler(wallet_db_name) as db_conn:
            share_repository = ShareRepository(db_conn)
            asset_repository = AssetRepository(db_conn)
            
            if (self.__ValidateShareByDate(share_repository.GetLastShareDate(), data_importer.GetLastShareDate())):
                for asset_info in data_importer.ImportData():
                    asset = asset_repository.Select(asset_info[4])
                    asset_id = asset[0].Id
                    
                    share = Share(datetime.strptime(asset_info[0], "%Y-%m-%d").date(),
                                asset_info[1],
                                asset_info[2],
                                asset_info[3],
                                asset_id)
                    
                    share_repository.Insert(share)
                
                return "Imported"
            else:
                return "Invalid date"

    def GetCategoryList(self, wallet_db_name):
        with DBConnectionHandler(wallet_db_name) as db_conn:
            category_list = []
            for category in CategoryRepository(db_conn).Select():
                category_list.append(category.Category)
            
            return category_list
        
    def UpdateCategoryTable(self, wallet_db_name, category):
        with DBConnectionHandler(wallet_db_name) as db_conn:
            repo = CategoryRepository(db_conn)
            repo.Insert(Category(Category=category))

    def GetAssetList(self, wallet_db_name):
        with DBConnectionHandler(wallet_db_name) as db_conn:
            asset_list_as_object = []
            asset_list_as_str = []
            for asset in AssetRepository(db_conn).Select():
                asset_list_as_object.append(asset)
                asset_list_as_str.append(str(asset))
            
            return [asset_list_as_object, asset_list_as_str]
        
    def __ValidateShareByDate(self, share_date, xlsx_share_date):
        return share_date < xlsx_share_date

    def __SplitAssetInfo(self, asset_info):
        return asset_info.split(' - ')
    
    def GetAssetSymbol(self, asset_info):
        return self.__SplitAssetInfo(asset_info)[0]

    def UpdateAssetCategory(self, wallet_db_name, asset_symbol, category):
        with DBConnectionHandler(wallet_db_name) as db_conn:
            asset_repo = AssetRepository(db_conn)
            category_repo = CategoryRepository(db_conn)

            category_id = category_repo.Select(category).Id

            asset_repo.Update(
                asset_symbol,
                new_category_id=category_id)
            

# *********************************************************
# This is a proof of concept draft
# *********************************************************
    def __CalcProfitBySale(self, sale_share, holding):
        this_share_sale_average_price = sale_share.Total_Value/sale_share.Amount
        profit = this_share_sale_average_price - holding.Average_Price
        return profit * sale_share.Amount


    def GetReportByAsset(self, wallet_db_name):
        asset_report = []
        asset_list = self.GetAssetList(
            wallet_db_name)[self.asset_as_object_position]
        
        with DBConnectionHandler(wallet_db_name) as db_conn:
            for asset in asset_list:
                buy_asset_share, sell_asset_share = \
                    self.__GetBuyAndSaleShareList(asset, 
                                                  db_conn)
                
                profit_by_sale = dict()
                
                if sell_asset_share != []:
                    this_holding = Holding(asset=asset, amount=0, average_price=0.0)
                    buy_idx = 0
                    sale_idx = 0
                    buy_share_in_the_period = []
                    remaining_amount = 0
                    process_buy = False
                    process_sale = False
                    while buy_idx < len(buy_asset_share) or sale_idx < len(sell_asset_share):
                        if buy_idx < len(buy_asset_share):
                            process_buy = True
                            buy_share = buy_asset_share[buy_idx]
                        else:
                            process_buy = False
                        
                        if sale_idx < len(sell_asset_share):
                            if buy_share.Date > sell_asset_share[sale_idx].Date:
                                process_sale = True

                        if process_buy and not process_sale:
                            buy_share_in_the_period.append(buy_share)
                            buy_idx += 1
                        else:
                            if this_holding.Amount != 0:
                                holding_as_share = Share(datetime.today().date(),
                                                        this_holding.Amount,
                                                        this_holding.Average_Price * this_holding.Amount,
                                                        "Buy",
                                                        this_holding.Asset.Id)
                                buy_share_in_the_period.append(holding_as_share)

                            qnt_buy_share_in_the_period = self.__GetQntOfBuyAsset(buy_share_in_the_period)    
                            average_buy_price = self.__CalcPMC(buy_share_in_the_period, qnt_buy_share_in_the_period)
                            remaining_amount = qnt_buy_share_in_the_period - sell_asset_share[sale_idx].Amount
                            this_holding.Amount = remaining_amount
                            this_holding.Average_Price = average_buy_price

                            profit_by_sale[sell_asset_share[sale_idx].Date] = \
                                self.__CalcProfitBySale(sell_asset_share[sale_idx], this_holding)
                            
                            buy_share_in_the_period = []
                            sale_idx += 1

                        process_sale = False
                    
                    if len(buy_share_in_the_period) > 0:
                        # When there is no sale in the period or when the last sale is before the last buy
                        if this_holding.Amount != 0:
                            holding_as_share = Share(datetime.today().date(),
                                                    this_holding.Amount,
                                                    this_holding.Average_Price * this_holding.Amount,
                                                    "Buy",
                                                    this_holding.Asset.Id)
                            buy_share_in_the_period.append(holding_as_share)

                        qnt_buy_share_in_the_period = self.__GetQntOfBuyAsset(buy_share_in_the_period)    
                        average_buy_price = self.__CalcPMC(buy_share_in_the_period, qnt_buy_share_in_the_period)
                        this_holding.Amount = qnt_buy_share_in_the_period
                        this_holding.Average_Price = average_buy_price

                else:
                    this_holding = self.__CalcHoldingInformation(
                        buy_asset_share,
                        sell_asset_share)

                asset_report.append({"Asset": asset.Symbol, "Profit": profit_by_sale, "Holding": this_holding})

        return asset_report
    
    def GetMonthlyReport(self, asset_report):
        monthly_report = dict()   
        for asset in asset_report:
            for date, profit in asset['Profit'].items():
                temp_date = datetime(date.year, date.month, 1)
                
                if temp_date not in monthly_report:
                    monthly_report[temp_date] = {asset['Asset']: profit}
                    monthly_report[temp_date]['Total'] = profit
                else:
                    monthly_report[temp_date]['Total'] += profit

                    if asset['Asset'] not in monthly_report[temp_date]:
                        monthly_report[temp_date][asset['Asset']] = profit
                    else:
                        monthly_report[temp_date][asset['Asset']] += profit

        return monthly_report

    def GetShareholdingPosition(self, wallet_db_name):
        asset_list = self.GetAssetList(
            wallet_db_name)[self.asset_as_object_position]
        
        with DBConnectionHandler(wallet_db_name) as db_conn:
            for asset in asset_list:
                buy_asset_share, sell_asset_share = \
                    self.__GetBuyAndSaleShareList(asset, 
                                                  db_conn)

                self.holding_list.append(self.__CalcHoldingInformation(
                    buy_asset_share,
                    sell_asset_share))

    def UpdateHoldingTable(self, wallet_db_name):
        with DBConnectionHandler(wallet_db_name) as db_conn:
            holding_repo = HoldingRepository(db_conn)
            for holding in self.holding_list:
                if holding.Amount != 0:
                    holding_repo.Insert(holding)

    def __GetBuyAndSaleShareList(self, asset, db_conn):
        asset_symbol = asset.Symbol

        buy_asset_share = ShareRepository(
        db_conn).Select(
        symbol=asset_symbol,\
        operation_type="Buy")
        
        sell_asset_share = ShareRepository(
        db_conn).Select(
        symbol=asset_symbol,\
        operation_type="Sale")

        return [buy_asset_share, sell_asset_share]


    def __CalcPMC(self, buy_share_list, total_amount):
        total_buy_price = 0
        for share in buy_share_list:
            total_buy_price = total_buy_price \
                + share.Total_Value
            
        return total_buy_price/total_amount
    

    def __GetQntOfBuyAsset(self, buy_share_list):
        total_amount = 0
        for share in buy_share_list:
            total_amount = total_amount \
                + share.Amount
            
        return total_amount
    
    def __GetQntOfSaleAsset(self, sell_share_list):
        total_amount = 0
        for share in sell_share_list:
            total_amount = total_amount \
                + share.Amount

        return total_amount

    def __CalcHoldingInformation(self, buy_share_list,
                                 sell_share_list):
        
        qnt_buy_asset = self.__GetQntOfBuyAsset(buy_share_list)    
        average_buy_price = self.__CalcPMC(buy_share_list, qnt_buy_asset)
        
        qnt_sale_asset = 0
        if len(sell_share_list) != 0:
            qnt_sale_asset = self.__GetQntOfSaleAsset(sell_share_list)

        total_amount = qnt_buy_asset - qnt_sale_asset
        holding = Holding(asset=buy_share_list[0].Asset,\
                                amount=total_amount,\
                                average_price=average_buy_price)

        return holding

            
# *********************************************************
# This is a proof of concept draft
# *********************************************************