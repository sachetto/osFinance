import sys

# Absolute path to the directory containing the module
module_dir = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra'
# Add the module directory to the Python module search path
sys.path.append(module_dir)

from ApplicationManager	import ApplicationManager
from infra.DataHandler.PDF_Report_Exporter import PDF

class ScreenState:
    def __init__(self, screen_builder):
        self.DataPath = r'G:\Meu Drive\Minhas Financas\Investimentos\Notas de negociação Clear\BOT - 2023\Nova Abordagem\infra\Data'
        self.CurrentWalletFullPath = None
        self.CurrentWalletName = None
        self.CurrentAssetSymbol = None
        self.ApplicationManager = ApplicationManager(self)
        self.ScreenBuilder = screen_builder
        
        self.State = 'screen1'
        self.handlers = {
            'screen1': self.handle_screen1,
            'report_screen': self.handle_report_screen,
            'screen3': self.handle_screen3,
            'naming_wallet_screen': self.handle_naming_wallet_screen,
            'ask_to_create_wallet_screen': self.handle_ask_to_create_wallet,
            'app_functions_screen': self.handle_app_functions_screen,
            'xlsx_share_files_screen': self.handle_xlsx_share_files_screen,
            'configure_screen': self.handle_configure_screen,
            'list_categories_screen': self.handle_list_categories_screen,
            'naming_category_screen': self.handle_naming_category_screen,
            'list_asset_and_category_screen': self.handle_list_asset_and_category_screen,
            'select_category_to_update_asset_screen': self.handle_select_category_to_update_asset_screen,
            'waiting_screen': self.handle_waiting_screen,
        }
        self.ScreenTexts = screen_builder.screen_texts
        self.__screen_type_pos = screen_builder.screen_type_pos
        
    def handle_input(self, user_input):
        # handler becomes a reference to the 
        # corresponding handler method
        handler = self.handlers.get(self.State)
        if handler:
            handler(user_input)

    def handle_screen1(self, user_input):
        wallet_database = user_input
        if wallet_database:
            if wallet_database == 'Criar nova carteira':
                self.State = 'naming_wallet_screen'
            else:
                self.CurrentWalletName = wallet_database.split('.')[0]
                self.CurrentWalletFullPath = self.DataPath + '\\' + wallet_database
                self.State = 'app_functions_screen'
        else:
            self.State = None

    def handle_report_screen(self, user_input):
        if user_input == None:
            self.State = 'app_functions_screen'
        if user_input == 'shareholding':
            self.State = 'waiting_screen'
            self.ApplicationManager.GetShareholdingPosition(
                self.CurrentWalletFullPath
                )
            self.ApplicationManager.UpdateHoldingTable(
                self.CurrentWalletFullPath
                )
            self.ScreenBuilder.UpdateScreenOptions(
                self.State,\
                ["Em construção..."]
                )
        elif user_input == 'monthly_report':
            self.State = 'waiting_screen'
            self.ScreenBuilder.UpdateScreenOptions(
                self.State,\
                ["Aguarde até o relatório ser salvo e aberto"]
                )
            asset_repo = self.ApplicationManager.GetReportByAsset(
                self.CurrentWalletFullPath
                )
            mon_report = self.ApplicationManager.GetMonthlyReport(
                asset_repo
                )
            pdf = PDF("Relatório Mensal", "Anderson Rosa")
            pdf.PrintReportByMonth(mon_report)
            pdf.output("infra\\Reports\\" + self.CurrentWalletName + ".pdf")
        elif user_input == '2':
            self.State = 'screen3'

    def handle_screen3(self, user_input):
        if user_input == '1':
            self.State = 'screen1'
        elif user_input == '2':
            self.State = 'naming_wallet_screen'

    def handle_naming_wallet_screen(self, user_input):
        if user_input:
            new_wallet_db = self.DataPath + '\\' + user_input + '.db'
            self.ApplicationManager.CreateMyWalletDatabase(new_wallet_db)
            self.CurrentWalletFullPath = new_wallet_db

            self.State = 'app_functions_screen'
        else:
            self.State = 'naming_wallet_screen'

    def handle_ask_to_create_wallet(self, user_input):
        if user_input == 'yes':
            self.State = 'naming_wallet_screen'
        else:
            self.State = None

    def handle_app_functions_screen(self, user_input):
        if user_input == 'report':
            self.State = 'report_screen'
        elif user_input == 'import':
            self.State = 'xlsx_share_files_screen'
            xlsx_share_files = self.ApplicationManager.GetShareFiles()
            self.ScreenBuilder.UpdateScreenOptions(self.State, xlsx_share_files)
        elif user_input == 'configurate':
            self.State = 'configure_screen'
        else:
            self.State = None

    def handle_xlsx_share_files_screen(self, user_input):
        result = ""
        if user_input != self.ApplicationManager.no_valid_xlsx_file \
        and user_input != None:
            self.ApplicationManager.UpdateAssetTable(
                self.CurrentWalletFullPath, user_input)
            result = self.ApplicationManager.UpdateShareTable(
                self.CurrentWalletFullPath, user_input)
            self.State = None
            self.State = 'waiting_screen'

        if result == "Imported":
            self.ScreenBuilder.UpdateScreenOptions(
                self.State,\
                ["Dados importados com sucesso!"]
                )
            self.State = 'waiting_screen'
        elif result == "Invalid date":
            self.ScreenBuilder.UpdateScreenOptions(
                self.State,\
                ["Confira as datas. Operações importadas anteriormente!"]
                )
        else:
            self.State = 'app_functions_screen'

    def handle_configure_screen(self, user_input):
        if user_input == 'register_category':
            categories_already_registrated = \
                self.ApplicationManager.GetCategoryList(
                    self.CurrentWalletFullPath
                    )
            self.State = 'list_categories_screen'
            self.ScreenBuilder.UpdateScreenOptions(
                self.State,\
                categories_already_registrated
                )
        elif user_input == 'set_category':
            self.State = 'list_asset_and_category_screen'
            asset_list = self.ApplicationManager.GetAssetList(
                    self.CurrentWalletFullPath
                    )[self.ApplicationManager.asset_as_string_position]
            self.ScreenBuilder.UpdateScreenOptions(
                    'list_asset_and_category_screen', asset_list)
            
        elif user_input == 'back_app_functions':
            self.State = 'app_functions_screen'
        else:
            self.State = None

    def handle_list_categories_screen(self, user_input):
        if user_input == 'back_config':
            self.State = 'configure_screen'
        else:
            self.State = 'naming_category_screen'

    def handle_naming_category_screen(self, user_input):
        if user_input:
            self.ApplicationManager.UpdateCategoryTable(
                self.CurrentWalletFullPath,\
                user_input
                )

        self.State = 'configure_screen'

    def handle_list_asset_and_category_screen(self, user_input):
        if user_input:
            self.CurrentAssetSymbol = self.ApplicationManager.\
                GetAssetSymbol(
                    user_input
                )
            
            categories_already_registrated = \
                self.ApplicationManager.GetCategoryList(
                    self.CurrentWalletFullPath
                    )
            self.ScreenBuilder.UpdateScreenOptions(
                'select_category_to_update_asset_screen',\
                categories_already_registrated
                )

            self.State = 'select_category_to_update_asset_screen'
        
        else:
            self.State = 'configure_screen'

    def handle_select_category_to_update_asset_screen(self, user_input):
        if user_input:
            self.ApplicationManager.UpdateAssetCategory(
                self.CurrentWalletFullPath,\
                self.CurrentAssetSymbol,\
                user_input
                )
            
        self.State = 'configure_screen'

    def handle_waiting_screen(self, user_input):
        self.State = 'app_functions_screen'

    def Run(self):
        [self.State, wallet_options] = self.ApplicationManager.SetupFirstState()
        
        if wallet_options:
            self.ScreenBuilder.UpdateScreenOptions(self.State, wallet_options)

        while self.State != None:
            screen_options = self.ScreenTexts.get(self.State)

            handler = screen_options[self.__screen_type_pos]
            if handler:
                # Handle the screen 
                selected_option = handler(screen_options)  
            else:
                self.State = None
                return

            self.handle_input(selected_option)

   