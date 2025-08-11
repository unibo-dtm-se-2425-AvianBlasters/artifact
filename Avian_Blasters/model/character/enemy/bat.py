from enemy_impl import EnemyImpl

class Bird(EnemyImpl):
    """ Bat enemy with homing behavior and sound wave attacks."""

    def __init__(self, x: int, y: int, width: int, height: int, speed: int, health: int):
        super().__init__(x, y, width, height, speed, health)
        

    def attack(self):
        """Bat attacks by emitting a sound wave."""
        print(f"Bat at ({self.x}, {self.y}) attacks by emitting a sound wave.")

    def move(self, player_x: int):
        """Move horizontally towards the player."""
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self._x -= self.speed
            
        