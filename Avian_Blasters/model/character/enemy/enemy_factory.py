from typing import List
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
from Avian_Blasters.model.world import WORLD_WIDTH
from Avian_Blasters.model.world_impl import WORLD_HEIGHT

def create_enemy_formation() -> List[Entity]:
        """Create a single green bird and a bat for testing movement"""
        from Avian_Blasters.model.character.enemy.bird import Bird
        from Avian_Blasters.model.character.enemy.bat import Bat
        
        enemies = []
        
        # Spawn only one green bird for testing
        # Start at left side of screen, move right while falling slowly
        bird = Bird(
            x=10,  # Start near left edge
            y=10,  # Start near top
            width=8, 
            height=5, 
            speed=1, 
            health=3,  # Green variant
            horizontal_speed=0.5,  # Move right at moderate speed
            vertical_speed=0.01,    # Fall slowly downward
            screen_width=WORLD_WIDTH,   # Use game world coordinates, not pixel coordinates
            screen_height=WORLD_HEIGHT
        )
        enemies.append(bird)
        
        # Add a bat with similar positioning but offset to avoid collision
        bat = Bat(
            x=50,  # Start more to the right than bird
            y=10,  # Same starting height
            width=8, 
            height=5, 
            speed=1, 
            health=3,
            horizontal_speed=0.3,  # Smooth horizontal chase speed
            vertical_speed=0.15    # Slow falling speed
        )
        enemies.append(bat)
        
        return enemies
