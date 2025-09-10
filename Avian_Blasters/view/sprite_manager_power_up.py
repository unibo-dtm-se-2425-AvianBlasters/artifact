import os
from typing import Tuple
import pygame
from Avian_Blasters.model.item.power_up.power_up import PowerUp, PowerUpType
from Avian_Blasters.view.abstract_sprite_manager import AbstractSpriteManager


class SpriteManagerPowerUp(AbstractSpriteManager):
    def __init__(self):
        super().__init__(path = 'assets' + os.sep + 'sprites' + os.sep + 'Power-Ups.png',
                         sprite_definitions = {
                             PowerUpType.INVULNERABILITY: {
                                'positions': [(28, 25, 25, 23)],
                                'size': (25, 23)
                            },
                            PowerUpType.DOUBLE_FIRE: {
                                'positions': [(80, 27, 29, 21)],
                                'size': (29, 21)
                            },
                            PowerUpType.LASER: {
                                'positions': [(140, 25, 19, 29)],
                                'size': (19, 29)
                            },
                            PowerUpType.HEALTH_RECOVERY: {
                                'positions': [(198, 27, 18, 21)],
                                'size': (18, 21)
                            }
                         })
        
    
    def load_sprites(self) -> bool:
        return super().load_sprites()
    
    def get_sprite(self, power_up: PowerUp, variant: int = 0) -> pygame.Surface:
        power_up_type = power_up.power_up_type
        if not self._loaded or power_up_type not in self._sprites:
            return self._create_fallback_sprite(power_up_type)
        sprites = self._sprites[power_up_type]
        if variant >= len(sprites):
            variant = 0 
        return sprites[variant]
    
    def get_sprite_size(self, power_up_type: PowerUpType) -> Tuple[int, int]:
        return self.get_sprite_size(power_up_type)
    
    def is_loaded(self) -> bool:
        return super().is_loaded()
    
    def _create_fallback_sprite(self, power_up_type: PowerUpType) -> pygame.Surface:
        
        colors = {
            PowerUpType.INVULNERABILITY: (0, 0, 255),      
            PowerUpType.DOUBLE_FIRE: (255, 165, 0),        
            PowerUpType.LASER: (255, 0, 0),                
            PowerUpType.HEALTH_RECOVERY: (0, 255, 0) 
        }
    
        return super()._create_fallback_sprite(power_up_type, colors)
        