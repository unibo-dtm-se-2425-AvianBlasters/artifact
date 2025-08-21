from enum import Enum

class PlayerStatus:
    """PlayerStatus is a class to handle the current status of the player character"""
    class Status(Enum):
        """Status is a way to represent all the possible statuses the player character can be in"""
        NORMAL = 1
        """State the player is normally in"""
        INVULNERABLE = 2
        """State the player is in after getting hit or after obtaining a certain
        power-up"""
        SLOWED = 3
        """State the player is in when affected by bat sound waves, reducing movement speed"""
    
    @property
    def status(self) -> Status:
        """Access the current status of the player character"""
        ...
    
    @status.setter
    def status(self, new_status : Status):
        ...
    
    def invincibility(self, cooldown : int):
        """Change the status to invulnerable for a certain time (cooldown)"""
        ...
    
    def slow_down(self, cooldown : int):
        """Slow down the player for a certain time (cooldown) due to sound wave attack"""
        ...
    
    def update(self):
        """If the status is different from the normal one, decrease the countdown by one
        until the countdown is equal to zero, then change the status of player back to normal"""
        ...