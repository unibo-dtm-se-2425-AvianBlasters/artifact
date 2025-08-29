from typing import List
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat

def create_enemy_formation() -> List[Entity]:
    """Create a formation of enemies like in the reference UI."""
    enemies = []
    
    # Create a simple enemy formation
    # Top row: Birds
    for i in range(11):
        x = 10 + i * 10
        y = 10
        enemy = Bird(x, y, 4, 4, 1, health=2, wave_amplitude=5)
        enemies.append(enemy)
    
    # Second row: More birds  
    for i in range(9):
        x = 15 + i * 10
        y = 20
        enemy = Bird(x, y, 4, 4, 1, health=1)
        enemies.append(enemy)
    
    # Middle rows: Bats
    for row in range(2):
        for i in range(3):
            x = 30 + i * 15
            y = 30 + row * 10
            enemy = Bat(x, y, 4, 4, 1, health=3)
            enemies.append(enemy)
    
    # Add some scattered enemies
    scattered_positions = [(15, 45), (60, 35), (90, 25), (45, 50)]
    for i, (x, y) in enumerate(scattered_positions):
        # Alternate between Bird and Bat
        if i % 2 == 0:
            enemy = Bird(x, y, 4, 4, 1, health=2)
        else:
            enemy = Bat(x, y, 4, 4, 1, health=2)
        enemies.append(enemy)
    
    return enemies