from Avian_Blasters.controller.game_controller_impl import GameControllerImpl

def main():
    """Main entry point for Avian Blasters game"""
    game_controller = GameControllerImpl()
    
    if game_controller.initialize():
        game_controller.run()
    else:
        print("Failed to initialize game. Please check your pygame installation.")

if __name__ == "__main__":
    main()
else:
    # For compatibility with python -m Avian_Blasters
    main()
