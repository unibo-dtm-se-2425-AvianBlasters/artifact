import unittest
from unittest.mock import Mock, PropertyMock, patch
from Avian_Blasters.model.area import Area
from Avian_Blasters.model.area_impl import AreaImpl
from Avian_Blasters.model.character.player.player_attack_handler import PlayerAttackHandler
from Avian_Blasters.model.character.player.player_status_handler import PlayerStatus
from Avian_Blasters.model.character.player.player_status_handler_impl import PlayerStatusImpl
from Avian_Blasters.model.character.player.power_up_handler_impl import PowerUpHandlerImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_factory import PowerUpFactory
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl
from Avian_Blasters.model.item.power_up.power_up_types.double_fire_power_up import DoubleFirePowerUp
from Avian_Blasters.model.item.power_up.power_up_types.health_recovery_power_up import HealthRecoveryPowerUp
from Avian_Blasters.model.item.power_up.power_up_types.invulnerability_power_up import InvulnerabilityPowerUp
from Avian_Blasters.model.item.power_up.power_up_types.laser_power_up import LaserPowerUp
from Avian_Blasters.model.item.projectile.projectile import ProjectileType
from Avian_Blasters.model.item.projectile.projectile_factory import ProjectileFactory

class DummyPowerUp(PowerUpImpl):
    def apply_effect(self, player):
        pass

class TestPowerUp(unittest.TestCase):
    def setUp(self):
        self.power_up = DummyPowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.LASER, is_timed= True, duration = 10.0, delta=1)

    def test_initial_status(self):
        self.assertEqual(10, self.power_up.get_area().get_position_x)
        self.assertEqual(10, self.power_up.get_area().get_position_y)
        self.assertEqual(4, self.power_up.get_area().width)
        self.assertEqual(4, self.power_up.get_area().height)
        self.assertEqual(Entity.TypeArea.POWERUP, self.power_up.get_type)
        self.assertEqual(PowerUpType.LASER, self.power_up.power_up_type)

    def test_is_collected_true(self):
        player_area = AreaImpl(10, 10, 5, 5)
        self.assertTrue(self.power_up.is_collected(player_area))
        self.assertTrue(self.power_up._collected)

    def test_is_collected_false(self):
        player_area = AreaImpl(20, 20, 5, 5)
        self.assertFalse(self.power_up.is_collected(player_area))
        self.assertFalse(self.power_up._collected)

class LaserPowerUpTest(unittest.TestCase):
    def setUp(self):
        self.power_up = LaserPowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.LASER, is_timed=True, duration=10.0, delta=1)
        self.player = Mock()

    def test_apply_and_remove_effect(self):
        self.power_up.apply_effect(self.player)
        self.player.player_attack_handler_get().set_projectile_type.assert_called_with(ProjectileType.LASER)
        self.power_up.remove_effect(self.player)
        self.player.player_attack_handler_get().set_projectile_type.assert_called_with(ProjectileType.NORMAL)

class InvulnerabilityPowerUpTest(unittest.TestCase):
    def setUp(self):
        self.power_up = InvulnerabilityPowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.INVULNERABILITY, is_timed=True, duration=10.0, delta=1)
        self.player = Mock()
        self.player_status = PlayerStatusImpl(PlayerStatus.Status.NORMAL)
        self.player.get_status.return_value = self.player_status

    def test_initial_status(self):
        self.assertEqual(PlayerStatus.Status.NORMAL, self.player_status.status)

    def test_apply_and_remove_effect(self):
        self.power_up.apply_effect(self.player)
        self.assertEqual(self.player_status.status, PlayerStatus.Status.INVULNERABLE)
        self.power_up.remove_effect(self.player)
        self.assertEqual(self.player_status.status, PlayerStatus.Status.NORMAL)

class DoubleFirePowerUpTest(unittest.TestCase):
    def setUp(self):
        self.power_up = DoubleFirePowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.DOUBLE_FIRE, is_timed=True, duration=10.0, delta=1)
        self.projectile_factory = ProjectileFactory()
        self.attack_handler = PlayerAttackHandler(self.projectile_factory, 3, ProjectileType.NORMAL)
        self.player = Mock()
        self.player.player_attack_handler_get = Mock(return_value=self.attack_handler)

    def test_apply_and_remove_effect(self):
        self.power_up.apply_effect(self.player)
        self.assertEqual(self.player.player_attack_handler_get().number_of_projectiles, 2)
        self.power_up.remove_effect(self.player)
        self.assertEqual(self.player.player_attack_handler_get().number_of_projectiles, 1)

class HealthRecoveryPowerUpTest(unittest.TestCase):
    def setUp(self):
        self.power_up = HealthRecoveryPowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.HEALTH_RECOVERY, is_timed=False, duration = None, delta=1)
        self.player = Mock()
        self.player.get_health_handler.return_value = Mock()

    def test_apply_effect(self):
        self.power_up.apply_effect(self.player)
        self.player.get_health_handler().heal.assert_called_once()

class PowerUpFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PowerUpFactory()
        self.x = 10
        self.y = 20
        self.width = 5
        self.height = 5
        self.type_area = Entity.TypeArea.POWERUP
        self.delta = 1
    
    def test_create_laser_power_up(self):
        power_up = self.factory.create_power_up(PowerUpType.LASER, self.x, self.y, self.width, self.height, self.type_area, self.delta)
        self.assertIsInstance(power_up, LaserPowerUp)
        self.assertEqual(PowerUpType.LASER, power_up.power_up_type)
        self.assertEqual(self.x, power_up.get_area().get_position_x)
        self.assertEqual(self.y, power_up.get_area().get_position_y)

    def test_create_invulnerability_power_up(self):
        power_up = self.factory.create_power_up(PowerUpType.INVULNERABILITY, self.x, self.y, self.width, self.height, self.type_area, self.delta)
        self.assertIsInstance(power_up, InvulnerabilityPowerUp)
        self.assertEqual(PowerUpType.INVULNERABILITY, power_up.power_up_type)
        self.assertEqual(self.x, power_up.get_area().get_position_x)
        self.assertEqual(self.y, power_up.get_area().get_position_y)

    def test_create_double_fire_power_up(self):
        power_up = self.factory.create_power_up(PowerUpType.DOUBLE_FIRE, self.x, self.y, self.width, self.height, self.type_area, self.delta)
        self.assertIsInstance(power_up, DoubleFirePowerUp)
        self.assertEqual(PowerUpType.DOUBLE_FIRE, power_up.power_up_type)
        self.assertEqual(self.x, power_up.get_area().get_position_x)
        self.assertEqual(self.y, power_up.get_area().get_position_y)

    def test_create_invalid_power_up_type(self):
        with self.assertRaises(ValueError):
            self.factory.create_power_up("INVALID_TYPE", self.x, self.y, self.width, self.height, self.type_area, self.delta)

    def test_create_invalid_area_type(self):
        with self.assertRaises(ValueError):
            self.factory.create_power_up(PowerUpType.LASER, self.x, self.y, self.width, self.height, "INVALID_AREA_TYPE", self.delta)

    def test_create_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            self.factory.create_power_up(PowerUpType.LASER, self.x, self.y, -1, self.height, self.type_area, self.delta)

class PowerUpHandlerTest(unittest.TestCase):
    def setUp(self):
        self.power_up_handler = PowerUpHandlerImpl(None)
        self.player = Mock()
        self.player_status = PlayerStatusImpl(PlayerStatus.Status.NORMAL)
        self.player.get_status.return_value = self.player_status 

    def test_collect_power_up(self):
        invulnerability_power_up = InvulnerabilityPowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.INVULNERABILITY, is_timed=True, duration=10.0, delta=1)
        self.power_up_handler.collect_power_up(invulnerability_power_up, self.player)
        self.assertEqual(self.player_status.status, PlayerStatus.Status.INVULNERABLE)
        self.assertEqual(self.power_up_handler.get_current_power_up(), invulnerability_power_up)

    def test_collect_with_active_power_up(self):
        invulnerability_power_up = InvulnerabilityPowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.INVULNERABILITY, is_timed=True, duration=10.0, delta=1)
        self.power_up_handler.collect_power_up(invulnerability_power_up, self.player)
        self.assertEqual(self.player_status.status, PlayerStatus.Status.INVULNERABLE)

        laser_power_up = LaserPowerUp(x=20, y=20, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.LASER, is_timed=True, duration=10.0, delta=1)
        self.power_up_handler.collect_power_up(laser_power_up, self.player)
        self.assertEqual(self.player_status.status, PlayerStatus.Status.NORMAL)
        self.assertEqual(self.power_up_handler.get_current_power_up(), laser_power_up)

    @patch('pygame.time.get_ticks', side_effect=[1000, 5000])
    def test_timed_power_up(self, mock_get_ticks):
        laser_power_up = LaserPowerUp(x=20, y=20, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.LASER, is_timed=True, duration=3.0, delta=1)
        self.power_up_handler.collect_power_up(laser_power_up, self.player)
        self.assertEqual(self.power_up_handler.get_current_power_up(), laser_power_up)
        self.power_up_handler.player_update(self.player)
        self.assertIsNone(self.power_up_handler.get_current_power_up())

    def test_player_update_with_no_power_up(self):
        self.power_up_handler.player_update(self.player)
        self.assertIsNone(self.power_up_handler.get_current_power_up())


    