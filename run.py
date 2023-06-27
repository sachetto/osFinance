from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog\
    , input_dialog, button_dialog

class AppState:
    def __init__(self):
        self.__stxtpos = 0
        self.__soppos = 1
        self.__kofsc = 2
        self.state = 'screen1'
        self.handlers = {
            'screen1': self.handle_screen1,
            'screen2': self.handle_screen2,
            'screen3': self.handle_screen3,
            'screen4': self.handle_screen4,
            'screen5': self.handle_screen5,
        }
        self.screen_texts = {
            'screen1': ['Select an option in Screen 1:', [('1', 'Jump to screen 2'), ('2', 'Jump to screen 3')], self.radiolist_dialog],
            'screen2': ['Select an option in Screen 2:', [('1', 'Back to screen 1'), ('2', 'Jump to screen 3')], self.radiolist_dialog],
            'screen3': ['Select an option in Screen 3:', [('1', 'Back to screen 1'), ('2', 'Jump to screen 4')], self.radiolist_dialog],
            'screen4': ['Enter a value in Screen 4:', [], self.input_dialog],
            'screen5': ['Press OK to continue in Screen 5.', [('Continue', 'Continue'), ('Quit', 'Quit')], self.button_dialog],
        }

    def radiolist_dialog(self, screen_options):
        selected_option = radiolist_dialog(
            title='Prompt Dialog',
            text=screen_options[self.__stxtpos],
            values=screen_options[self.__soppos],
        ).run()
        return selected_option
    
    def input_dialog(self, screen_options):
        selected_option = input_dialog(
            title='Prompt Dialog',
            text=screen_options[self.__stxtpos],
        ).run()
        return selected_option

    def button_dialog(self, screen_options):
        selected_option = button_dialog(
            title='Prompt Dialog',
            text=screen_options[self.__stxtpos],
            buttons=screen_options[self.__soppos],
        ).run()
        return selected_option

    def handle_input(self, user_input):
        # handler becomes a reference to the 
        # corresponding handler method
        handler = self.handlers.get(self.state)
        if handler:
            handler(user_input)

    def handle_screen1(self, user_input):
        if user_input == '1':
            self.state = 'screen2'
        elif user_input == '2':
            self.state = 'screen3'

    def handle_screen2(self, user_input):
        if user_input == '1':
            self.state = 'screen1'
        elif user_input == '2':
            self.state = 'screen3'

    def handle_screen3(self, user_input):
        if user_input == '1':
            self.state = 'screen1'
        elif user_input == '2':
            self.state = 'screen4'

    def handle_screen4(self, user_input):
        if user_input:
            if user_input == 'restart':
                self.state = 'screen1'
            else:
                self.state = 'screen5'

    def handle_screen5(self, user_input):
        if user_input == 'Continue':
            self.state = 'screen1'
        else:
            self.state = None

    def run(self):
        while self.state != None:
            screen_options = self.screen_texts.get(self.state)

            handler = screen_options[self.__kofsc]
            if handler:
                selected_option = handler(screen_options)  # Handle the screen
            else:
                break

            self.handle_input(selected_option)

# Example usage
app_state = AppState()
app_state.run()
