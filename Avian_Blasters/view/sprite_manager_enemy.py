import pygame
from typing import Dict, Tuple, Optional
from Avian_Blasters.view.sprite_manager import SpriteManager
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
import os

class SpriteManagerEnemy(SpriteManager):
    """SpriteManagerEnemy is a specialized sprite manager for enemy sprites (Bird and Bat)"""
    
    def __init__(self):
        self._bird_sprite_sheet: Optional[pygame.Surface] = None
        self._bat_sprite_sheet: Optional[pygame.Surface] = None
        self._bird_sprites: Dict[int, list[pygame.Surface]] = {}
        self._bat_sprites: Dict[int, list[pygame.Surface]] = {}
        self._sprite_sizes: Dict[str, Dict[int, Tuple[int, int]]] = {}
        self._loaded = False
        
        # Define sprite definitions for Bird (similar to player approach)
        self._bird_sprite_definitions = {
            3: {
                'positions': [(28, 27, 64, 40), (118, 27, 64, 40)],
                'size': (16, 10)
            },
            2: {
                'positions': [(24, 92, 64, 44), (116, 92, 64, 44)],
                'size': (16, 10)
            },
            1: {
                'positions': [(24, 160, 64, 44), (114, 160, 64, 44)],
                'size': (16, 10)
            },
        }
        
        # Define sprite definitions for Bat (similar to player approach)
        self._bat_sprite_definitions = {
            3: {
                'positions': [(24, 18, 64, 44), (114, 18, 64, 44)],
                'size': (16, 10)
            },
            2: {
                'positions': [(24, 92, 64, 44), (116, 92, 64, 44)],
                'size': (16, 10)
            },
            1: {
                'positions': [(24, 160, 64, 44), (114, 160, 64, 44)],
                'size': (16, 10)
            },
        }
        
        # Store paths for later loading
        self._bird_path = 'assets' + os.sep + 'sprites' + os.sep + 'Bird_V3.png'
        self._bat_path = 'assets' + os.sep + 'sprites' + os.sep + 'Bat_V3.png'
    
    def load_sprites(self) -> bool:
        """Load sprites from the Bird and Bat sprite sheet files"""
        try:
            # Load Bird sprite sheet
            self._bird_sprite_sheet = pygame.image.load(self._bird_path).convert_alpha()
            if self._bird_sprite_sheet is None:
                print("Failed to load Bird sprite sheet")
                return False
            
            # Load Bat sprite sheet
            self._bat_sprite_sheet = pygame.image.load(self._bat_path).convert_alpha()
            if self._bat_sprite_sheet is None:
                print("Failed to load Bat sprite sheet")
                return False
            
            # Extract Bird sprites for each variant
            for variant, definition in self._bird_sprite_definitions.items():
                sprites = []
                for i, pos in enumerate(definition['positions']):
                    x, y, width, height = pos
                    sprite_rect = pygame.Rect(x, y, width, height)
                    sprite = self._bird_sprite_sheet.subsurface(sprite_rect)
                    
                    # Convert sprite to proper format with alpha channel
                    sprite_copy = sprite.copy().convert_alpha()
                    sprites.append(sprite_copy)
                
                self._bird_sprites[variant] = sprites
            
            # Extract Bat sprites for each variant
            for variant, definition in self._bat_sprite_definitions.items():
                sprites = []
                for i, pos in enumerate(definition['positions']):
                    x, y, width, height = pos
                    sprite_rect = pygame.Rect(x, y, width, height)
                    sprite = self._bat_sprite_sheet.subsurface(sprite_rect)
                    
                    # Convert sprite to proper format with alpha channel
                    sprite_copy = sprite.copy().convert_alpha()
                    sprites.append(sprite_copy)
                
                self._bat_sprites[variant] = sprites
            
            # Store sprite sizes
            self._sprite_sizes['bird'] = {variant: definition['size'] for variant, definition in self._bird_sprite_definitions.items()}
            self._sprite_sizes['bat'] = {variant: definition['size'] for variant, definition in self._bat_sprite_definitions.items()}
            
            self._loaded = True
            return True
            
        except Exception as e:
            print(f"Failed to load enemy sprite sheets: {e}")
            return False
    
    def get_sprite(self, enemy: Enemy, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified enemy and variant"""
        if not self._loaded:
            return self._create_fallback_sprite(enemy)
        
        # Determine enemy type and get appropriate health/variant
        if isinstance(enemy, Bird):
            health = enemy.get_health_handler().current_health
            sprites = self._bird_sprites.get(health, [])
            enemy_type = 'bird'
        elif isinstance(enemy, Bat):
            health = enemy.get_health_handler().current_health
            sprites = self._bat_sprites.get(health, [])
            enemy_type = 'bat'
        else:
            # Fallback for unknown enemy types
            return self._create_fallback_sprite(enemy)
        
        if not sprites:
            return self._create_fallback_sprite(enemy)
        
        # Use variant to select from available sprites
        if variant >= len(sprites):
            variant = 0  # Use first sprite as fallback
        
        return sprites[variant]
    
    def get_sprite_size(self, enemy: Enemy) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified enemy"""
        if isinstance(enemy, Bird):
            health = enemy.get_health_handler().current_health
            return self._sprite_sizes.get('bird', {}).get(health, (16, 10))
        elif isinstance(enemy, Bat):
            health = enemy.get_health_handler().current_health
            return self._sprite_sizes.get('bat', {}).get(health, (16, 10))
        else:
            return (16, 10)  # Default size (matches player size)
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, enemy: Enemy) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        size = self.get_sprite_size(enemy)
        surface = pygame.Surface(size)
        
        # Use different colors for different enemy types and health
        if isinstance(enemy, Bird):
            health = enemy.get_health_handler().current_health
            colors = {
                3: (0, 255, 0),      # Green
                2: (255, 255, 0),    # Yellow  
                1: (255, 0, 0)       # Red
            }
            color = colors.get(health, (0, 255, 0))
        elif isinstance(enemy, Bat):
            health = enemy.get_health_handler().current_health
            colors = {
                3: (0, 0, 255),      # Blue
                2: (255, 0, 255),    # Magenta
                1: (128, 0, 128)     # Purple
            }
            color = colors.get(health, (0, 0, 255))
        else:
            color = (255, 255, 255)  # White for unknown
        
        surface.fill(color)
        return surface
