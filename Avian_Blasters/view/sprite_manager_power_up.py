from typing import Tuple
from typing import Dict, Optional
import pygame
from Avian_Blasters.model.item.power_up.power_up import PowerUp, PowerUpType
from Avian_Blasters.view.sprite_manager import SpriteManager


class SpriteManagerPowerUp(SpriteManager):
    def __init__(self):
        self._sprite_sheet: Optional[pygame.Surface] = None
        self._sprites: Dict[PowerUpType, list[pygame.Surface]] = {}
        self._sprite_sizes: Dict[PowerUpType, Tuple[int, int]] = {}
        self._loaded = False
        self._path = "assets/sprites/Power-Ups_V3.png"

        
        # Define sprite grid positions and sizes
        # Based on actual sprite sheet analysis - sprites found at (40-90, 40-70)
        self._sprite_definitions = {
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
    
    def get_sprite(self, power_up: PowerUp, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified power-up and variant"""
        power_up_type = power_up.power_up_type
        if not self._loaded or power_up_type not in self._sprites:
            # Return a fallback colored rectangle if sprites aren't loaded
            return self._create_fallback_sprite(power_up_type)
        
        sprites = self._sprites[power_up_type]
        if variant >= len(sprites):
            variant = 0  # Use first sprite as fallback
        
        return sprites[variant]
    
    def get_sprite_size(self, power_up_type: PowerUpType) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified type"""
        if power_up_type in self._sprite_sizes:
            return self._sprite_sizes[power_up_type]
        else:
            return (32, 32)
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, power_up_type: PowerUpType) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        width, height = self.get_sprite_size(power_up_type)
        surface = pygame.Surface((width, height))
        
        # Use the same colors as before for fallback
        colors = {
            PowerUpType.INVULNERABILITY: (0, 0, 255),      
            PowerUpType.DOUBLE_FIRE: (255, 165, 0),        
            PowerUpType.LASER: (0, 255, 0),                
            PowerUpType.HEALTH_RECOVERY: (255, 0, 0) 
        }
    
        color = colors.get(power_up_type, (255, 255, 255))
        surface.fill(color)
        return surface
        