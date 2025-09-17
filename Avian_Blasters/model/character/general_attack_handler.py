from abc import abstractmethod
from Avian_Blasters.model.character.character import Character
from Avian_Blasters.model.cooldown_handler import CoolDownHandler
from Avian_Blasters.model.item.projectile.projectile import Projectile


class GeneralAttackHandler:
    """ GeneralAttackHandler is a class that handles the attack of a character"""

    @property
    def projectile_type(self) -> str:
        """ Returns the type of projectile used by the character """
        ...

    @property
    def cooldown_handler(self) -> CoolDownHandler:
        """ Returns the cooldown handler of the character """
        ...
    
    @abstractmethod
    def try_attack(self, character : Character) -> list[Projectile]:
        """ Tries to make the character shoot, returning a list of projectiles if successful """
        ...

    @abstractmethod
    def update(self):
        """ Updates the cooldown handler of the character """
        ...

    