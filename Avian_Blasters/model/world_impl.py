from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.world import World
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.item.power_up.power_up import PowerUp
from Avian_Blasters.model.item.projectile.projectile import Projectile

WORLD_WIDTH = 120
WORLD_HEIGHT = 90 

class WorldImpl(World):
    """WorldImpl is an implementation of World"""
    
    def __init__(self, entities : list[Entity]):
        self._entities = entities

    def get_all_entities(self) -> list[Entity]:
        return self._entities
    
    def add_entities(self, entities : list[Entity]):
        self.__setter(entities)

    def get_players(self) -> list[Player]:
        return self.__getter(Entity.TypeArea.PLAYER)
    
    def get_enemies(self) -> list[Enemy]:
        return self.__getter(Entity.TypeArea.ENEMY)
    
    def add_enemies(self, enemies : list[Enemy]):
        self.add_entities(enemies)

    def get_power_ups(self) -> list[PowerUp]:
        return self.__getter(Entity.TypeArea.POWERUP)

    def add_power_ups(self, power_ups : list[PowerUp]):
        self.add_entities(power_ups)
    
    def get_projectiles(self) -> list[Projectile]:
        temp = self.__getter(Entity.TypeArea.PLAYER_PROJECTILE) + self.__getter(Entity.TypeArea.ENEMY_PROJECTILE)
        return temp
    
    def add_projectiles(self, projectiles : list[Projectile]):
        self.add_entities(projectiles)

    def __getter(self, type : Entity.TypeArea) -> list[Entity]:
        result_list = []
        for i in self._entities:
            if i.get_type == type:
                result_list.append(i)
        return result_list
    
    def __setter(self, entities : list):
        for i in entities:
            self._entities.append(i)