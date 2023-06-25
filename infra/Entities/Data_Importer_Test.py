from Data_Importer import DataImporter

# ***********************************************
path = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\share_test_file.xlsx'

data_importer = DataImporter(path)

def ImportData_Test():
    output_required = [
        ['2019-07-02', 100, 157.0, 'C', 'OIBR3'\
         , 'OI ON N1'],
        ['2019-07-02', 13, 85.28, 'C', 'CIEL3'\
         , 'CIELO ON'],
        ['2019-07-11', 4, 404.8, 'C', 'BOVA11'\
         , 'ISHARES BOVA CI'],
        ['2019-07-15', 12, 82.8, 'C', 'VIIA3'\
         , 'VIAVAREJO ON NM'],
        ['2019-07-15', 2, 13.8, 'C', 'VIIA3'\
         , 'VIAVAREJO ON NM'],
        ['2019-07-16', 20, 347.4, 'C', 'SINH3'\
         , 'JSL ON NM'],
        ['2019-07-16', 4, 69.48, 'C', 'SINH3'\
         , 'JSL ON NM']
    ]

    data = data_importer.InportData()

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

# ***********************************************
ImportData_Test()
GetAssetList_Test()