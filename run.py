from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog, button_dialog

class AppState:
    def __init__(self):
        self.__stxtpos = 0
        self.__soppos = 1
        self.state = 'screen1'
        self.handlers = {
            'screen1': self.handle_screen1,
            'screen2': self.handle_screen2,
            'screen3': self.handle_screen3,
            'screen4': self.handle_screen4,
            'screen5': self.handle_screen5,
        }
        self.screen_texts = {
            'screen1': ['Select an option in Screen 1:', [('1', 'Option 1'), ('2', 'Option 2')]],
            'screen2': ['Select an option in Screen 2:', [('1', 'Option 1'), ('2', 'Option 2')]],
            'screen3': ['Select an option in Screen 3:', [('1', 'Option 1'), ('2', 'Option 2')]],
            'screen4': ['Enter a value in Screen 4:'],
            'screen5': ['Press OK to continue in Screen 5.'],
        }

    def handle_input(self, user_input):
        # handler becomes a reference to the 
        # corresponding handler method
        handler = self.handlers.get(self.state)
        if handler:
            handler(user_input)

    def handle_screen1(self, user_input):
        if user_input == '1':
            print('Option 1 selected in Screen 1')
        elif user_input == '2':
            print('Option 2 selected in Screen 1')
            self.state = 'screen2'

    def handle_screen2(self, user_input):
        if user_input == '1':
            print('Option 1 selected in Screen 2')
        elif user_input == '2':
            print('Option 2 selected in Screen 2')
            self.state = 'screen3'

    def handle_screen3(self, user_input):
        if user_input == '1':
            print('Option 1 selected in Screen 3')
        elif user_input == '2':
            print('Option 2 selected in Screen 3')
            self.state = 'screen4'

    def handle_screen4(self, user_input):
        if user_input:
            print(f'Input value in Screen 4: {user_input}')
            self.state = 'screen5'

    def handle_screen5(self, user_input):
        if user_input == 'OK':
            print('OK button pressed in Screen 5')
            self.state = 'screen1'

    def run(self):
        while True:
            handler = self.handlers.get(self.state)
            if handler:
                handler(None)  # Handle the screen transition
            else:
                break

            screen_text = self.screen_texts.get(self.state)
            if self.state == 'screen4':
                input_value = input_dialog(
                    title='Prompt Dialog',
                    text=screen_text[self.__stxtpos],
                ).run()
                self.handle_input(input_value)
            elif self.state == 'screen5':
                button_dialog(
                    title='Prompt Dialog',
                    text=screen_text[self.__stxtpos],
                    buttons=[('OK', 'OK')],
                ).run()
                self.handle_input('OK')
            else:
                selected_option = radiolist_dialog(
                    title='Prompt Dialog',
                    text=screen_text[self.__stxtpos],
                    values=screen_text[self.__soppos],
                ).run()

                self.handle_input(selected_option)

# Example usage
app_state = AppState()
app_state.run()
