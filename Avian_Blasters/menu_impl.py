from Avian_Blasters.menu import MainMenu
from Avian_Blasters.controller.game_controller import GameController
from Avian_Blasters.controller.game_controller_impl import GameControllerImpl
from Avian_Blasters.scoreboard_impl import ScoreboardImpl
import pygame
import pygame_menu
import pygame_menu.events
from pygame_menu.widgets.widget.table import Table
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
    print(selection)
    DIFFICULTY[0] = selection

def set_fps(value : tuple[any, int], selection : any) -> None:
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({selection}) at index {index}')
    FPS[0] = selection

def set_name(name):
    NAME[0] = name

def play():
    """Launches the game"""
    CONTROLLER = GameControllerImpl(DIFFICULTY[0], NAME[0], FPS[0])
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
        MENU = pygame_menu.Menu('', self._width/2, self._height/2, center_content=True)
        SCORE_MENU = pygame_menu.Menu('Best Scores', self._width/2, self._height/2)
        scoreboard = ScoreboardImpl().get_scores(300)

        table : Table = None
        table = SCORE_MENU.add.table(table_id='Scoreboard', font_size=15)
        table.default_cell_padding = 5
        table.default_row_background_color = 'gray'
        table.add_row(['Position', 'Name', 'Score', 'Difficulty'],
              cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD)
        i = 1
        for row in scoreboard:
            name, score, difficulty = row
            table.add_row([str(i), name, str(score), difficulty], cell_align=pygame_menu.locals.ALIGN_LEFT)
            i += 1

        SCORE_MENU.add.button('Go Back', pygame_menu.events.BACK)
        
        MENU.add.text_input('Name :', default='', onchange=set_name)
        MENU.add.button('Play', play)
        MENU.add.selector('Difficulty :', [('Easy peasy', 3), ('Typical ride', 2), ('Hard as nails', 1)], default=0, onchange=set_difficulty)
        MENU.add.selector('FPS :', [('Smooth 60', 60), ('Typical 30', 30), ('Rough 15', 15)], default=0, onchange=set_fps)
        MENU.add.button('Scoreboard', SCORE_MENU)
        MENU.add.button('Quit', pygame_menu.events.EXIT)
        MENU.mainloop(surface)
