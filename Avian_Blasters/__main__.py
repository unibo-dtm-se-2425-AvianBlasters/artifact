from Avian_Blasters.controller.game_controller_impl import GameControllerImpl, TARGET_FPS
from Avian_Blasters.menu_impl import MainMenuImpl

def main():
    """Main entry point for Avian Blasters game"""
    menu = MainMenuImpl()
    menu.initiate()
    game_controller = GameControllerImpl(3, "Test", TARGET_FPS)
    if game_controller.initialize():
        game_controller.run()
    else:
        print("Failed to initialize game. Please check your pygame installation.")

if __name__ == "__main__":
    main()
else:
    # For compatibility with python -m Avian_Blasters
    main()
