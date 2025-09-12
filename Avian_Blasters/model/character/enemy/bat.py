from typing import Optional
from enum import Enum

from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import BatAttackHandler
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


class BatMovementState(Enum):
    DESCENDING = 1  # Moving straight down, no shooting
    HOMING = 2      # Moving from left to right homing on the player's current x-axis position, with shooting


class Bat(EnemyImpl):
    """ Bat moves straight down initially, then switches to a left to right homing movement when close to player. """

    def __init__(
        self, 
        x: int, 
        y: int, 
        width: int, 
        height: int, 
        speed: int, 
        health: int,
        horizontal_speed: float = 0.3,
        vertical_speed: float = 0.2,
        screen_width: int = 800,
        screen_height: int = 600,
    ) -> None:
        super().__init__(x, y, width, height, speed, health, attack_handler=BatAttackHandler(ProjectileFactory()))
        
        # Movement state system
        self._movement_state = BatMovementState.DESCENDING
        self._player_x: Optional[int] = None
        self._player_y: Optional[int] = None
        
        # Movement parameters
        self._horizontal_speed = max(0.0, horizontal_speed)
        self._vertical_speed = max(0.0, vertical_speed)
        self._screen_width = screen_width
        self._screen_height = screen_height
        
        # Bird-like movement parameters (used in BIRD_LIKE state)
        self._horizontal_direction = 1  # 1 for right, -1 for left
        
        # Accumulate fractional movement for sub-pixel speeds
        self._horizontal_accumulator = 0.0
        self._vertical_accumulator = 0.0
        
    def set_player_position(self, player_x: int, player_y: int) -> None:
        """Set player position for distance calculation and state switching"""
        self._player_x = player_x
        self._player_y = player_y

    def move(self) -> None:
        # Check if we should switch movement states
        self._update_movement_state()
        
        if self._movement_state == BatMovementState.DESCENDING:
            self._move_descending()
        elif self._movement_state == BatMovementState.HOMING:
            self._move_horizontal()
            
    def _update_movement_state(self) -> None:
        """Check distance to player and update movement state if needed"""
        if (self._movement_state == BatMovementState.DESCENDING and 
            self._player_y is not None):
            
            # Calculate vertical distance to player
            vertical_distance = abs(self.y - self._player_y)
            
            # Switch to bird-like movement when close to player
            if vertical_distance < 20:
                self._movement_state = BatMovementState.HOMING
                self._vertical_speed = 0
    
    def _move_descending(self) -> None:
        self._vertical_accumulator += self._vertical_speed
        
        # Extract integer movement and keep fractional part
        dx = 0  # No horizontal movement in descending state
        dy = int(self._vertical_accumulator)
        
        # Keep the fractional part for next frame
        self._vertical_accumulator -= dy
        
        # Apply movement
        if dy != 0:
            from Avian_Blasters.model.entity_impl import EntityImpl
            EntityImpl.move(self, dx, dy, self.get_area().width, self.get_area().height)
    
    def _move_horizontal(self) -> None:
        """Move from side to side homing on the x-axis position of player"""
        horizontal_direction = 0
        current_x = self.get_area().get_position_x
        if self._player_x is not None:
            if current_x < self._player_x:
                horizontal_direction = 1  # Move right toward target
            elif current_x > self._player_x:
                horizontal_direction = -1  # Move left toward target
        
        # Accumulate fractional movement for smooth sub-pixel speeds
        self._horizontal_accumulator += self._horizontal_speed * horizontal_direction
        self._vertical_accumulator += self._vertical_speed
        
        # Extract integer movement and keep fractional part
        dx = int(self._horizontal_accumulator)
        dy = int(self._vertical_accumulator)
        
        # Keep the fractional parts for next frame
        self._horizontal_accumulator -= dx
        self._vertical_accumulator -= dy
        
        # Apply movement
        if dx != 0 or dy != 0:
            from Avian_Blasters.model.entity_impl import EntityImpl
            EntityImpl.move(self, dx, dy, self.get_area().width, self.get_area().height)
    
    def shoot(self) -> list:
        """Override shooting behavior - only shoot in HOMING state"""
        if self._movement_state == BatMovementState.HOMING:
            # Use parent's shooting behavior when in bird-like mode
            return super().shoot()
        else:
            # No shooting while in descending mode
            return []
