import pygame
from typing import Dict, Tuple, Optional
from Avian_Blasters.view.sprite_manager import SpriteManager
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.projectile.projectile import ProjectileType

class SpriteManagerImpl(SpriteManager):
    """SpriteManagerImpl is a pygame implementation of SpriteManager for projectiles and powerups"""
    
    def __init__(self):
        self._sprite_sheet: Optional[pygame.Surface] = None
        self._sprites: Dict[Entity.TypeArea, list[pygame.Surface]] = {}
        self._sprite_sizes: Dict[Entity.TypeArea, Tuple[int, int]] = {}
        self._loaded = False
        
        # Define sprite grid positions and sizes for projectiles and powerups only
        # Player and enemy sprites are handled by specialized sprite managers
        self._sprite_definitions = {
            Entity.TypeArea.PLAYER_PROJECTILE: {
                'positions': [(224, 292, 12, 20)],  # Player projectiles
                'size': (12, 20)
            },
            Entity.TypeArea.ENEMY_PROJECTILE: {
                'positions': [(216, 32, 12, 20), (520, 30, 63, 44)],  # [0] Bird projectiles, [1] Bat projectiles
                'size': (12, 20)
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
    
    def get_sprite(self, entity_type: Entity.TypeArea, variant: int = 0, projectile_type: Optional[ProjectileType] = None) -> pygame.Surface:
        """Get a sprite surface for the specified entity type and variant
        
        For enemy projectiles, projectile_type determines which sprite to use:
        - ProjectileType.NORMAL (bird projectile) -> variant 0
        - ProjectileType.SOUND_WAVE (bat projectile) -> variant 1
        """
        if not self._loaded or entity_type not in self._sprites:
            # Return a fallback colored rectangle if sprites aren't loaded
            return self._create_fallback_sprite(entity_type, projectile_type)
        
        sprites = self._sprites[entity_type]
        
        # Handle enemy projectiles based on projectile type
        if entity_type == Entity.TypeArea.ENEMY_PROJECTILE and projectile_type is not None:
            if projectile_type == ProjectileType.NORMAL:  # Bird projectile
                variant = 0
            elif projectile_type == ProjectileType.SOUND_WAVE:  # Bat projectile
                variant = 1
        
        if variant >= len(sprites):
            variant = 0  # Use first sprite as fallback
        
        return sprites[variant]
    
    def get_sprite_size(self, entity_type: Entity.TypeArea) -> Tuple[int, int]:
        """Get the size (width, height) of sprites for the specified entity type"""
        if entity_type in self._sprite_sizes:
            return self._sprite_sizes[entity_type]
        # Return default size for unsupported entity types (shouldn't happen in normal flow)
        return (16, 10)
    
    def is_loaded(self) -> bool:
        """Check if sprites have been successfully loaded"""
        return self._loaded
    
    def _create_fallback_sprite(self, entity_type: Entity.TypeArea, projectile_type: Optional[ProjectileType] = None) -> pygame.Surface:
        """Create a simple colored rectangle as fallback when sprites aren't loaded"""
        width, height = self.get_sprite_size(entity_type)
        surface = pygame.Surface((width, height))
        
        # Use colors only for projectiles and powerups (player/enemy handled by specialized managers)
        if entity_type == Entity.TypeArea.ENEMY_PROJECTILE and projectile_type is not None:
            # Different colors for different enemy projectile types
            if projectile_type == ProjectileType.NORMAL:  # Bird projectile
                color = (255, 100, 100)  # Light red
            elif projectile_type == ProjectileType.SOUND_WAVE:  # Bat projectile
                color = (200, 100, 255)  # Light purple
            else:
                color = (128, 0, 128)  # Default purple
        else:
            colors = {
                Entity.TypeArea.PLAYER_PROJECTILE: (0, 0, 255),  # Blue
                Entity.TypeArea.ENEMY_PROJECTILE: (128, 0, 128), # Purple (default)
                Entity.TypeArea.POWERUP: (255, 255, 0)    # Yellow
            }
            color = colors.get(entity_type, (255, 255, 255))
        
        surface.fill(color)
        return surface
