from datetime import datetime
import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from datetime import timedelta
from Entities.Holding import Holding
from Entities.Asset import Asset
from Entities.Category import Category
from DataHandler.PDF_Report_Exporter import PDF


# ****************************************
a1 = Asset("B3SA3", "B3 SA", 0.00, 1)
a2 = Asset("KNCR11", "FII KINEA RI CI", 0.00, 2)

h1 = Holding(asset=a1, amount=100, average_price=10.0)
h2 = Holding(asset=a2, amount=100, average_price=10.0)
h3 = Holding(asset=a2, amount=100, average_price=10.0)

info = [{"Asset": "PETR4", "Profit": \
            {datetime.today().date(): 1.1,\
            datetime.today().date() + timedelta(days=1): 1.3,\
            datetime.today().date() + timedelta(days=4): -1.3},\
            "Holding": h1},\
        {"Asset": "VALE3", "Profit": \
            {datetime.today().date(): 1.1,\
            datetime.today().date() + timedelta(days=1): 1.3,},\
            "Holding": h2},\
        {"Asset": "B3SA3", "Profit": \
            {datetime.today().date(): 1.1,\
            datetime.today().date() + timedelta(days=1): 1.3,\
            datetime.today().date() + timedelta(days=3): 1.3,\
            datetime.today().date() + timedelta(days=4): 1.3,\
            datetime.today().date() + timedelta(days=5): 1.3,\
            datetime.today().date() + timedelta(days=2): 1.3,},\
            "Holding": h2},\
        {"Asset": "BBAS3", "Profit": \
            {datetime.today().date(): -1.1,\
            datetime.today().date() + timedelta(days=1): 1.3,\
            datetime.today().date() + timedelta(days=2): 1.3,\
            datetime.today().date() + timedelta(days=5): 1.3,},\
            "Holding": h2},\
        {"Asset": "ABCD3", "Profit": \
            {datetime.today().date(): 1.1,\
            datetime.today().date() + timedelta(days=1): 1.3,},\
            "Holding": h2},\
        {"Asset": "ITUB4", "Profit": {},\
            "Holding": h3}]

pdf = PDF("Relatório por Ativo", "Anderson Rosa")
pdf.PrintReportByAsset(info)

# ****************************************
info2 = {datetime(2019, 1, 1):{"PETR4": 2.2, "VALE3": 1.1, "Total": 3.3},\
         datetime(2019, 2, 1):{"TIM4": 0.2, "ITSA4": 3.1, "Total": 3.3},\
         datetime(2019, 3, 1):{"PETR4": 8.2, "ITUB4":3.3, "Total": 11.5},\
        }

pdf.PrintReportByMonth(info2)
pdf.output("infra\\Reports\\ReportName.pdf")