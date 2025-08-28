import pygame
from typing import Dict, Tuple, Optional
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.view.sprite_manager import SpriteManager
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.player import Player

class SpriteManagerProjectile(SpriteManager):
    """SpriteManagerImpl is a pygame implementation of SpriteManager"""
    
    def __init__(self):
        self._sprite_sheet: Optional[pygame.Surface] = None
        self._sprites: Dict[str, list[pygame.Surface]] = {}
        self._sprite_sizes: Dict[str, Tuple[int, int]] = {}
        self._loaded = False
        self._path = "assets/sprites/Projectiles_V3.png"

        
        # Define sprite grid positions and sizes
        # Based on actual sprite sheet analysis - sprites found at (40-90, 40-70)
        self._sprite_definitions = {
            "PLAYER_NORMAL": {
                'positions': [(28, 28, 12, 20)],
                'size': (6, 10)
            },
            "ENEMY_NORMAL": {
                'positions': [(83, 28, 12, 20)],
                'size': (6, 10)
            },
            "SOUND_WAVE": {
                'positions': [(136, 18, 60, 40)],
                'size': (12, 8)
            },
            "LASER": {
                'positions': [(228, 0, 12, 76)],
                'size': (12, 76)
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
    
    def get_sprite(self, projectile: Projectile, variant: int = 0) -> pygame.Surface:
        """Get a sprite surface for the specified projectile and variant"""
        key = self._get_key(projectile)
        if not self._loaded or key not in self._sprites:
            # Return a fallback colored rectangle if sprites aren't loaded
            return self._create_fallback_sprite(key)
        
        sprites = self._sprites[key]
        if variant >= len(sprites):
            variant = 0  # Use first sprite as fallback
        
        return sprites[variant]
    
    def get_sprite_size(self, key: str) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified key"""
        if key in self._sprite_sizes:
            return self._sprite_sizes[key]
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, key: str) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        width, height = self.get_sprite_size(key)
        surface = pygame.Surface((width, height))
        
        # Use the same colors as before for fallback
        colors = {
            "PLAYER_NORMAL": (0, 0, 255),
            "ENEMY_NORMAL": (128, 0, 128),
            "SOUND_WAVE": (128, 0, 128),
            "LASER": (255, 0, 0)
        }
    
        color = colors.get(key, (255, 255, 255))
        surface.fill(color)
        return surface
        

    def _get_key(self, projectile: Projectile)-> str:
        projectile_type = projectile.get_projectile_type()
        if projectile_type == ProjectileType.PLAYER_NORMAL:
            if projectile.get_type() == Entity.TypeArea.PLAYER_PROJECTILE:
                return "PLAYER_NORMAL"
            else:
                return "ENEMY_NORMAL"
        elif projectile_type == ProjectileType.SOUND_WAVE:
            return "SOUND_WAVE"
        elif projectile_type == ProjectileType.LASER:
            return "LASER"  
        else:
            return "PLAYER_NORMAL"