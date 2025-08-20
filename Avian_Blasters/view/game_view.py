import pygame
from typing import List
from Avian_Blasters.model.world import World
from Avian_Blasters.model.entity import Entity

class GameView:
    """GameView defines the interface for rendering the game world using pygame"""
    
    def initialize(self, width: int, height: int, title: str) -> bool:
        """Initialize the pygame display and return success status"""
        ...
    
    def render_world(self, world: World) -> None:
        """Render the complete game world including all entities"""
        ...
    
    def render_entity(self, entity: Entity) -> None:
        """Render a single entity to the screen"""
        ...
    
    def render_entity_with_variant(self, entity: Entity, variant: int) -> None:
        """Render a single entity with a specific sprite variant"""
        ...
    
    def clear_screen(self) -> None:
        """Clear the screen with background color"""
        ...
    
    def update_display(self) -> None:
        """Update the pygame display"""
        ...
    
    def get_screen_dimensions(self) -> tuple[int, int]:
        """Get the current screen width and height"""
        ...
    
    def cleanup(self) -> None:
        """Cleanup pygame resources"""
        ...
