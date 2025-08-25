from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.world import World
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.item.power_up.power_up import PowerUp
from Avian_Blasters.model.item.projectile.projectile import Projectile
from typing import Type

WORLD_WIDTH = 120
WORLD_HEIGHT = 90 

class WorldImpl(World):
    """WorldImpl is an implementation of World"""
    
    def __init__(self, entities : list[Entity]):
        self._entities = entities
        self.__cleaner()

    def get_all_entities(self) -> list[Entity]:
        return self._entities
    
    def add_entities(self, entities : list[Entity]):
        self.__setter(entities)

    def get_players(self) -> list[Player]:
        return self.__getter(Player)
    
    def get_enemies(self) -> list[Enemy]:
        return self.__getter(Enemy)
    
    def add_enemies(self, enemies : list[Enemy]):
        self.add_entities(enemies)

    def get_power_ups(self) -> list[PowerUp]:
        return self.__getter(PowerUp)

    def add_power_ups(self, power_ups : list[PowerUp]):
        self.add_entities(power_ups)
    
    def get_projectiles(self) -> list[Projectile]:
        temp = self.__getter(Projectile)
        return temp
    
    def add_projectiles(self, projectiles : list[Projectile]):
        self.add_entities(projectiles)

    def __getter(self, class_type : Type) -> list[Entity]:
        self.__cleaner()
        result_list = []
        for i in self._entities:
            if isinstance(i, class_type):
                result_list.append(i)
        return result_list
    
    def __setter(self, entities : list):
        for i in entities:
            if i is not None:
                self._entities.append(i)
    
    def __cleaner(self):
        for i in self._entities[:]:
            if not isinstance(i, Entity):
                self._entities.remove(i)