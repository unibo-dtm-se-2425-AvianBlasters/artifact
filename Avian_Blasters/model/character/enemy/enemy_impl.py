from enemy import Enemy

class EnemyImpl(Enemy):
    """ Base implementation for common enemy functionality. """
    
    def __init__(self, x: int, y: int, width: int, height: int, speed: int, health: int):
        super().__init__(x, y, width, height)
        self.health = health
        self.speed = speed

    def move(self):
        """ default movement: move downwards at the speed defined """
        self.y += self.speed
        
    def attack(self):
        pass  # Implement specific attack logic in subclasses

    def take_damage(self, damage: int):
        """ Reduce health by given damage amount. """
        self.health -= damage
        
    def is_dead(self) -> bool:
        """ Check if the enemy is dead. """
        return self.health <= 0
        