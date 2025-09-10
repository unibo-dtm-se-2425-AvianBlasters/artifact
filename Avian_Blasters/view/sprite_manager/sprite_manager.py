import pygame
from typing import Dict, Tuple, Any
from Avian_Blasters.model.entity import Entity

class SpriteManager:
    """SpriteManager defines the interface for loading and managing game sprites"""
    
    def load_sprites(self) -> bool:
        """Load sprites from the sprite sheet file"""
        ...
    
    def get_sprite(self, index: Any, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified entity type and variant"""
        ...
    
    def get_sprite_size(self, index : Any) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified entity type"""
        ...
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        ...
