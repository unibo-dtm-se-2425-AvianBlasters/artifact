from typing import Optional
from enum import Enum

from Avian_Blasters.model.character.enemy.enemy_impl import EnemyImpl
from Avian_Blasters.model.character.enemy.attack_handler_impl import BatAttackHandler
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory


class BatMovementState(Enum):
    DESCENDING = 1  # Moving straight down, no shooting
    BIRD_LIKE = 2   # Moving like bird (horizontal bouncing + vertical), with shooting


class Bat(EnemyImpl):
    """ Bat moves straight down initially, then switches to bird-like movement when close to player. """

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

    def set_target_x(self, player_x: int) -> None:
        # Legacy method - not used in new behavior but kept for compatibility
        pass
        
    def set_player_position(self, player_x: int, player_y: int) -> None:
        """Set player position for distance calculation and state switching"""
        self._player_y = player_y

    def move(self) -> None:
        # Check if we should switch movement states
        self._update_movement_state()
        
        if self._movement_state == BatMovementState.DESCENDING:
            self._move_descending()
        elif self._movement_state == BatMovementState.BIRD_LIKE:
            self._move_bird_like()
            
    def _update_movement_state(self) -> None:
        """Check distance to player and update movement state if needed"""
        if (self._movement_state == BatMovementState.DESCENDING and 
            self._player_y is not None):
            
            # Calculate vertical distance to player
            vertical_distance = abs(self.y - self._player_y)
            
            # Switch to bird-like movement when close to player
            if vertical_distance < 20:
                self._movement_state = BatMovementState.BIRD_LIKE
    
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
    
    def _move_bird_like(self) -> None:
        """Move like a bird - horizontal bouncing + vertical falling"""
        current_x = self.get_area().get_position_x
        
        # Check for boundaries and change direction if needed (bird-like bouncing)
        if current_x + self.width >= self._screen_width:
            self._horizontal_direction = -1  # Change to moving left
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
        
        # Apply movement
        if dx != 0 or dy != 0:
            from Avian_Blasters.model.entity_impl import EntityImpl
            EntityImpl.move(self, dx, dy, self.get_area().width, self.get_area().height)
    
    def shoot(self) -> list:
        """Override shooting behavior - only shoot in BIRD_LIKE state"""
        if self._movement_state == BatMovementState.BIRD_LIKE:
            # Use parent's shooting behavior when in bird-like mode
            return super().shoot()
        else:
            # No shooting while in descending mode
            return []
