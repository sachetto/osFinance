import pandas as pd
from datetime import datetime

# Indice, Data, Tipo, 
# Mercado, Titulo, Ticker,
# Qnt , Preco, Valor

class DataImporter:
    def __init__(self, path):
        self.__raw_share_list = pd.read_excel(path)

    def ImportData(self):
        share_list = []
        for index, row in self.__raw_share_list.iterrows():
            date = row['Data'].strftime('%Y-%m-%d')
            amount = row['Qnt']
            total_value = row['Valor']
            share_type = "Buy" if row['Tipo'] == "C" else "Sale"
            symbol = row['Ticker']
            company_name = row['Titulo']
            share_list.append([date, amount, total_value\
                        , share_type, symbol, company_name])
            
        return share_list
    
    def GetAssetList(self):
        asset_list = []
        raw_asset_list = self.__raw_share_list.groupby('Ticker').head(1)
        for index, row in raw_asset_list.iterrows():
            symbol = row['Ticker']
            company_name = row['Titulo']
            asset_list.append([symbol, company_name])
            
        return asset_list
    
    def GetLastShareDate(self):
        date = self.__raw_share_list.iloc[-1]['Data']
        return datetime.strptime(date.strftime('%Y-%m-%d'), '%Y-%m-%d').date()
    
    def GetFirstShareDate(self):
        date = self.__raw_share_list.iloc[0]['Data']
        return datetime.strptime(date.strftime('%Y-%m-%d'), '%Y-%m-%d').date()