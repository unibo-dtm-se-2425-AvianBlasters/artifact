from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.character.player.player import Player
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.item.power_up.power_up import PowerUp
from Avian_Blasters.model.item.projectile.projectile import Projectile

WORLD_WIDTH = 160 #or it could be 120
WORLD_HEIGHT = 90 

class World:

    def get_all_entities(self) -> list[Entity]:
        ...
    
    def add_entities(self, entities : list[Entity]):
        ...

    def get_player(self) -> Player:
        ...
    
    def get_enemies(self) -> list[Enemy]:
        ...

    def get_power_ups(self) -> list[PowerUp]:
        ...
    
    def get_projectiles(self) -> list[Projectile]:
        ...