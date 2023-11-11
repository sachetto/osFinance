import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from ApplicationManager import ApplicationManager
from infra.DataHandler.PDF_Report_Exporter import PDF

class ApplicationManagerITC:
    def __init__(self) -> None:
        self.DataPath = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra\Data'
        # self.CurrentWallet = self.DataPath + "\\Monthly2.db"
        self.CurrentWallet = self.DataPath + "\\Anderson.db"
        self.ApplicationManager = ApplicationManager(self)

    def GetReportByAsset_Test(self):
        return self.ApplicationManager.GetReportByAsset(
            self.CurrentWallet
            )
        
    def GetMonthlyReport_Test(self, asset_repo):
        return self.ApplicationManager.GetMonthlyReport(
            asset_repo
            )

    def ReportTestList(self):
        asset_report = self.GetReportByAsset_Test()
        mon_report = self.GetMonthlyReport_Test(asset_report)

        pdf = PDF("Relatório por Ativo", "Anderson Rosa")
        pdf.PrintReportByAsset(asset_report)
        pdf.output("infra\\Reports\\ApplicationManager1_Test.pdf")
        
        pdf = PDF("Relatório Mensal", "Anderson Rosa")
        pdf.PrintReportByMonth(mon_report)
        pdf.output("infra\\Reports\\ApplicationManager2_Test.pdf")

    def UpdateShareTable_Test(self):
        share_file_name = "complex_share_test_file.xlsx"
        self.ApplicationManager.UpdateShareTable(self.CurrentWallet, share_file_name)

    def UpdateHoldingTable_Test(self):
        self.ApplicationManager.GetShareholdingPosition(self.CurrentWallet)
        self.ApplicationManager.UpdateHoldingTable(self.CurrentWallet)

if __name__ == "__main__":
    app = ApplicationManagerITC()
    # app.ReportTestList()
    # app.UpdateShareTable_Test()
    app.UpdateHoldingTable_Test()

