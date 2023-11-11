from Data_Check import DataCheck
import os

path = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra\Data'

db_files = ['test.db', 'test2.db']
xlsx_files = ['test.xlsx', 'test2.xlsx']

def __CreateDBFile():
    with open(path + r'\\'+ db_files[0], 'w') as file:
        file.write('test')
    with open(path + r'\\'+ db_files[1], 'w') as file:
        file.write('test2')
    with open(path + r'\\'+ 'Testeeee', 'w') as file:
        file.write('test2')

def __DeleteAllDBFiles():
    for file in db_files:
        os.remove(path + r'\\' + file)

def __CreateXlsxFile():
    with open(path + r'\\'+ xlsx_files[0], 'w') as file:
        file.write('test')
    with open(path + r'\\'+ xlsx_files[1], 'w') as file:
        file.write('test2')

def __DeleteAllXlsxFiles():
    for file in xlsx_files:
        os.remove(path + r'\\' + file)

def ListDotDBFiles_Teste():
    __CreateDBFile()

    data_check = DataCheck(path)
    files_listed = data_check.ListDotDBFiles()
    
    if any (file in files_listed for file in db_files):
        print('ListDotDBFiles_Teste - PASSED')
    else:
        print('ListDotDBFiles_Teste - FAILED')

    __DeleteAllDBFiles()

def ListDotXlsxFiles_Teste():
    __CreateXlsxFile()

    data_check = DataCheck(path)
    files_listed = data_check.ListDotXlsxFiles()
    
    if any (file in files_listed for file in xlsx_files):
        print('ListDotXlsxFiles_Teste - PASSED')
    else:
        print('ListDotXlsxFiles_Teste - FAILED')

    __DeleteAllXlsxFiles()

# ------------------------------------------------------

ListDotDBFiles_Teste()
ListDotXlsxFiles_Teste()