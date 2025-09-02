import math

from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import BirdAttackHandler
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


class Bird(EnemyImpl):
    """ Bird is an enemy that bounces horizontally between screen edges while falling downward. """
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        speed: int,
        health: int,
        horizontal_speed: float = 1.0,
        vertical_speed: float = 0.3,
        screen_width: int = 800,
        screen_height: int = 600,
    ) -> None:
        super().__init__(x, y, width, height, speed, health, attack_handler=BirdAttackHandler(ProjectileFactory()))
        self._horizontal_speed = max(0.0, horizontal_speed)
        self._vertical_speed = max(0.0, vertical_speed)
        self._screen_width = screen_width
        self._screen_height = screen_height
        # Direction: 1 for right, -1 for left
        self._horizontal_direction = 1
        # Accumulate fractional movement for sub-pixel speeds
        self._horizontal_accumulator = 0.0
        self._vertical_accumulator = 0.0

    def move(self) -> None:
        # Get current position using the same method as player
        current_x = self.get_area().get_position_x
        current_y = self.get_area().get_position_y
        
        # Check for boundaries and change direction if needed
        # Bounce off right edge (bird's right edge hits screen edge)
        if current_x + self.width >= self._screen_width:
            self._horizontal_direction = -1  # Change to moving left
        # Bounce off left edge (use game world left boundary)
        elif current_x <= 1:  # Match player's left limit
            self._horizontal_direction = 1   # Change to moving right
        
        # Accumulate fractional movement for smooth sub-pixel speeds
        self._horizontal_accumulator += self._horizontal_speed * self._horizontal_direction
        self._vertical_accumulator += self._vertical_speed
        
        # Extract integer movement and keep fractional part
        dx = int(self._horizontal_accumulator)
        dy = int(self._vertical_accumulator)
        
        # Keep the fractional parts for next frame
        self._horizontal_accumulator -= dx
        self._vertical_accumulator -= dy
        
        # Only move if there's actual movement to apply
        if dx != 0 or dy != 0:
            from Avian_Blasters.model.entity_impl import EntityImpl
            EntityImpl.move(self, dx, dy, self.get_area().width, self.get_area().height)
