import unittest
from Avian_Blasters.model.character.player import *
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.world_impl import WorldImpl
from Avian_Blasters.model.item.item import Direction
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl
# from Avian_Blasters.model.item.item import Direction


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.players = [PlayerImpl(0,0,10,10,1,3,0,1,100,-100), PlayerImpl(0,0,10,10,1,3,0,1,100,-100)]
        self.projectiles = [ProjectileImpl(0,10,10,10,Entity.TypeArea.ENEMY_PROJECTILE,ProjectileType.NORMAL, Direction.UP, 1),
                            ProjectileImpl(0,10,10,10,Entity.TypeArea.PLAYER_PROJECTILE,ProjectileType.NORMAL, Direction.DOWN, 1),
                            ProjectileImpl(0,10,10,10,Entity.TypeArea.ENEMY_PROJECTILE,ProjectileType.NORMAL, Direction.UP, 1)]
        self.entities = list()
        for i in self.players:
            self.entities.append(i)
        for i in self.projectiles:
            self.entities.append(i)
        self.world = WorldImpl(self.entities)
    
    def test_check(self):
        self.assertEqual(self.entities, self.world.get_all_entities())
        self.assertEqual(self.players, self.world.get_players())
        self.assertEqual(list(), self.world.get_enemies())
        self.assertEqual(list(), self.world.get_power_ups())
        self.assertEqual(set(self.projectiles), set(self.world.get_projectiles()))