import pygame
from typing import Dict
from Avian_Blasters.model.item.power_up.power_up import PowerUp
from Avian_Blasters.model.item.projectile.projectile import Projectile
from Avian_Blasters.view.game_view import GameView
from Avian_Blasters.view.sprite_manager.sprite_manager import SpriteManager
from Avian_Blasters.view.sprite_manager.default_sprite_manager import DefaultSpriteManager
from Avian_Blasters.view.sprite_manager.sprite_manager_player import SpriteManagerPlayer
from Avian_Blasters.view.sprite_manager.sprite_manager_enemy import SpriteManagerEnemy
from Avian_Blasters.view.sprite_manager.sprite_manager_power_up import SpriteManagerPowerUp
from Avian_Blasters.view.sprite_manager.sprite_manager_projectile import SpriteManagerProjectile
from Avian_Blasters.view.ui_renderer import UIRenderer
from Avian_Blasters.view.ui_renderer_impl import UIRendererImpl
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.world import World, WORLD_WIDTH, WORLD_HEIGHT
from Avian_Blasters.model.entity import Entity

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRAPH_REFRESH = 60

class GameViewImpl(GameView):
    """GameViewImpl is a pygame implementation of GameView"""
    
    def __init__(self):
        self._screen = None
        self._screen_width = 0
        self._screen_height = 0
        self._scale_x = 1.0
        self._scale_y = 1.0
        self._sprite_managers: Dict[Entity.TypeArea, SpriteManager] = {
            Entity.TypeArea.PLAYER: SpriteManagerPlayer(),
            Entity.TypeArea.ENEMY: SpriteManagerEnemy(),
            Entity.TypeArea.PLAYER_PROJECTILE: SpriteManagerProjectile(),
            Entity.TypeArea.ENEMY_PROJECTILE: SpriteManagerProjectile(),
            Entity.TypeArea.POWERUP: SpriteManagerPowerUp()
        }
        self._default_sprite_manager = DefaultSpriteManager()
        self._ui_renderer: UIRenderer = UIRendererImpl()
        self._cooldown_animation = 0
    
    def initialize(self, width: int, height: int, title: str) -> bool:
        try:
            self._screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption(title)
            self._screen_width = width
            self._screen_height = height
            
            # Calculate scaling factors from world coordinates to screen coordinates
            self._scale_x = width / WORLD_WIDTH
            self._scale_y = height / WORLD_HEIGHT
            
            # Load sprites
            for manager in self._sprite_managers.values():
                if not manager.load_sprites() and self._default_sprite_manager.load_sprites():
                    print("Warning: Failed to load some sprites, using fallback.")
            # Initialize UI renderer
            if not self._ui_renderer.initialize():
                print("Warning: Failed to initialize UI renderer")
            
            return True
        except Exception as e:
            print(f"Failed to initialize pygame: {e}")
            return False
    
    def render_world(self, world: World) -> None:
        self.clear_screen()
        
        # Render all entities
        entities = world.get_all_entities()
        for entity in entities:
            if self._cooldown_animation < GRAPH_REFRESH//2 or entity.get_type not in [Entity.TypeArea.PLAYER, Entity.TypeArea.ENEMY]:
                self.render_entity(entity)
            elif self._cooldown_animation < GRAPH_REFRESH:
                self.render_entity_with_variant(entity, 1)
                if self._cooldown_animation == GRAPH_REFRESH - 1:
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
        self.__render_entity_generic(entity)

    def render_entity_with_variant(self, entity: Entity, variant: int) -> None:
        self.__render_entity_generic(entity, variant)
    
    def __render_entity_generic(self, entity: Entity, variant: int = 0) -> None:
        """Render a single entity to the screen"""
        if self._screen is None:
            return
            
        area = entity.get_area()
        
        # Convert world coordinates to screen coordinates
        screen_x = int(area.get_position_x * self._scale_x)
        screen_y = int(area.get_position_y * self._scale_y)
    
        # Get sprite for this entity with proper error handling
        try:
            if isinstance(entity, Player):
                sprite = self._sprite_managers[Entity.TypeArea.PLAYER].get_sprite(entity, variant)
            elif isinstance(entity, Enemy):
                sprite = self._sprite_managers[Entity.TypeArea.ENEMY].get_sprite(entity, variant)
            elif isinstance(entity, Projectile):
                sprite = self._sprite_managers[Entity.TypeArea.PLAYER_PROJECTILE].get_sprite(entity, variant)
            elif isinstance(entity, PowerUp):
                sprite = self._sprite_managers[Entity.TypeArea.POWERUP].get_sprite(entity, variant)
            else:
                sprite = self._default_sprite_manager.get_sprite(entity.get_type, variant)

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
    
    def clear_screen(self) -> None:
        if self._screen is not None:
            self._screen.fill(BLACK)
    
    def update_display(self) -> None:
        pygame.display.flip()
    
    def get_screen_dimensions(self) -> tuple[int, int]:
        return (self._screen_width, self._screen_height)
    
    def cleanup(self) -> None:
        #pygame.quit()
        self._screen = None
