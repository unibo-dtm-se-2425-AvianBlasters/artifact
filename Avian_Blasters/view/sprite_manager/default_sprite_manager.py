import pygame
import os
from typing import Tuple
from Avian_Blasters.view.sprite_manager.abstract_sprite_manager import AbstractSpriteManager
from Avian_Blasters.model.entity import Entity

class DefaultSpriteManager(AbstractSpriteManager):
    """SpriteManagerImpl is the default implementation of SpriteManager"""
    
    def __init__(self):
        super().__init__(path = 'assets' + os.sep + 'sprites.png',
                       sprite_definitions = {
                            Entity.TypeArea.PLAYER: {
                                'positions': [(24, 280, 64, 40), (124, 280, 64, 40)],  # Player sprites where we found green pixels
                                'size': (16, 10)
                            },
                            Entity.TypeArea.ENEMY: {
                                'positions': [(26, 24, 64, 44), (120, 24, 64, 44),  # birds
                                             (304, 24, 64, 44), (344, 24, 60, 44)],   # bats
                                'size': (16, 10)
                            },
                            Entity.TypeArea.PLAYER_PROJECTILE: {
                                'positions': [(216, 292, 12, 20)],  # Projectiles
                                'size': (12, 20)
                            },
                            Entity.TypeArea.ENEMY_PROJECTILE: {
                                'positions': [(216, 35, 12, 20), (532, 32, 64, 44)],  # Enemy projectiles
                                'size': (12, 20)
                            },
                            Entity.TypeArea.POWERUP: {
                                'positions': [(143, 28, 12, 40), (120, 40, 16, 16), (120, 60, 16, 16)],  # Power-ups
                                'size': (16, 16)
                            }
                        })
        
        
    def load_sprites(self) -> bool:
        return super().load_sprites()

    def get_sprite(self, entity_type: Entity.TypeArea, variant: int = 0) -> pygame.Surface:
        return super().get_sprite(entity_type, variant)
    
    def get_sprite_size(self, entity_type: Entity.TypeArea) -> Tuple[int, int]:
        return super().get_sprite_size(entity_type)
    
    def is_loaded(self) -> bool:
        return super().is_loaded()
    
    def _create_fallback_sprite(self, entity_type: Entity.TypeArea) -> pygame.Surface:
        # Use the same colors as before for fallback
        colours = {
            Entity.TypeArea.PLAYER: (0, 255, 0),             # Green
            Entity.TypeArea.ENEMY: (255, 0, 0),              # Red
            Entity.TypeArea.PLAYER_PROJECTILE: (0, 0, 255),  # Blue
            Entity.TypeArea.ENEMY_PROJECTILE: (128, 0, 128), # Purple
            Entity.TypeArea.POWERUP: (255, 255, 0)           # Yellow
        }
        
        return super()._create_fallback_sprite(entity_type, colours)
