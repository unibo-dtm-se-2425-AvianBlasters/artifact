import pygame
from typing import Dict, Tuple, Optional
from Avian_Blasters.view.abstract_sprite_manager import AbstractSpriteManager
from Avian_Blasters.model.character.player import Player
from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus
import os

class SpriteManagerPlayer(AbstractSpriteManager):
    """SpriteManagerImpl is the implementation of SpriteManager
    handling the sprites linked to the player character"""
    
    def __init__(self):
        super().__init__(path = 'assets' + os.sep + 'sprites' + os.sep + 'Car_V3.png',
                       sprite_definitions = {
                           5: {
                               'positions': [(23, 307, 64, 40), (120, 307, 64, 40)],
                               'size': (16, 10)
                               }, 
                            4: {
                                'positions': [(23, 249, 64, 40), (120, 249, 64, 40)],
                                'size': (16, 10)
                                },
                            3: {
                                'positions': [(24, 18, 64, 40), (121, 18, 64, 40)],
                                'size': (16, 10)
                                },
                            2: {
                                'positions': [(24, 78, 64, 40), (121, 78, 64, 40)],
                                'size': (16, 10)
                                },
                            1: {
                                'positions': [(24, 134, 64, 40), (121, 134, 64, 40)],
                                'size': (16, 10)
                            },
                            0: {
                                'positions': [(24, 191, 64, 40), (121, 191, 64, 40)],
                                'size': (16, 10)
                            }
                        }
                    )
    
    def load_sprites(self) -> bool:
        return super().load_sprites()
    
    def get_sprite(self, player : Player, variant: int = 0) -> pygame.Surface:
        image = player.get_health_handler().current_health
        if player.is_hurt():
            image = 0
        elif player.get_status().status == PlayerStatus.Status.INVULNERABLE:
            image = 5
        elif player.get_power_up_handler().get_current_power_up() is not None:
            image = 4
        return super().get_sprite(image, variant)
    
    def get_sprite_size(self, index : int) -> Tuple[int, int]:
        return super().get_sprite_size(index)
    
    def is_loaded(self) -> bool:
        return super().is_loaded()
    
    def _create_fallback_sprite(self, current_health : int) -> pygame.Surface:
        colours = {
            5: (0, 0, 255),      # Blue
            4: (255, 69, 0),     # Orange
            3: (0, 255, 0),      # Green
            2: (255, 255, 0),    # Yellow
            1: (255, 0, 0),      # Red
            0: (255, 255, 255)   # White 
        }
        return super()._create_fallback_sprite(current_health, colours)
