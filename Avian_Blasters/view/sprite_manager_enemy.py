import pygame
from typing import Dict, Tuple, Optional
from Avian_Blasters.view.abstract_sprite_manager import AbstractSpriteManager
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
import os

class SpriteManagerEnemy(AbstractSpriteManager):
    
    def __init__(self):
        super().__init__(path='assets' + os.sep + 'sprites' + os.sep + 'Bird_V3.png',
                       sprite_definitions={
                           3: {  # Full health - Green bird
                               'positions': [(25, 25, 64, 42), (117, 25, 64, 42)],
                               'size': (16, 10)
                           },
                           2: {  # Medium health - Yellow bird  
                               'positions': [(25, 97, 64, 42), (117, 97, 64, 42)],
                               'size': (16, 10)
                           },
                           1: {  # Low health - Red bird
                               'positions': [(25, 165, 64, 42), (117, 165, 64, 42)],
                               'size': (16, 10)
                           }
                       })
        
        self._bat_sprite_sheet: Optional[pygame.Surface] = None
        self._bat_sprites_loaded = False
        self._bat_sprite_definitions = {
            3: {  # Full health - Green bat
                'positions': [(22, 24, 70, 44), (112, 24, 70, 44)],
                'size': (16, 10)
            },
            2: {  # Medium health - Yellow bat  
                'positions': [(22, 92, 70, 44), (112, 92, 70, 44)],
                'size': (16, 10)
            },
            1: {  # Low health - Red bat
                'positions': [(22, 164, 70, 44), (112, 164, 70, 44)],
                'size': (16, 10)
            }
        }
        self._bat_sprites_by_health: Dict[int, list[pygame.Surface]] = {}
    
    def load_sprites(self) -> bool:
        bird_loaded = super().load_sprites()
        bat_loaded = self._load_bat_sprites()
        
        return bird_loaded and bat_loaded
    
    def _load_bat_sprites(self) -> bool:
        try:
            bat_path = 'assets' + os.sep + 'sprites' + os.sep + 'Bat_V3.png'
            self._bat_sprite_sheet = pygame.image.load(bat_path).convert_alpha()
            if self._bat_sprite_sheet is None:
                print("Failed to load Bat sprite sheet")
                return False

            for health, definition in self._bat_sprite_definitions.items():
                sprites_for_health = []
                for pos in definition['positions']:
                    x, y, width, height = pos
                    sprite_rect = pygame.Rect(x, y, width, height)
                    sprite = self._bat_sprite_sheet.subsurface(sprite_rect)
                    sprite_copy = sprite.copy().convert_alpha()
                    sprites_for_health.append(sprite_copy)
                self._bat_sprites_by_health[health] = sprites_for_health
            
            self._bat_sprites_loaded = True
            return True
            
        except Exception as e:
            print(f"Failed to load bat sprite sheet: {e}")
            return False
    
    def get_sprite(self, entity_type: Entity.TypeArea, variant: int = 0) -> pygame.Surface:
        if not self.is_loaded():
            return self._create_fallback_sprite_for_bird(3)
        return super().get_sprite(3, variant)
    
    def get_sprite_for_enemy(self, enemy: Enemy, variant: int = 0) -> pygame.Surface:

        if isinstance(enemy, Bird):
            health = enemy.get_health
            if not self.is_loaded():
                return self._create_fallback_sprite_for_bird(health)
            return super().get_sprite(health, variant)
        
        elif isinstance(enemy, Bat):
            health = enemy.get_health
            if not self._bat_sprites_loaded or health not in self._bat_sprites_by_health:
                return self._create_fallback_sprite_for_bat(health)
            
            sprites_for_health = self._bat_sprites_by_health[health]
            if not sprites_for_health:
                return self._create_fallback_sprite_for_bat(health)
            sprite_variant = variant % len(sprites_for_health)
            return sprites_for_health[sprite_variant]
        
        else:
            return self._create_fallback_sprite_for_bird(3)
    
    def get_sprite_size(self, entity_type: Entity.TypeArea) -> Tuple[int, int]:
        return (16, 10)  # Standard enemy sprite size
    
    def _create_fallback_sprite_for_bird(self, health: int) -> pygame.Surface:
        colours = {
            3: (0, 255, 0),
            2: (255, 255, 0),
            1: (255, 0, 0),
        }
        return super()._create_fallback_sprite(health, colours)
    
    def _create_fallback_sprite_for_bat(self, health: int = 3) -> pygame.Surface:
        surface = pygame.Surface((16, 10))
        
        if health == 3:
            color = (0, 200, 0)
        elif health == 2:
            color = (200, 200, 0)
        elif health == 1:
            color = (200, 0, 0)
        else:
            color = (100, 0, 100)
        
        surface.fill(color)
        return surface
