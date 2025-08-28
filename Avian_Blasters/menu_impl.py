from Avian_Blasters.menu import MainMenu
from Avian_Blasters.controller.game_controller import GameController
from Avian_Blasters.controller.game_controller_impl import GameControllerImpl
import pygame
import pygame_menu
import pygame_menu.events
import pygame_menu.widgets
from tkinter import *
from tkinter.ttk import *

MENU : pygame_menu.Menu = None
SCORE_MENU: pygame_menu.Menu = None
DIFFICULTY = [2]
NAME = [""]
FPS = [60]

def set_difficulty(value : tuple[any, int], selection : any) -> None:
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({selection}) at index {index}')
    DIFFICULTY[0] = index

def set_fps(value : tuple[any, int], selection : any) -> None:
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({selection}) at index {index}')
    print(selection)
    FPS[0] = selection

def set_name(name):
    NAME[0] = name

def play():
    """Launches the game"""
    CONTROLLER = GameControllerImpl(DIFFICULTY[0] + 1, NAME, FPS[0])
    if CONTROLLER.initialize():
        CONTROLLER.run()
    else:
        print("Failed to initialize game. Please check your pygame installation.")
    
CONTROLLER = None


class MainMenuImpl(MainMenu):

    def __init__(self):
        root = Tk()

        # getting screen's height in pixels
        self._height = root.winfo_screenheight()

        # getting screen's width in pixels
        self._width = root.winfo_screenwidth()

        pygame.init()    
        
    def initiate(self):
        surface = pygame.display.set_mode((self._width/2, self._height/2), pygame.RESIZABLE)
        MENU = pygame_menu.Menu("Avian Blasters", self._width/2, self._height/2, center_content=True)
        SCORE_MENU = pygame_menu.Menu('Best Scores', self._width/2, self._height/2)
        SCORE_MENU.add.button('Go Back', pygame_menu.events.BACK)
        table = pygame_menu.widgets.Table(3, 20)

        
        MENU.add.text_input('Name :', default='', onchange=set_name)
        MENU.add.button('Play', play)
        MENU.add.selector('Difficulty :', [('Hard as nails', 1), ('Typical ride', 2), ('Easy peasy', 3)], default=2, onchange=set_difficulty)
        MENU.add.selector('FPS :', [('Smooth 60', 60), ('Typical 30', 30), ('Rough 15', 15)], default=0, onchange=set_fps)
        MENU.add.button('Scoreboard', SCORE_MENU)
        MENU.add.button('Quit', pygame_menu.events.EXIT)
        MENU.mainloop(surface)
