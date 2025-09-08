import os
from Avian_Blasters.menu import MainMenu
from Avian_Blasters.controller.game_controller_impl import GameControllerImpl
from Avian_Blasters.scoreboard_impl import ScoreboardImpl
import pygame
import pygame_menu
import pygame_menu.events
from pygame_menu.widgets.widget.table import Table
from tkinter import *
from tkinter.ttk import *
from pygame_menu.widgets.core import Selection

from Avian_Blasters.sound_manager_impl import SoundManagerImpl

class MenuSelection(Selection):
    def __init__(self, border_width, margin_x, margin_y):
        super().__init__(margin_left=margin_x, margin_right=margin_x, margin_top=margin_y, margin_bottom=margin_y)
        self.border_width = border_width

    def draw(self, surface, widget):
        rect = widget.get_rect()
        pygame.draw.rect(surface, (255, 220, 0), rect, self.border_width)

class MainMenuImpl(MainMenu):

    def __init__(self):

        root = Tk()

        # getting screen's height in pixels
        self._height = root.winfo_screenheight()

        # getting screen's width in pixels
        self._width = root.winfo_screenwidth()

        self._menu_theme = pygame_menu.themes.Theme(
            background_color=(0, 130, 250),             
            title_background_color=(0, 130, 250),
            title_font_color=(255, 220, 0),            
            title_font=pygame_menu.font.FONT_8BIT,
            title_font_size=40,
            title_offset=(self._width//12, 30),
            widget_font_color=(255, 255, 255),         
            widget_font=pygame_menu.font.FONT_MUNRO,
            widget_font_size=20,
            widget_background_color=(255, 100, 0),     
            widget_border_color=(255, 220, 0),         
            widget_border_width=2,
            widget_padding=(5, 20),
            widget_margin=(5, 10),
            widget_selection_effect=MenuSelection(border_width=4, margin_x=0, margin_y=0)
        )

        self._scoreboard_theme = pygame_menu.themes.Theme(
            background_color=(0, 130, 250),             
            title_background_color=(0, 130, 250),
            title_font_color=(255, 220, 0),            
            title_font=pygame_menu.font.FONT_8BIT,
            title_font_size=20,
            title_offset=(self._width//5.5, 30),
            widget_font_color=(255, 255, 255),         
            widget_font=pygame_menu.font.FONT_MUNRO,
            widget_font_size=15,
            widget_background_color=(255, 100, 0),     
            widget_border_color=(255, 220, 0),
            widget_border_width=2,
            widget_padding=(5, 10),
            widget_margin=(0, 5),
            widget_selection_effect=MenuSelection(border_width=4, margin_x=0, margin_y=0)
        )

        self._sound_manager = SoundManagerImpl()
        self._menu_music_path = 'assets' + os.sep + 'music' + os.sep + 'menu_music.mp3'
        self._game_music_path = 'assets' + os.sep + 'music' + os.sep + 'game_music.mp3' # Music by Ievgen Poltavskyi from Pixabay

        pygame.init()
        self._surface = pygame.display.set_mode((self._width/2, self._height/2), pygame.RESIZABLE)
        self._MENU = pygame_menu.Menu('AVIAN BLASTERS', self._width/2, self._height/2, center_content=True, theme=self._menu_theme)
        self._SCORE_MENU = pygame_menu.Menu('Best Scores', self._width/2, self._height/2, theme=self._scoreboard_theme)
        self._table_number = 0
        self._table : Table = None
        self._highest = 0
        self._max = 300
        self._fps = 60
        self._name = ""
        self._difficulty = 3
        
    def initiate(self):
        self._sound_manager.play_music(self._menu_music_path)
        self._SCORE_MENU.add.button('Go Back', pygame_menu.events.BACK)
        self._table = self._SCORE_MENU.add.table(table_id=str(self._table_number), font_size=int(self._width*0.009))
        self._build_table(self._table, self._highest)
        
        self._MENU.add.text_input('Name :', default='', onchange=self._set_name)
        self._MENU.add.button('Play', self.play)
        self._MENU.add.selector('Difficulty :', [('Easy peasy', 3), ('Typical ride', 2), ('Hard as nails', 1)], default=0, onchange=self._set_difficulty)
        self._MENU.add.selector('FPS :', [('Smooth 60', 60), ('Typical 30', 30), ('Rough 15', 15)], default=0, onchange=self._set_fps)
        self._MENU.add.button('Scoreboard', self._SCORE_MENU)
        self._MENU.add.button('Reset', self._reset_secoreboard, self._table)
        self._MENU.add.button('Quit', pygame_menu.events.EXIT)
        self._SCORE_MENU.add.button('Higher scores', self._build_table, self._table, -self._max)
        self._SCORE_MENU.add.button('Lower scores', self._build_table, self._table, self._max)
        self._reset_secoreboard(self._table)
        self._MENU.mainloop(self._surface)

    def _reset_secoreboard(self, table : Table):
        ScoreboardImpl().reset_scoreboard()
        self._build_table(table, 0)
        self._SCORE_MENU.render()

    def _build_table(self, table : Table, beginning : int):
        scoreboard = ScoreboardImpl().get_scores(300)
        length = len(scoreboard)
        
        if self._highest + beginning <= 0:
            beginning = 0
            self._highest = 0
        elif self._highest + beginning <= length:
            self._highest += beginning
        beginning = self._highest

        print(self._highest)

        if len(table._rows) > 0:
            self._SCORE_MENU.remove_widget(str(self._table_number))
            self._table_number += 1
            table = None
            table = self._SCORE_MENU.add.table(table_id=str(self._table_number), font_size=int(self._width*0.009))
            print('Reset scoreboard')
        table.default_cell_padding = 6
        table.default_row_background_color = (0, 90, 200)
        

        end = beginning + self._max
        if end > length:
            print(end)
            end = length

        i = 1 
        for row in scoreboard[beginning:end]:
            name, score, difficulty = row
            table.add_row([str(i + beginning), name, str(score), difficulty], cell_align=pygame_menu.locals.ALIGN_LEFT)
            i += 1
            if table.get_height() > self._SCORE_MENU.get_height() * 2/4:
                break
        if self._table_number == 0:
            self._max = min(i - 1, self._max)
        table._max_height = (self._height / 3, True, True)
        self._SCORE_MENU.render()
    
    def play(self):
        controller = GameControllerImpl(self._difficulty, self._name, self._fps)
        if controller.initialize():
            print("Game Start")
            self._sound_manager.stop_music()
            self._sound_manager.play_music(self._game_music_path, volume=0.3)
            controller.run()
        else:
            print("Failed to initialize game. Please check your pygame installation.")
        self._sound_manager.stop_music()
        self._sound_manager.play_music(self._menu_music_path)
        self._surface = pygame.display.set_mode((self._width/2, self._height/2), pygame.RESIZABLE)
    
    def _set_difficulty(self, value : tuple[any, int], selection : any) -> None:
        selected, index = value
        print(f'Selected difficulty: "{selected}" ({selection}) at index {index}')
        self._difficulty = selection

    def _set_fps(self, value : tuple[any, int], selection : any) -> None:
        selected, index = value
        print(f'Selected difficulty: "{selected}" ({selection}) at index {index}')
        self._fps = selection

    def _set_name(self, name : str):
        self._name = name[:30]

