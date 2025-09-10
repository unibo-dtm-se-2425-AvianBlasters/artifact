import os
import pygame
from typing import Tuple
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.view.sprite_manager.abstract_sprite_manager import AbstractSpriteManager
from Avian_Blasters.model.entity import Entity

class SpriteManagerProjectile(AbstractSpriteManager):
    def __init__(self):
        super().__init__(path = 'assets' + os.sep + 'sprites' + os.sep + 'Projectiles.png',
                         sprite_definitions = {
                            "PLAYER_NORMAL": {
                                'positions': [(28, 28, 12, 20)],
                                'size': (12, 20)
                            },
                            "ENEMY_NORMAL": {
                                'positions': [(83, 28, 12, 20)],
                                'size': (12, 20)
                            },
                            "SOUND_WAVE": {
                                'positions': [(136, 18, 60, 40)],
                                'size': (12, 8)
                            },
                            "LASER": {
                                'positions': [(228, 0, 12, 76)],
                                'size': (12, 76)
                            }
                         })
    def load_sprites(self) -> bool:
        return super().load_sprites()
    
    def get_sprite(self, projectile: Projectile, variant: int = 0) -> pygame.Surface:
        key = self._get_key(projectile)
        if not self._loaded or key not in self._sprites:
            return self._create_fallback_sprite(key)
        sprites = self._sprites[key]
        if variant >= len(sprites):
            variant = 0
        return sprites[variant]
    
    def get_sprite_size(self, key: str) -> Tuple[int, int]:
        return self._sprite_sizes.get(key)
    
    def is_loaded(self) -> bool:
        return super().is_loaded()
    
    def _create_fallback_sprite(self, key: str) -> pygame.Surface:
        
        colors = {
            "PLAYER_NORMAL": (0, 0, 255),
            "ENEMY_NORMAL": (128, 0, 128),
            "SOUND_WAVE": (128, 0, 128),
            "LASER": (255, 0, 0)
        }
        return super()._create_fallback_sprite(key, colors)
        

    def _get_key(self, projectile: Projectile)-> str:
        projectile_type = projectile.projectile_type
        if projectile_type == ProjectileType.NORMAL:
            if projectile.get_type == Entity.TypeArea.PLAYER_PROJECTILE:
                return "PLAYER_NORMAL"
            else:
                return "ENEMY_NORMAL"
        elif projectile_type == ProjectileType.SOUND_WAVE:
            return "SOUND_WAVE"
        elif projectile_type == ProjectileType.LASER:
            return "LASER"  
        else:
            return "PLAYER_NORMAL"
        