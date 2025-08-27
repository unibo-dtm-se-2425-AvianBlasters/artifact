import pygame
from typing import Dict, Tuple, Optional
from Avian_Blasters.view.sprite_manager import SpriteManager
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.player import Player

class SpriteManagerPlayer(SpriteManager):
    """SpriteManagerImpl is a pygame implementation of SpriteManager"""
    
    def __init__(self):
        self._sprite_sheet: Optional[pygame.Surface] = None
        self._sprites: Dict[int, list[pygame.Surface]] = {}
        self._sprite_sizes: Dict[int, Tuple[int, int]] = {}
        self._loaded = False
        self._path = "assets/sprites/Car_V3.png"

        
        # Define sprite grid positions and sizes
        # Based on actual sprite sheet analysis - sprites found at (40-90, 40-70)
        self._sprite_definitions = {
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
        }
    
    def load_sprites(self) -> bool:
        """Load sprites from the sprite sheet file"""
        try:
            # Load and convert sprite sheet for optimal performance
            self._sprite_sheet = pygame.image.load(self._path).convert_alpha()
            if self._sprite_sheet is None:
                return False
            

            
            # Extract individual sprites for each entity type
            for entity_type, definition in self._sprite_definitions.items():
                sprites = []
                for i, pos in enumerate(definition['positions']):
                    x, y, width, height = pos
                    sprite_rect = pygame.Rect(x, y, width, height)
                    sprite = self._sprite_sheet.subsurface(sprite_rect)
                    

                    
                    # Convert sprite to proper format with alpha channel
                    sprite_copy = sprite.copy().convert_alpha()
                    
                    # Use the actual extracted sprites now
                    sprites.append(sprite_copy)
                
                self._sprites[entity_type] = sprites
                self._sprite_sizes[entity_type] = definition['size']
            
            self._loaded = True
            return True
            
        except Exception as e:
            print(f"Failed to load sprite sheet: {e}")
            return False
    
    def get_sprite(self, player : Player, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified player and variant"""
        health = player.get_health_handler().current_health
        if not self._loaded or health not in self._sprites:
            # Return a fallback colored rectangle if sprites aren't loaded
            return self._create_fallback_sprite(health)
        
        sprites = self._sprites[health]
        if variant >= len(sprites):
            variant = 0  # Use first sprite as fallback
        
        return sprites[variant]
    
    def get_sprite_size(self, health : int) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified health"""
        if health in self._sprite_sizes:
            return self._sprite_sizes[health]
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, current_health : int) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        width, height = self.get_sprite_size(current_health)
        surface = pygame.Surface((width, height))
        
        # Use the same colors as before for fallback
        colors = {
            3: (0, 255, 0),      # Green
            2: (255, 255, 0),    # Yellow
            1: (255, 0, 0)       # Red
        }
        
        color = colors.get(current_health, (255, 255, 255))
        surface.fill(color)
        return surface
