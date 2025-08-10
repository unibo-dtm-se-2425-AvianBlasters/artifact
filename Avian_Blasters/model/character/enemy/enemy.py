from character import Character

class Enemy(Character):
    """Abstract base class for all enemies in the game."""
    
    def attack (self):
        """ It defines how the enemy attacks the player."""
        raise NotImplementedError("This method should be overridden by subclasses.")