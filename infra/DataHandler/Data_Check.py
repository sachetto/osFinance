import os

class DataCheck:
    def __init__(self, path):
        self.__path = path

    def __ListFilesInDir(self):
        return os.listdir(self.__path)

    def ListDotDBFiles(self):
        files = self.__ListFilesInDir()
        return [file for file in files if file.endswith('.db')]

    def ListDotXlsxFiles(self):
        files = self.__ListFilesInDir()
        return [file for file in files if file.endswith('.xlsx')]
    
    def IsThereWalletFile(self):
        return (len(self.ListDotDBFiles()) > 0)
    
    def IsThereStocksFile(self):
        return (len(self.ListDotXlsxFiles()) > 0)