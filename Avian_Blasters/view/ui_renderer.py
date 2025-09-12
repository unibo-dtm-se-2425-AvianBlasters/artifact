import pygame
from Avian_Blasters.model.character.player.player import Player

class UIRenderer:
    """UIRenderer defines the interface for rendering game UI elements"""
    
    def initialize(self, font_size: int = 24) -> bool:
        """Initialize fonts and UI resources"""
        ...
    
    def render_score(self, screen: pygame.Surface, player: Player, x: int, y: int) -> None:
        """Render the player's score at the specified position"""
        ...
    
    def render_health(self, screen: pygame.Surface, player: Player, x: int, y: int) -> None:
        """Render the player's health/lives at the specified position"""
        ...
    
    def render_game_over(self, screen: pygame.Surface, screen_width: int, screen_height: int) -> None:
        """Render game over screen"""
        ...
    
    def cleanup(self) -> None:
        """Cleanup UI resources"""
        ...
