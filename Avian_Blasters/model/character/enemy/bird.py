from enemy_impl import EnemyImpl

class Bird(EnemyImpl):
    """Implementation of a bird enemy with predictable wave movement 
    and projectile attacks in the game."""

    def __init__(self, x: int, y: int, width: int, height: int, speed: int, health: int):
        super().__init__(x, y, width, height, speed, health)
        self.direction = 1 # 1 for right, -1 for left

    def attack(self):
        """Birds attack by dropping projectiles."""
        print(f"Bird at ({self.x}, {self.y}) attacks by dropping a projectile.")

    def move(self):
        """Move in a wave pattern (left-right sweeping)."""
        self.x += self._speed * self.direction
        if self.x <= 0 or self.x >= 800 - self.width: # Assuming 800 is the screen width
            self.direction *= -1 # Change direction when hitting screen edges
        self.y += self.speed

        


    