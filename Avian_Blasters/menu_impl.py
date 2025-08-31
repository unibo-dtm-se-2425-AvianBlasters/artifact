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

DIFFICULTY = [3]
NAME = [""]
FPS = [60]

class MainMenuImpl(MainMenu):

    def __init__(self):
        root = Tk()

        # getting screen's height in pixels
        self._height = root.winfo_screenheight()

        # getting screen's width in pixels
        self._width = root.winfo_screenwidth()

        pygame.init()

        self._surface = pygame.display.set_mode((self._width/2, self._height/2), pygame.RESIZABLE)
        self._MENU = pygame_menu.Menu('', self._width/2, self._height/2, center_content=True)
        self._SCORE_MENU = pygame_menu.Menu('Best Scores', self._width/2, self._height/2)
        self._table_number = 0
        self._table : Table = None
        
    def initiate(self):
        self._SCORE_MENU.add.button('Go Back', pygame_menu.events.BACK)
        self._table = self._SCORE_MENU.add.table(table_id=str(self._table_number), font_size=int(self._width*0.009))
        self._build_table(self._table, 0, 300)
        
        self._MENU.add.text_input('Name :', default='', onchange=self._set_name)
        self._MENU.add.button('Play', self.play)
        self._MENU.add.selector('Difficulty :', [('Easy peasy', 3), ('Typical ride', 2), ('Hard as nails', 1)], default=0, onchange=self._set_difficulty)
        self._MENU.add.selector('FPS :', [('Smooth 60', 60), ('Typical 30', 30), ('Rough 15', 15)], default=0, onchange=self._set_fps)
        self._MENU.add.button('Scoreboard', self._SCORE_MENU)
        self._MENU.add.button('Reset', self.reset_secoreboard, ScoreboardImpl(), self._table)
        self._MENU.add.button('Quit', pygame_menu.events.EXIT)
        self._MENU.mainloop(self._surface)

    def reset_secoreboard(self, scoreboard : ScoreboardImpl, table : Table):
        scoreboard.reset_scoreboard()
        self._build_table(table, 0, 300)
        self._table._id = self._table_number
        self._SCORE_MENU.render()

    def _build_table(self, table : Table, beginning : int, end : int):
        scoreboard = ScoreboardImpl().get_scores(300)
        length = len(scoreboard)

        if beginning > length:
            return

        if len(table._rows) > 0:
            self._SCORE_MENU.remove_widget(str(self._table_number))
            self._table_number += 1
            table = None
            table = self._SCORE_MENU.add.table(table_id=str(self._table_number), font_size=int(self._width*0.009))
            print('Reset scoreboard')
        table.default_cell_padding = 6
        table.default_row_background_color = 'gray'

        i = 1
        if (end>length):
            end = length
        for row in scoreboard[beginning:end]:
            name, score, difficulty = row
            table.add_row([str(i + beginning), name, str(score), difficulty], cell_align=pygame_menu.locals.ALIGN_LEFT)
            i += 1
            if table.get_height() > self._SCORE_MENU.get_height() * 2/3:
                break
        table._max_height = (self._height / 3, True, True)
        table.resize(width = table.get_width(), height = table.get_height())
    
    def play(self):
        """Launches the game"""
        controller = GameControllerImpl(DIFFICULTY[0], NAME[0], FPS[0])
        if controller.initialize():
            controller.run()
        else:
            print("Failed to initialize game. Please check your pygame installation.")
    
    def _set_difficulty(self, value : tuple[any, int], selection : any) -> None:
        selected, index = value
        print(f'Selected difficulty: "{selected}" ({selection}) at index {index}')
        DIFFICULTY[0] = selection

    def _set_fps(self, value : tuple[any, int], selection : any) -> None:
        selected, index = value
        print(f'Selected difficulty: "{selected}" ({selection}) at index {index}')
        FPS[0] = selection

    def _set_name(name : str):
        NAME[0] = name[:30]

    def __are_there_still_elements(self, value: int):
        scoreboard = ScoreboardImpl().get_scores(300)
        length = len(scoreboard)

