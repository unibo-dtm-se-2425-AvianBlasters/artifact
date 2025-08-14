from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.world import World
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.item.power_up.power_up import PowerUp
from Avian_Blasters.model.item.projectile.projectile import Projectile

WORLD_WIDTH = 120
WORLD_HEIGHT = 90 

class WorldImpl(World):
    def __init__(self, entities : list[Entity]):
        self._entities = entities

    def get_all_entities(self) -> list[Entity]:
        return self._entities
    
    def add_entities(self, entities : list[Entity]):
        ...

    def get_players(self) -> list[Player]:
        return self.__getter(Entity.TypeArea.PLAYER)
    
    def get_enemies(self) -> list[Enemy]:
        return self.__getter(Entity.TypeArea.ENEMY)
    
    def add_enemies(self, enemies : list[Enemy]):
        ...

    def get_power_ups(self) -> list[PowerUp]:
        return self.__getter(Entity.TypeArea.POWERUP)

    
    def add_power_ups(self, power_ups : list[PowerUp]):
        ...
    
    def get_projectiles(self) -> list[Projectile]:
        temp = self.__getter(Entity.TypeArea.PLAYER_PROJECTILE) + self.__getter(Entity.TypeArea.ENEMY_PROJECTILE)
        return temp
    
    def add_projectiles(self, projectiles : list[Projectile]):
        ...

    def __getter(self, type : Entity.TypeArea) -> list[type]:
        list = []
        for i in self._entities:
            if i.get_type == type:
                list.append(i)
        return list