import pygame
from typing import List, Dict
from Avian_Blasters.view.game_view import GameView
from Avian_Blasters.view.sprite_manager import SpriteManager
from Avian_Blasters.view.sprite_manager_impl import SpriteManagerImpl
from Avian_Blasters.view.sprite_manager_player import SpriteManagerPlayer
from Avian_Blasters.view.ui_renderer import UIRenderer
from Avian_Blasters.view.ui_renderer_impl import UIRendererImpl
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.world import World, WORLD_WIDTH, WORLD_HEIGHT
from Avian_Blasters.model.entity import Entity

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class GameViewImpl(GameView):
    """GameViewImpl is a pygame implementation of GameView"""
    
    def __init__(self):
        self._screen = None
        self._screen_width = 0
        self._screen_height = 0
        self._scale_x = 1.0
        self._scale_y = 1.0
        self._sprite_manager: SpriteManager = SpriteManagerImpl()
        self._sprite_manager_player = SpriteManagerPlayer()
        self._ui_renderer: UIRenderer = UIRendererImpl()
        self._cooldown_animation = 0
    
    def initialize(self, width: int, height: int, title: str) -> bool:
        """Initialize the pygame display and return success status"""
        try:
            pygame.init()
            self._screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption(title)
            self._screen_width = width
            self._screen_height = height
            
            # Calculate scaling factors from world coordinates to screen coordinates
            self._scale_x = width / WORLD_WIDTH
            self._scale_y = height / WORLD_HEIGHT
            
            # Load sprites
            sprite_path = "assets/sprites.png"
            if not self._sprite_manager.load_sprites(sprite_path):
                print(f"Warning: Failed to load sprites from {sprite_path}, using fallback rectangles")
            self._sprite_manager_player.load_sprites()
            # Initialize UI renderer
            if not self._ui_renderer.initialize():
                print("Warning: Failed to initialize UI renderer")
            
            return True
        except Exception as e:
            print(f"Failed to initialize pygame: {e}")
            return False
    
    def render_world(self, world: World) -> None:
        """Render the complete game world including all entities"""
        self.clear_screen()
        
        # Render all entities
        entities = world.get_all_entities()
        for entity in entities:
            if self._cooldown_animation < 30 or entity.get_type not in [Entity.TypeArea.PLAYER, Entity.TypeArea.ENEMY]:
                self.render_entity(entity)
            elif self._cooldown_animation < 60:
                self.render_entity_with_variant(entity, 1)
                if self._cooldown_animation == 59:
                    self._cooldown_animation = 0
        
        # Render UI elements
        players = world.get_players()
        if players:
            player = players[0]
            # Render score in top-left corner
            self._ui_renderer.render_score(self._screen, player, 10, 10)
            # Render health below score
            self._ui_renderer.render_health(self._screen, player, 10, 30)
        
        self._cooldown_animation += 1
    
    def render_entity(self, entity: Entity) -> None:
        """Render a single entity to the screen"""
        if self._screen is None:
            return
            
        area = entity.get_area()
        
        # Convert world coordinates to screen coordinates
        screen_x = int(area.get_position_x * self._scale_x)
        screen_y = int(area.get_position_y * self._scale_y)
        

        
        # Get sprite for this entity with proper error handling
        try:
            sprite = self._sprite_manager.get_sprite(entity.get_type)

            if isinstance(entity, Player):
                sprite = self._sprite_manager_player.get_sprite(entity)
            
            # Scale sprite to match world size
            sprite_width = int(area.width * self._scale_x)
            sprite_height = int(area.height * self._scale_y)
            
            # Scale the sprite if needed
            if sprite.get_size() != (sprite_width, sprite_height):
                sprite = pygame.transform.scale(sprite, (sprite_width, sprite_height))
            
            # Calculate position (centered)
            sprite_x = screen_x - sprite_width // 2
            sprite_y = screen_y - sprite_height // 2
            
            # Ensure sprite has proper surface format
            if sprite.get_flags() & pygame.SRCALPHA:
                # Sprite has alpha channel - blit directly
                self._screen.blit(sprite, (sprite_x, sprite_y))
            else:
                # Convert sprite to match display format
                converted_sprite = sprite.convert(self._screen)
                self._screen.blit(converted_sprite, (sprite_x, sprite_y))
            

            
        except Exception as e:
            # Fallback to colored rectangles if sprite rendering fails
            sprite_width = int(area.width * self._scale_x)
            sprite_height = int(area.height * self._scale_y)
            sprite_x = screen_x - sprite_width // 2
            sprite_y = screen_y - sprite_height // 2
            
            # Choose fallback color based on entity type
            if entity.get_type == Entity.TypeArea.PLAYER:
                color = (0, 255, 0)  # Green for player
            elif entity.get_type == Entity.TypeArea.ENEMY:
                color = (255, 0, 0)  # Red for enemies
            else:
                color = (255, 255, 0)  # Yellow for other entities
            
            # Draw colored rectangle as fallback
            rect = pygame.Rect(sprite_x, sprite_y, sprite_width, sprite_height)
            pygame.draw.rect(self._screen, color, rect)
    
    def render_entity_with_variant(self, entity: Entity, variant: int) -> None:
        """Render a single entity with a specific sprite variant"""
        if self._screen is None:
            return
            
        area = entity.get_area()
        
        # Convert world coordinates to screen coordinates
        screen_x = int(area.get_position_x * self._scale_x)
        screen_y = int(area.get_position_y * self._scale_y)
        
        # Get sprite for this entity with specific variant
        sprite = self._sprite_manager.get_sprite(entity.get_type, variant)

        if isinstance(entity, Player):
            sprite = self._sprite_manager_player.get_sprite(entity, variant)

        
        # Scale sprite to match world size
        sprite_width = int(area.width * self._scale_x)
        sprite_height = int(area.height * self._scale_y)
        
        # Scale the sprite if needed
        if sprite.get_size() != (sprite_width, sprite_height):
            sprite = pygame.transform.scale(sprite, (sprite_width, sprite_height))
        
        # Calculate position (centered)
        sprite_x = screen_x - sprite_width // 2
        sprite_y = screen_y - sprite_height // 2
        
        # Blit the sprite to the screen
        self._screen.blit(sprite, (sprite_x, sprite_y))
    
    def clear_screen(self) -> None:
        """Clear the screen with background color"""
        if self._screen is not None:
            self._screen.fill(BLACK)
    
    def update_display(self) -> None:
        """Update the pygame display"""
        pygame.display.flip()
    
    def get_screen_dimensions(self) -> tuple[int, int]:
        """Get the current screen width and height"""
        return (self._screen_width, self._screen_height)
    
    def cleanup(self) -> None:
        """Cleanup pygame resources"""
        pygame.quit()
