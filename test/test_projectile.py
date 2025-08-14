import unittest
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.item import Direction
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl
from Avian_Blasters.model.position import Position

class TestProjectileFactory(unittest.TestCase):
    def setUp(self):
        self.factory = ProjectileFactory()

    def test_create_normal_projectile(self):
        projectile = self.factory.create_projectile(projectile_type = ProjectileType.NORMAL, x = 5, y = 5, direction = Direction.UP, width = 2, height = 4, type_area = Entity.TypeArea.PLAYER_PROJECTILE, delta = 1)
        self.assertIsInstance(projectile, ProjectileImpl)
        self.assertEqual(projectile.projectile_type, ProjectileType.NORMAL)
        self.assertEqual(projectile.direction, Direction.UP)
        self.assertEqual(projectile.get_area().get_position_x, 5)
        self.assertEqual(projectile.get_area().get_position_y, 5)
        self.assertTrue(projectile.active)


    def test_create_invalid_projectile_type(self):
        with self.assertRaises(ValueError):
            self.factory.create_projectile(projectile_type = "INVALID", x = 5, y = 5, direction = Direction.UP, width = 2, height = 4, type_area = Entity.TypeArea.PLAYER_PROJECTILE, delta = 1)

    def test_create_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            self.factory.create_projectile(projectile_type = ProjectileType.NORMAL, x = 5, y = 5, direction = Direction.UP, width = -1, height = 4, type_area = Entity.TypeArea.PLAYER_PROJECTILE, delta = 1)

    def test_create_invalid_type_area(self):
        with self.assertRaises(ValueError):
            self.factory.create_projectile(projectile_type = ProjectileType.NORMAL, x = 5, y = 5, direction = Direction.UP, width = 2, height = 4, type_area = "INVALID", delta = 1)

class TestProjectile(unittest.TestCase):

    def setUp(self):
        self.projectile_player = ProjectileImpl(x = 10, y = 10, width = 2, height = 4, type = Entity.TypeArea.PLAYER_PROJECTILE ,projectile_type = ProjectileType.NORMAL, direction = Direction.UP, delta = 1)
        self.projectile_enemy = ProjectileImpl(x = 20, y = 20, width = 2, height = 4, type = Entity.TypeArea.ENEMY_PROJECTILE, projectile_type = ProjectileType.NORMAL, direction = Direction.DOWN, delta = 1)

    def test_entity_type(self):
        self.assertEqual(Entity.TypeArea.PLAYER_PROJECTILE, self.projectile_player.get_type)
        self.assertEqual(Entity.TypeArea.ENEMY_PROJECTILE, self.projectile_enemy.get_type)
    

    def test_initial_status(self):
        self.assertEqual(ProjectileType.NORMAL, self.projectile_player.projectile_type)
        self.assertEqual(ProjectileType.NORMAL, self.projectile_enemy.projectile_type)
        self.assertEqual(10, self.projectile_player.get_area().get_position_x)
        self.assertEqual(20, self.projectile_enemy.get_area().get_position_x)
        self.assertEqual(10, self.projectile_player.get_area().get_position_y)
        self.assertEqual(20, self.projectile_enemy.get_area().get_position_y)
        self.assertTrue(self.projectile_player.active)
        self.assertTrue(self.projectile_enemy.active)

    def test_move(self):
        initial_position_x = self.projectile_player.get_area().get_position_x
        initial_position_y = self.projectile_player.get_area().get_position_y
        self.projectile_player.move(0, 1, 2, 2)
        new_position_x = initial_position_x + 0
        new_position_y = initial_position_y + 1
        self.assertEqual(new_position_x, self.projectile_player.get_area().get_position_x)
        self.assertEqual(new_position_y, self.projectile_player.get_area().get_position_y)

    def test_destroy(self):
        self.projectile_player.destroy()
        self.assertFalse(self.projectile_player.active)

    def test_projectile_stops_moving_when_destroyed(self):
        last_position_x = self.projectile_player.get_area().get_position_x
        last_position_y = self.projectile_player.get_area().get_position_y
        self.projectile_player.destroy()
        self.projectile_player.move(1, 1, 2, 2)
        self.assertEqual(last_position_x, self.projectile_player.get_area().get_position_x)
        self.assertEqual(last_position_y, self.projectile_player.get_area().get_position_y)
        self.assertFalse(self.projectile_player.active)