import unittest
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.world import World
from Avian_Blasters.model.world_impl import WorldImpl
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl
from Avian_Blasters.model.character.enemy.enemy import Enemy
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
from Avian_Blasters.model.item.power_up.power_up import PowerUp, PowerUpType
from Avian_Blasters.model.item.power_up.power_up_factory import PowerUpFactory

class TestWorld(unittest.TestCase):

    def setUp(self):
        self.power_up_factory = PowerUpFactory()
        self.players : list[Player] = [PlayerImpl(0, 0, 10, 10, 1, 3, 0, 1, 100, -100, 60), PlayerImpl(0, 0, 10, 10, 1, 3, 0, 1, 100, -100, 60)]
        self.projectiles : list[Projectile] = [ProjectileImpl(0,10,10,10,Entity.TypeArea.ENEMY_PROJECTILE,ProjectileType.NORMAL, 1),
                            ProjectileImpl(0,10,10,10,Entity.TypeArea.PLAYER_PROJECTILE,ProjectileType.NORMAL, 1),
                            ProjectileImpl(0,10,10,10,Entity.TypeArea.ENEMY_PROJECTILE,ProjectileType.NORMAL, 1)]
        self.enemies  : list[Enemy] = [Bird(0, 20, 10, 10, 2, 3, 20, 0.15), Bat(0, 15, 10, 10, 2, 3)]
        self.power_ups : list[PowerUp] = [self.power_up_factory.create_power_up(PowerUpType.INVULNERABILITY, 30, 20, 10, 10, Entity.TypeArea.POWERUP, ),
                          self.power_up_factory.create_power_up(PowerUpType.DOUBLE_FIRE, 30, 20, 10, 10, Entity.TypeArea.POWERUP, )]
        self.entities : list[Entity] = list()
        self.add(self.players + self.projectiles + self.enemies + self.power_ups)
        self.world : World = WorldImpl(self.entities)

    def add(self, entities : list[Entity]):
        for i in entities:
            self.entities.append(i)
    
    def verify(self, list : list, world_list : list[Entity]):
        self.assertEqual(set(list), set(world_list))
    
    def test_initialisation(self):
        self.verify(self.entities, self.world.get_all_entities())
        self.verify(self.players, self.world.get_players())
        self.verify(self.enemies, self.world.get_enemies())
        self.verify(self.power_ups, self.world.get_power_ups())
        self.verify(self.projectiles, self.world.get_projectiles())
    
    def test_addition(self):
        # Test addition of entities and handling of wrong addition requests
        self.world.add_entities(self.players + [None, None, None])
        self.verify(self.players + self.players, self.world.get_players())
        self.world.add_projectiles(self.projectiles)
        self.verify(self.projectiles + self.projectiles, self.world.get_projectiles())
        self.world.add_enemies(self.enemies)
        self.verify(self.enemies + self.enemies, self.world.get_enemies())
        self.world.add_power_ups([None, "Hello"] + self.power_ups)
        self.verify(self.power_ups + self.power_ups, self.world.get_power_ups())
        self.verify(self.entities + self.players + self.projectiles + self.enemies, self.world.get_all_entities())
        
        # Test explicitly that adding not Entity objects does not increase the number of entities
        before_wrong_addition = self.world.get_all_entities().count
        self.world.add_entities([1, None, "Ciao", 4])
        self.assertEqual(before_wrong_addition, self.world.get_all_entities().count)
