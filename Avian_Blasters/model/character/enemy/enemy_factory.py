from typing import List, Optional
import random
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
from Avian_Blasters.model.world import WORLD_HEIGHT, WORLD_WIDTH

_bat_spawn_timer = 0.0
_bat_spawn_interval = random.uniform(5.0, 20.0)  

def create_enemy_formation() -> List[Entity]:
    """Spawn 5 birds in a row formation at the start of the game"""
    from Avian_Blasters.model.character.enemy.bird import Bird
    from Avian_Blasters.model.character.enemy.bat import Bat
    
    enemies = []
    
    # Create 5 birds in a row formation
    num_birds = 10
    num_rows = 3
    
    # Calculate spacing to spread the birds evenly across the screen
    # Leave some margin on both sides (20 pixels each side)
    margin = 10
    available_width = WORLD_WIDTH - 2 * margin
    spacing = available_width // (num_birds + 1)  # +1 to have even spacing including edges
    
    for y in range(num_rows):
        for i in range(num_birds):
            # Position birds evenly across the screen width
            spawn_x = margin + spacing * (i + 1)
            spawn_y = 5 + (y * spacing)  # Aligned in a row
            
            # Create a bird
            enemy = Bird(
                x=spawn_x,
                y=spawn_y,
                width=8,
                height=5,
                speed=1,
                health=3,
                horizontal_speed=0.05,  # Random speed variation
                vertical_speed=0.01,  # Slow falling
                screen_width=WORLD_WIDTH,
                screen_height=WORLD_HEIGHT
            )
            
            enemies.append(enemy)
    
    return enemies

def create_random_bat() -> Entity:
    """Create a single bat that spawns randomly during gameplay"""
    from Avian_Blasters.model.character.enemy.bat import Bat
    
    # Random horizontal position across the top (with some margin)
    spawn_x = random.randint(10, WORLD_WIDTH - 20)
    spawn_y = random.randint(-10, 0)  # Spawn slightly above the screen
    
    # Create a bat with random movement characteristics
    bat = Bat(
        x=spawn_x,
        y=spawn_y,
        width=8,
        height=5,
        speed=1,
        health=3,
        horizontal_speed=random.uniform(0.2, 0.4),  # Random horizontal speed
        vertical_speed=random.uniform(0.1, 0.2),    # Random descent speed
        screen_width=WORLD_WIDTH,
        screen_height=WORLD_HEIGHT
    )
    
    return bat

def update_bat_spawning(delta_time: float, enemies: List[Entity]) -> Optional[Entity]:
    """Handle bat spawning timing and logic - returns new bat if one should be spawned"""
    # Bat spawning system state
    global _bat_spawn_timer, _bat_spawn_interval

    # Update bat spawn timer
    _bat_spawn_timer += delta_time
    
    # Check if it's time to spawn a bat
    if _bat_spawn_timer >= _bat_spawn_interval:
        # Check if there's already a bat alive (only allow one bat at a time)
        existing_bats = [enemy for enemy in enemies if isinstance(enemy, Bat)]
        
        if not existing_bats:  # No bats currently alive
            # Reset timer and set next random interval
            _bat_spawn_timer = 0.0
            _bat_spawn_interval = random.uniform(15.0, 25.0)  # Next bat in 15-25 seconds
            
            # Create and return a new random bat
            return create_random_bat()
    
    return None

def handle_bird_formation_movement(enemies: List[Entity]) -> None:
    """Handle Space Invaders style formation movement for birds"""
    from Avian_Blasters.model.character.enemy.bird import Bird
    
    # Get all birds from the provided enemies list
    birds = [enemy for enemy in enemies if isinstance(enemy, Bird)]
    
    if not birds:
        return
    
    # Find the leftmost and rightmost birds
    leftmost_bird = min(birds, key=lambda bird: bird.get_area().get_position_x)
    rightmost_bird = max(birds, key=lambda bird: bird.get_area().get_position_x + bird.get_area().width)
    
    # Check boundaries and change direction if needed
    current_direction = Bird.get_formation_direction()
    
    # Check if moving right and rightmost bird would hit right wall
    if current_direction > 0 and rightmost_bird.get_area().get_position_x + rightmost_bird.get_area().width >= WORLD_WIDTH:
        Bird.set_formation_direction(-1) 
    elif current_direction < 0 and leftmost_bird.get_area().get_position_x <= 5:
        Bird.set_formation_direction(1)  

def can_bird_shoot(bird: Entity, all_enemies: List[Entity]) -> bool:
    """Check if a bird can shoot - only if there's no living bird directly in front of it"""
    from Avian_Blasters.model.character.enemy.bird import Bird
    
    if not isinstance(bird, Bird):
        return True  # Non-birds can always shoot
    
    bird_x = bird.get_area().get_position_x
    bird_y = bird.get_area().get_position_y
    
    # Get all living birds
    living_birds = [enemy for enemy in all_enemies 
                   if isinstance(enemy, Bird) and not enemy.is_dead()]
    
    # Check if there's any living bird in front (lower y-coordinate, same column)
    for other_bird in living_birds:
        if other_bird == bird:
            continue
            
        other_x = other_bird.get_area().get_position_x
        other_y = other_bird.get_area().get_position_y

        x_tolerance = 5  # Adjust based on your bird spacing
        
        if (abs(other_x - bird_x) <= x_tolerance and other_y > bird_y):
            # There's a living bird in front, this bird cannot shoot
            return False
    
    return True
