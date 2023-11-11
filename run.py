from infra.Screen.Screen_Builder import ScreenBuilder
from infra.Screen.Screen_State import ScreenState

# defines the main function of the application
def main():
    screens = ScreenBuilder()
    app_state = ScreenState(screens)

    app_state.Run()



if __name__ == '__main__':
    main()