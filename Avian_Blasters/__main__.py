from Avian_Blasters.menu.menu_impl import MainMenuImpl

def main():
    """Main entry point for Avian Blasters game"""
    menu = MainMenuImpl()
    menu.initiate()

if __name__ == "__main__":
    main()
else:
    # For compatibility with python -m Avian_Blasters
    main()
