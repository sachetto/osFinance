from prompt_toolkit.shortcuts import radiolist_dialog\
    , input_dialog, button_dialog

class ScreenBuilder:
    def __init__(self):
        self.__screen_txt_pos = 0
        self.__screen_options_pos = 1
        self.screen_type_pos = 2
        self.screen_texts = {
            'screen1': ['Selecione a carteira que deseja trabalhar:',\
                        [('1', 'NaN'),\
                         ('2', 'NaN')],\
                        self.__radiolist_dialog],
            'xlsx_share_files_screen': ['Selecione o arquivo a ser importado:',\
                        [('1', 'NaN'),\
                         ('2', 'NaN')],\
                        self.__radiolist_dialog],
            'report_screen': ['Selecione o Relatório desejado:',\
                         [('shareholding', 'Posição Atual'),\
                          ('monthly_report', 'Relatório de compra e venda mensal'),\
                          ('list_categories', 'Listar Categorias'),\
                          ('last_share_date', 'Exibir data da última operação processada')],\
                         self.__radiolist_dialog],
            'naming_wallet_screen': ['Digite o nome da Carteira que deseja criar:',\
                         [], self.__input_dialog],
            'ask_to_create_wallet_screen': ['Não há carteiras processadas, deseja criar uma?.',\
                         [('Sim', 'yes'),\
                         ('Não', 'no')],\
                         self.__button_dialog],
            'app_functions_screen': ['Deseja gerar um relatório, importar novos dados '+\
                        'ou sair',\
                         [('Relatório', 'report'),\
                         ('Importar', 'import'),\
                         ('Configurar', 'configurate'),\
                         ('Sair', 'quit')],\
                         self.__button_dialog],
            'configure_screen': ['Qual configuração deseja fazer?',\
                         [('Cadastrar nova categoria', 'register_category'),\
                         ('Atribuir categoria', 'set_category'),\
                         ('Voltar ao menu principal', 'back_app_functions'),\
                         ('Sair', 'quit')],\
                         self.__button_dialog],
            'list_categories_screen': ['Estas são as categorias já cadastradas?',\
                         [('Nova', 'register'),\
                         ('Voltar', 'back_config')],\
                         self.__button_dialog],
            'naming_category_screen': ['Digite o NOME da nova categoria:\n',\
                         [], self.__input_dialog],
            'list_asset_and_category_screen': ['Selecione uma asset para atribuit/editar sua categoria:',\
                         [('1', 'NaN'),\
                         ('2', 'NaN')],\
                         self.__radiolist_dialog],
            'select_category_to_update_asset_screen': ['Selecione a categoria desejada:',\
                         [('1', 'NaN'),\
                         ('2', 'NaN')],\
                         self.__radiolist_dialog],
            'waiting_screen': ['Informação: ',\
                         [('Ok', 'register')],\
                         self.__button_dialog],
        }

    def __radiolist_dialog(self, screen_options):
        selected_option = radiolist_dialog(
            title='Prompt Dialog',
            text=screen_options[self.__screen_txt_pos],
            values=screen_options[self.__screen_options_pos],
        ).run()
        return selected_option
    
    def __input_dialog(self, screen_options):
        selected_option = input_dialog(
            title='Prompt Dialog',
            text=screen_options[self.__screen_txt_pos],
        ).run()
        return selected_option

    def __button_dialog(self, screen_options):
        selected_option = button_dialog(
            title='Prompt Dialog',
            text=screen_options[self.__screen_txt_pos],
            buttons=screen_options[self.__screen_options_pos],
        ).run()
        return selected_option
    
    '''
    This function updates the screen options, based on the
    screen type.
        - When the screen is a radiolist_dialog, the screen 
        options are a list of tuples used to create the 
        radiolist.
        - When the screen is a button_dialog, the screen 
        options are a list of text only, used as information.
    '''
    def UpdateScreenOptions(self, screen_name, screen_options):
        if self.screen_texts[screen_name][self.screen_type_pos]\
           == self.__radiolist_dialog:
            
            self.screen_texts[screen_name][self.__screen_options_pos] \
            = []

            for op in screen_options:
                self.screen_texts[screen_name][self.__screen_options_pos]\
                .append((op, op))
        
        if self.screen_texts[screen_name][self.screen_type_pos]\
           == self.__button_dialog:
            
            title = self.screen_texts[screen_name][self.__screen_txt_pos]\
                .split('\n')[0]
            self.screen_texts[screen_name][self.__screen_txt_pos] = title

            for op in screen_options:
                self.screen_texts[screen_name][self.__screen_txt_pos] = \
                self.screen_texts[screen_name][self.__screen_txt_pos]\
                + '\n' + ' - ' + op