import pygame
from typing import Dict, Tuple, Optional, Any
from Avian_Blasters.view.sprite_manager import SpriteManager
from Avian_Blasters.model.entity import Entity

class AbstractSpriteManager(SpriteManager):
    """AbstractSpriteManager is a partial implementation
    of SpriteManager covering functionalities common to all
    SpriteManager implementations"""
    
    def __init__(self, path : str, sprite_definitions : Dict[Any, dict[str, Any]]):
        self._sprite_sheet: Optional[pygame.Surface] = None
        self._sprites: Dict[Any, list[pygame.Surface]] = {}
        self._sprite_sizes: Dict[Any, Tuple[int, int]] = {}
        self._loaded = False
        self._path = path
        self._sprite_definitions = sprite_definitions
    
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
    
    def get_sprite(self, index : Any, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified entity type and variant"""
        if not self._loaded or index not in self._sprites:
            # Return a fallback colored rectangle if sprites aren't loaded
            return self._create_fallback_sprite(index)
        
        sprites = self._sprites[index]
        if variant >= len(sprites):
            variant = 0  # Use first sprite as fallback
        
        return sprites[variant]
    
    def get_sprite_size(self, index : Any) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified entity type"""
        if index in self._sprite_sizes:
            return self._sprite_sizes[index]
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, index : Any, colours : dict[Any, tuple[int, int, int]]) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        width, height = self.get_sprite_size(index)
        surface = pygame.Surface((width, height))
        colour = colours.get(index, (255, 255, 255))
        surface.fill(colour)
        return surface
