import math
from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import BirdAttackHandler
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


class Bird(EnemyImpl):
    """ Bird is an enemy that moves in formation like Space Invaders. """
    
    # Class variables for formation movement
    _formation_direction = 1  # 1 for right, -1 for left
    _formation_horizontal_speed = 0.03
    _formation_vertical_speed = 0.02
    
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
        self._screen_width = screen_width
        self._screen_height = screen_height
        # Accumulate fractional movement for sub-pixel speeds
        self._horizontal_accumulator = 0.0
        self._vertical_accumulator = 0.0

    @classmethod
    def set_formation_direction(cls, direction: int) -> None:
        """Set the direction for the entire formation"""
        cls._formation_direction = direction

    @classmethod
    def get_formation_direction(cls) -> int:
        """Get the current formation direction"""
        return cls._formation_direction

    def move(self) -> None:
        """Move as part of formation - no individual boundary checking"""
        # Use formation movement speed and direction
        self._horizontal_accumulator += Bird._formation_horizontal_speed * Bird._formation_direction
        self._vertical_accumulator += Bird._formation_vertical_speed
        
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
