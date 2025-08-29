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
        self._bird_sprites: list[pygame.Surface] = []
        self._bat_sprites: list[pygame.Surface] = []
        self._sprite_size: Tuple[int, int] = (16, 10)  # Default size
        self._loaded = False
        
        # Define sprite positions for Bird_V3.png
        # Based on typical sprite sheet layout - adjust coordinates as needed
        self._bird_sprite_positions = [
            (24, 18, 64, 40),   # Bird variant 1
            (121, 18, 64, 40),  # Bird variant 2
        ]
        
        # Define sprite positions for Bat_V3.png
        # Based on typical sprite sheet layout - adjust coordinates as needed
        self._bat_sprite_positions = [
            (24, 18, 64, 40),   # Bat variant 1
            (121, 18, 64, 40),  # Bat variant 2
        ]
    
    def load_sprites(self, sprite_sheet_path: str = None) -> bool:
        """Load sprites from the Bird and Bat sprite sheet files"""
        try:
            # Load Bird sprite sheet
            bird_path = 'assets' + os.sep + 'sprites' + os.sep + 'Bird_V3.png'
            self._bird_sprite_sheet = pygame.image.load(bird_path).convert_alpha()
            if self._bird_sprite_sheet is None:
                print("Failed to load Bird sprite sheet")
                return False
            
            # Load Bat sprite sheet
            bat_path = 'assets' + os.sep + 'sprites' + os.sep + 'Bat_V3.png'
            self._bat_sprite_sheet = pygame.image.load(bat_path).convert_alpha()
            if self._bat_sprite_sheet is None:
                print("Failed to load Bat sprite sheet")
                return False
            
            # Extract Bird sprites
            self._bird_sprites = []
            for pos in self._bird_sprite_positions:
                x, y, width, height = pos
                sprite_rect = pygame.Rect(x, y, width, height)
                sprite = self._bird_sprite_sheet.subsurface(sprite_rect)
                sprite_copy = sprite.copy().convert_alpha()
                self._bird_sprites.append(sprite_copy)
            
            # Extract Bat sprites
            self._bat_sprites = []
            for pos in self._bat_sprite_positions:
                x, y, width, height = pos
                sprite_rect = pygame.Rect(x, y, width, height)
                sprite = self._bat_sprite_sheet.subsurface(sprite_rect)
                sprite_copy = sprite.copy().convert_alpha()
                self._bat_sprites.append(sprite_copy)
            
            self._loaded = True
            return True
            
        except Exception as e:
            print(f"Failed to load enemy sprite sheets: {e}")
            return False
    
    def get_sprite(self, entity_type: Entity.TypeArea, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified entity type and variant"""
        if not self._loaded:
            return self._create_fallback_sprite(entity_type)
        
        # For enemies, we need to determine if it's a Bird or Bat
        # Since we don't have the actual enemy instance here, we'll use variant to alternate
        if variant % 2 == 0:  # Even variants use Bird sprites
            sprites = self._bird_sprites
        else:  # Odd variants use Bat sprites
            sprites = self._bat_sprites
        
        if not sprites:
            return self._create_fallback_sprite(entity_type)
        
        sprite_variant = (variant // 2) % len(sprites)  # Get sprite variant within the type
        return sprites[sprite_variant]
    
    def get_sprite_for_enemy(self, enemy: Enemy, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for a specific enemy instance"""
        if not self._loaded:
            return self._create_fallback_sprite(Entity.TypeArea.ENEMY)
        
        # Determine sprite based on enemy type
        if isinstance(enemy, Bird):
            sprites = self._bird_sprites
        elif isinstance(enemy, Bat):
            sprites = self._bat_sprites
        else:
            # Fallback for unknown enemy types
            sprites = self._bird_sprites if variant % 2 == 0 else self._bat_sprites
        
        if not sprites:
            return self._create_fallback_sprite(Entity.TypeArea.ENEMY)
        
        sprite_variant = variant % len(sprites)
        return sprites[sprite_variant]
    
    def get_sprite_size(self, entity_type: Entity.TypeArea) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified entity type"""
        return self._sprite_size
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, entity_type: Entity.TypeArea) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        surface = pygame.Surface(self._sprite_size)
        
        # Use different colors for different enemy types
        colors = {
            Entity.TypeArea.ENEMY: (255, 0, 0),  # Red for enemies
        }
        
        color = colors.get(entity_type, (255, 255, 255))
        surface.fill(color)
        return surface
