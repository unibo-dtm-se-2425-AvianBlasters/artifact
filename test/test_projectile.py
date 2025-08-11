import unittest
from Avian_Blasters.model.item.projectile.laser_projectile import LaserProjectile
from Avian_Blasters.model.item.projectile.normal_projectile import NormalProjectile
from Avian_Blasters.model.item.projectile.projectile import Projectile, ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory
from Avian_Blasters.model.item.projectile.projectile_impl import ProjectileImpl
from Avian_Blasters.model.position import Position

class TestProjectileFactory(unittest.TestCase):
    def setUp(self):
        self.factory = ProjectileFactory()

    def test_create_normal_projectile(self):
        position = Position(2, 2)
        projectile = self.factory.create_projectile(ProjectileType.NORMAL, position)
        self.assertIsInstance(projectile, NormalProjectile)
        self.assertEqual(position, projectile.position)

    def test_create_laser_projectile(self):
        position = Position(3, 3)
        projectile = self.factory.create_projectile(ProjectileType.LASER, position)
        self.assertIsInstance(projectile, LaserProjectile)
        self.assertEqual(position, projectile.position)

class TestProjectile(unittest.TestCase):
    initial_x = 8
    initial_y = 8
    direction = -1
    speed = 1
    projectile_type = ProjectileType.NORMAL
    initial_position = Position(initial_x, initial_y)

    def setUp(self):
        self.projectile = ProjectileImpl(self.projectile_type, self.initial_position, direction=self.direction, speed=self.speed)

    def test_initial_status(self):
        self.assertEqual(self.projectile_type, self.projectile.type)
        self.assertEqual(self.initial_position, self.projectile.position)
        self.assertTrue(self.projectile.active)
        self.assertEqual(self.direction, self.projectile.direction)

    def test_move(self):
        initial_position = self.projectile.position
        self.projectile.move()
        new_position = Position(initial_position.x, initial_position.y + self.direction * self.speed)
        self.assertEqual(new_position, self.projectile.position)

    def test_destroy(self):
        self.projectile.destroy()
        self.assertFalse(self.projectile.active)

    def test_projectile_stops_moving_when_destroyed(self):
        last_position = self.projectile.position
        self.projectile.destroy()
        self.projectile.move()
        self.assertEqual(last_position, self.projectile.position)
        self.assertFalse(self.projectile.active)