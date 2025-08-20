import pygame
from typing import Dict, Tuple
from Avian_Blasters.model.entity import Entity

class SpriteManager:
    """SpriteManager defines the interface for loading and managing game sprites"""
    
    def load_sprites(self, sprite_sheet_path: str) -> bool:
        """Load sprites from the sprite sheet file"""
        ...
    
    def get_sprite(self, entity_type: Entity.TypeArea, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified entity type and variant"""
        ...
    
    def get_sprite_size(self, entity_type: Entity.TypeArea) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified entity type"""
        ...
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        ...
