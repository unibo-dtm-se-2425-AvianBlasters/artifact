from typing import List
import random
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
from Avian_Blasters.model.world import WORLD_HEIGHT
from Avian_Blasters.model.world_impl import WORLD_WIDTH

def create_enemy_formation() -> List[Entity]:
    """Spawn enemies randomly from the top - 80% birds, 20% bats"""
    from Avian_Blasters.model.character.enemy.bird import Bird
    from Avian_Blasters.model.character.enemy.bat import Bat
    
    enemies = []
    
    # Randomly spawn 2-4 enemies per wave
    num_enemies = random.randint(1, 2)
    
    for i in range(num_enemies):
        # Random horizontal position across the top (with some margin)
        spawn_x = random.randint(10, WORLD_WIDTH - 20)
        spawn_y = random.randint(-5, 5)  # Slight variation in spawn height
        
        # 20% chance for bat, 80% chance for bird
        if random.random() < 0.20:
            # Spawn a bat
            enemy = Bat(
                x=spawn_x,
                y=spawn_y,
                width=8,
                height=5,
                speed=1,
                health=3,
                horizontal_speed=random.uniform(0.2, 0.4),  # Random speed variation
                vertical_speed=random.uniform(0.1, 0.2),    # Random descent speed
                screen_width=WORLD_WIDTH,
                screen_height=WORLD_HEIGHT
            )
        else:
            # Spawn a bird
            enemy = Bird(
                x=spawn_x,
                y=spawn_y,
                width=8,
                height=5,
                speed=1,
                health=3,
                horizontal_speed=random.uniform(0.3, 0.7),  # Random speed variation
                vertical_speed=random.uniform(0.01, 0.05),  # Slow falling
                screen_width=WORLD_WIDTH,
                screen_height=WORLD_HEIGHT
            )
        
        enemies.append(enemy)
    
    return enemies
