from Data_Importer import DataImporter

# ***********************************************
path = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\share_test_file.xlsx'

data_importer = DataImporter(path)

def ImportData_Test():
    output_required = [
        ['2019-07-02', 100, 157.0, 'Buy', 'OIBR3'\
         , 'OI ON N1'],
        ['2019-07-02', 13, 85.28, 'Buy', 'CIEL3'\
         , 'CIELO ON'],
        ['2019-07-11', 4, 404.8, 'Buy', 'BOVA11'\
         , 'ISHARES BOVA CI'],
        ['2019-07-15', 12, 82.8, 'Buy', 'VIIA3'\
         , 'VIAVAREJO ON NM'],
        ['2019-07-15', 2, 13.8, 'Sale', 'VIIA3'\
         , 'VIAVAREJO ON NM'],
        ['2019-07-16', 20, 347.4, 'Buy', 'SINH3'\
         , 'JSL ON NM'],
        ['2019-07-16', 4, 69.48, 'Buy', 'SINH3'\
         , 'JSL ON NM']
    ]

    data = data_importer.ImportData()

    if data == output_required:
        print('DataImport_Test - PASSED')
    else:
        print('DataImport_Test - FAILED')

def GetAssetList_Test():
    output_required = [
        ['OIBR3', 'OI ON N1'],
        ['CIEL3', 'CIELO ON'],
        ['BOVA11', 'ISHARES BOVA CI'],
        ['VIIA3', 'VIAVAREJO ON NM'],
        ['SINH3', 'JSL ON NM']
    ]

    data = data_importer.GetAssetList()

    if data == output_required:
        print('GetAssetList_Test - PASSED')
    else:
        print('GetAssetList_Test - FAILED')


def GetLastShareDate_Test():
    output_required = '2019-07-16'

    date = data_importer.GetLastShareDate()
    date = date.strftime('%Y-%m-%d')

    if date == output_required:
        print('GetLastShareDate_Test - PASSED')
    else:
        print('GetLastShareDate_Test - FAILED')


def GetFirstShareDate_Test():
    output_required = '2019-07-02'

    date = data_importer.GetFirstShareDate()
    date = date.strftime('%Y-%m-%d')

    if date == output_required:
        print('GetFirstShareDate_Test - PASSED')
    else:
        print('GetFirstShareDate_Test - FAILED')


# ***********************************************
ImportData_Test()
GetAssetList_Test()
GetLastShareDate_Test()
GetFirstShareDate_Test()