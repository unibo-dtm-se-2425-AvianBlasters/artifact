import pygame
from typing import Optional
from Avian_Blasters.view.ui_renderer import UIRenderer
from Avian_Blasters.model.character.player.player import Player

class UIRendererImpl(UIRenderer):
    """UIRendererImpl is a pygame implementation of UIRenderer"""
    
    def __init__(self):
        self._font: Optional[pygame.font.Font] = None
        self._small_font: Optional[pygame.font.Font] = None
        
    def initialize(self, font_size: int = 24) -> bool:
        """Initialize fonts and UI resources"""
        try:
            pygame.font.init()
            self._font = pygame.font.Font(None, font_size)
            self._small_font = pygame.font.Font(None, 16)
            return True
        except Exception as e:
            print(f"Failed to initialize UI renderer: {e}")
            return False
    
    def render_score(self, screen: pygame.Surface, player: Player, x: int, y: int) -> None:
        """Render the player's score at the specified position"""
        if self._font is None:
            return
            
        try:
            score = player.get_score().score
            score_text = f"SCORE: {score:07d}"
            text_surface = self._font.render(score_text, True, (255, 255, 255))
            screen.blit(text_surface, (x, y))
        except Exception as e:
            # Fallback if score system isn't fully implemented
            score_text = "SCORE: 0000000"
            text_surface = self._font.render(score_text, True, (255, 255, 255))
            screen.blit(text_surface, (x, y))
    
    def render_health(self, screen: pygame.Surface, player: Player, x: int, y: int) -> None:
        """Render the player's health/lives at the specified position"""
        if self._small_font is None:
            return
            
        try:
            health = player.get_health_handler().current_health
            # Render health as colored indicator
            if health >= 3:
                color = (0, 255, 0)  # Green
                status = "HEALTHY"
            elif health >= 2:
                color = (255, 255, 0)  # Yellow  
                status = "DAMAGED"
            else:
                color = (255, 0, 0)  # Red
                status = "CRITICAL"
                
            health_text = f"HEALTH: {status}"
            text_surface = self._small_font.render(health_text, True, color)
            screen.blit(text_surface, (x, y))
        except Exception as e:
            # Fallback
            health_text = "HEALTH: HEALTHY"
            text_surface = self._small_font.render(health_text, True, (0, 255, 0))
            screen.blit(text_surface, (x, y))
    
    def render_game_over(self, screen: pygame.Surface, screen_width: int, screen_height: int) -> None:
        """Render game over screen"""
        if self._font is None:
            return
            
        game_over_text = self._font.render("GAME OVER", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, text_rect)
        
        restart_text = self._small_font.render("Press SPACE to restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 40))
        screen.blit(restart_text, restart_rect)
    
    def cleanup(self) -> None:
        """Cleanup UI resources"""
        pass
