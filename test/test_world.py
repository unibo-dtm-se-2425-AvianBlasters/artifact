import unittest
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.world_impl import WorldImpl
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl
from Avian_Blasters.model.character.enemy.bird import Bird
from Avian_Blasters.model.character.enemy.bat import Bat
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_factory import PowerUpFactory

class TestWorld(unittest.TestCase):

    def setUp(self):
        self.power_up_factory = PowerUpFactory()
        self.players = [PlayerImpl(0, 0, 10, 10, 1, 3, 0, 1, 100, -100, 60), PlayerImpl(0, 0, 10, 10, 1, 3, 0, 1, 100, -100, 60)]
        self.projectiles = [ProjectileImpl(0,10,10,10,Entity.TypeArea.ENEMY_PROJECTILE,ProjectileType.NORMAL, 1),
                            ProjectileImpl(0,10,10,10,Entity.TypeArea.PLAYER_PROJECTILE,ProjectileType.NORMAL, 1),
                            ProjectileImpl(0,10,10,10,Entity.TypeArea.ENEMY_PROJECTILE,ProjectileType.NORMAL, 1)]
        self.enemies = [Bird(0, 20, 10, 10, 2, 3, 20, 0.15), Bat(0, 15, 10, 10, 2, 3)]
        self.power_ups = [self.power_up_factory.create_power_up(PowerUpType.INVULNERABILITY, 30, 20, 10, 10, Entity.TypeArea.POWERUP, ),
                          self.power_up_factory.create_power_up(PowerUpType.DOUBLE_FIRE, 30, 20, 10, 10, Entity.TypeArea.POWERUP, )]
        self.entities = list()
        self.__add(self.players + self.projectiles + self.enemies + self.power_ups + [1, None, "Ciao", 4])
        self.world = WorldImpl(self.entities)

    def __add(self, entities : list[Entity]):
        for i in entities:
            self.entities.append(i)
    
    def test_initialisation(self):
        self.assertEqual(self.entities, self.world.get_all_entities())
        self.assertEqual(self.players, self.world.get_players())
        self.assertEqual(set(self.enemies), set(self.world.get_enemies()))
        self.assertEqual(set(self.power_ups), set(self.world.get_power_ups()))
        self.assertEqual(set(self.projectiles), set(self.world.get_projectiles()))
    
    def test_addition(self):
        self.world.add_entities(self.players + [None, None, None])
        self.assertEqual(self.players + self.players, self.world.get_players())
        self.world.add_projectiles(self.projectiles)
        self.assertEqual(set(self.projectiles + self.projectiles), set(self.world.get_projectiles()))
        self.world.add_enemies(self.enemies)
        self.assertEqual(set(self.enemies + self.enemies), set(self.world.get_enemies()))
        self.world.add_power_ups([None, "Hello"] + self.power_ups)
        self.assertEqual(set(self.power_ups + self.power_ups), set(self.world.get_power_ups()))
        self.assertEqual(set(self.entities + self.players + self.projectiles + self.enemies), set(self.world.get_all_entities()))
