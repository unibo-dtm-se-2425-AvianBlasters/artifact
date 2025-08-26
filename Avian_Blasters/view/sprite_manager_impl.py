import pygame
from typing import Dict, Tuple, Optional
from Avian_Blasters.view.sprite_manager import SpriteManager
from Avian_Blasters.model.entity import Entity

class SpriteManagerImpl(SpriteManager):
    """SpriteManagerImpl is a pygame implementation of SpriteManager"""
    
    def __init__(self):
        self._sprite_sheet: Optional[pygame.Surface] = None
        self._sprites: Dict[Entity.TypeArea, list[pygame.Surface]] = {}
        self._sprite_sizes: Dict[Entity.TypeArea, Tuple[int, int]] = {}
        self._loaded = False
        
        # Define sprite grid positions and sizes for each entity type
        # Based on actual sprite sheet analysis - sprites found at (40-90, 40-70)
        self._sprite_definitions = {
            Entity.TypeArea.PLAYER: {
                'positions': [(24, 280, 64, 40), (124, 280, 64, 40)],  # Player sprites where we found green pixels
                'size': (16, 10)
            },
            Entity.TypeArea.ENEMY: {
                'positions': [(26, 24, 64, 44), (120, 24, 64, 44), (80, 40, 64, 40),  # birds
                             (26, 304, 64, 44), (60, 60, 60, 40), (80, 60, 60, 40)],   # bats
                'size': (16, 10)
            },
            Entity.TypeArea.PLAYER_PROJECTILE: {
                'positions': [(224, 292, 12, 20)],  # Projectiles
                'size': (12, 20)
            },
            Entity.TypeArea.ENEMY_PROJECTILE: {
                'positions': [(213, 33, 12, 20), (100, 70, 4, 8)],  # Enemy projectiles
                'size': (4, 8)
            },
            Entity.TypeArea.POWERUP: {
                'positions': [(143, 28, 12, 40), (120, 40, 16, 16), (120, 60, 16, 16)],  # Power-ups
                'size': (16, 16)
            }
        }
    
    def load_sprites(self, sprite_sheet_path: str) -> bool:
        """Load sprites from the sprite sheet file"""
        try:
            # Load and convert sprite sheet for optimal performance
            self._sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
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
    
    def get_sprite(self, entity_type: Entity.TypeArea, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified entity type and variant"""
        if not self._loaded or entity_type not in self._sprites:
            # Return a fallback colored rectangle if sprites aren't loaded
            return self._create_fallback_sprite(entity_type)
        
        sprites = self._sprites[entity_type]
        if variant >= len(sprites):
            variant = 0  # Use first sprite as fallback
        
        return sprites[variant]
    
    def get_sprite_size(self, entity_type: Entity.TypeArea) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified entity type"""
        if entity_type in self._sprite_sizes:
            return self._sprite_sizes[entity_type]
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, entity_type: Entity.TypeArea) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        width, height = self.get_sprite_size(entity_type)
        surface = pygame.Surface((width, height))
        
        # Use the same colors as before for fallback
        colors = {
            Entity.TypeArea.PLAYER: (0, 255, 0),      # Green
            Entity.TypeArea.ENEMY: (255, 0, 0),       # Red
            Entity.TypeArea.PLAYER_PROJECTILE: (0, 0, 255),  # Blue
            Entity.TypeArea.ENEMY_PROJECTILE: (128, 0, 128), # Purple
            Entity.TypeArea.POWERUP: (255, 255, 0)    # Yellow
        }
        
        color = colors.get(entity_type, (255, 255, 255))
        surface.fill(color)
        return surface
