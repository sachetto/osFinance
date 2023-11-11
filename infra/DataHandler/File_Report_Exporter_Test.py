import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from DataHandler.File_Report_Exporter import FileExporter

# ***********************************************
path = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra\Reports'


file_title = 'Título do arquivo \n'
file_data = 'Linha 1 \nLinha 2 \nLinha 3 \t ainda na linha 3 tabulado.'

file_info = file_title + file_data

file_exporter = FileExporter(path)
file_exporter.Save('test_report.txt', file_info)

file_exporter.DisplayReportFile('test_report.txt')

# ***********************************************