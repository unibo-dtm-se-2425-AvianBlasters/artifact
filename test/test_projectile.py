import unittest
from unittest.mock import Mock
from Avian_Blasters.model.character.player.player_attack_handler import PLAYER_COOLDOWN_STEPS, PLAYER_PROJECTILE_WIDTH, PlayerAttackHandler
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
        projectile = self.factory.create_projectile(projectile_type = ProjectileType.NORMAL, x = 5, y = 5, width = 2, height = 4, type_area = Entity.TypeArea.PLAYER_PROJECTILE, delta = 1)
        self.assertIsInstance(projectile, ProjectileImpl)
        self.assertEqual(projectile.projectile_type, ProjectileType.NORMAL)
        self.assertEqual(projectile.get_area().get_position_x, 5)
        self.assertEqual(projectile.get_area().get_position_y, 5)
        self.assertTrue(projectile.active)


    def test_create_invalid_projectile_type(self):
        with self.assertRaises(ValueError):
            self.factory.create_projectile(projectile_type = "INVALID", x = 5, y = 5, width = 2, height = 4, type_area = Entity.TypeArea.PLAYER_PROJECTILE, delta = 1)

    def test_create_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            self.factory.create_projectile(projectile_type = ProjectileType.NORMAL, x = 5, y = 5, width = -1, height = 4, type_area = Entity.TypeArea.PLAYER_PROJECTILE, delta = 1)

    def test_create_invalid_type_area(self):
        with self.assertRaises(ValueError):
            self.factory.create_projectile(projectile_type = ProjectileType.NORMAL, x = 5, y = 5, width = 2, height = 4, type_area = "INVALID", delta = 1)

class TestProjectile(unittest.TestCase):

    def setUp(self):
        self.projectile_player = ProjectileImpl(x = 10, y = 10, width = 2, height = 4, type = Entity.TypeArea.PLAYER_PROJECTILE ,projectile_type = ProjectileType.NORMAL, delta = 1)
        self.projectile_enemy = ProjectileImpl(x = 20, y = 20, width = 2, height = 4, type = Entity.TypeArea.ENEMY_PROJECTILE, projectile_type = ProjectileType.NORMAL, delta = 1)

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

class TestPlayerAttackHandler(unittest.TestCase):
    def setUp(self):
        self.projectile_factory = ProjectileFactory()
        self.attack_handler = PlayerAttackHandler(self.projectile_factory, 3, ProjectileType.NORMAL)
        self.player = Mock()
        self.player.get_area.return_value = Mock(get_position_x=50, get_position_y=50, width=10, height=10)

    def test_initial_status(self):
        self.assertEqual(self.attack_handler._projectile_speed, 3)
        self.assertEqual(self.attack_handler._projectile_type, ProjectileType.NORMAL)
        self.assertEqual(self.attack_handler._cooldown_steps, PLAYER_COOLDOWN_STEPS)

    def test_set_number_of_projectiles(self):
        self.attack_handler.set_number_of_projectiles(3)
        self.assertEqual(self.attack_handler._number_of_projectiles, 3)

    def test_try_attack_single_projectile(self):
        self.attack_handler.set_number_of_projectiles(1)
        self.assertEqual(self.attack_handler._number_of_projectiles, 1)
        projectiles = self.attack_handler.try_attack(self.player)
        self.assertEqual(len(projectiles), 1)
        for projectile in projectiles:
            self.assertIsInstance(projectile, Projectile)
            self.assertEqual(projectile.get_area().get_position_x, 50)
            self.assertEqual(projectile.get_area().get_position_y, 50)
            self.assertEqual(projectile.projectile_type, ProjectileType.NORMAL)

    def test_try_attack_double_shot(self):
        self.attack_handler.set_number_of_projectiles(2)
        self.assertEqual(self.attack_handler._number_of_projectiles, 2)
        projectiles = self.attack_handler.try_attack(self.player)
        self.assertEqual(len(projectiles), 2)   
        player_center_x = 50
        player_center_y = 50
        offset = 20
        total_width = (2 - 1) * offset
        start_x = player_center_x - total_width // 2 
        for i, projectile in enumerate(projectiles):
            self.assertIsInstance(projectile, Projectile)
            expected_x = start_x + i * (offset)
            self.assertEqual(projectile.get_area().get_position_x, expected_x)
            self.assertEqual(projectile.get_area().get_position_y, player_center_y)
            self.assertEqual(projectile.projectile_type, ProjectileType.NORMAL)
            print(projectile.get_area().get_position_x, projectile.get_area().get_position_y)

    def test_try_attack_multiple_projectiles(self):
        self.attack_handler.set_number_of_projectiles(3)
        self.assertEqual(self.attack_handler._number_of_projectiles, 3)
        projectiles = self.attack_handler.try_attack(self.player)
        self.assertEqual(len(projectiles), 3)   
        player_center_x = 50
        player_center_y = 50
        offset = 20
        total_width =  (3 - 1) * offset
        start_x = player_center_x - total_width // 2 
        for i, projectile in enumerate(projectiles):
            self.assertIsInstance(projectile, Projectile)
            expected_x = start_x + i * (offset) 
            self.assertEqual(projectile.get_area().get_position_x, expected_x)
            self.assertEqual(projectile.get_area().get_position_y, player_center_y)
            self.assertEqual(projectile.projectile_type, ProjectileType.NORMAL)
            print(projectile.get_area().get_position_x, projectile.get_area().get_position_y)

    def test_cooldown(self):
        self.attack_handler._cooldown = 0
        projectiles = self.attack_handler.try_attack(self.player)
        self.assertEqual(len(projectiles), 1)
        self.assertGreater(self.attack_handler._cooldown, 0)
        projectiles = self.attack_handler.try_attack(self.player)
        self.assertEqual(len(projectiles), 0)
        while self.attack_handler._cooldown > 0:
            projectiles = self.attack_handler.try_attack(self.player)
            self.assertEqual(len(projectiles), 0)
        projectiles = self.attack_handler.try_attack(self.player)
        self.assertEqual(len(projectiles), 1)
        
        



        