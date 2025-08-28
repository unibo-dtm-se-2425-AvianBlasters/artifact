from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.item.power_up.power_up import PowerUp
from Avian_Blasters.model.item.projectile.projectile import Projectile

WORLD_WIDTH = 120
WORLD_HEIGHT = 90 

class World:
    """World is the class containing all of the elements the game world
    is comprised of"""

    def get_all_entities(self) -> list[Entity]:
        """Returns all of the entities of the game"""
        ...
    
    def add_entities(self, entities : list[Entity]):
        """Adds a list of entites to the one of World"""
        ...

    def get_players(self) -> list[Player]:
        """Returns a list of the player characters"""
        ...
    
    def get_enemies(self) -> list[Enemy]:
        """Returns a list of the enemies currently present in the game
        world"""
        ...
    
    def add_enemies(self, enemies : list[Enemy]):
        """Adds a list of enemies to the one contained in World"""
        ...

    def get_power_ups(self) -> list[PowerUp]:
        """Returns a list of the power-ups currently present in the game
        world"""
        ...
    
    def add_power_ups(self, power_ups : list[PowerUp]):
        """Adds a list of power-ups to the one contained in World"""
        ...
    
    def get_projectiles(self) -> list[Projectile]:
        """Returns a list of the projectiles currently present in the game
        world"""
    
    def add_projectiles(self, projectiles : list[Projectile]):
        """Adds a list of projectiles to the one contained in World"""

    def remove_entity(self, entity: Entity):
        """Removes an entity from World"""
