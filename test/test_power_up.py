import unittest
from Avian_Blasters.model.area import Area
from Avian_Blasters.model.area_impl import AreaImpl
from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.item.power_up.power_up import PowerUpType
from Avian_Blasters.model.item.power_up.power_up_impl import PowerUpImpl

class DummyPowerUp(PowerUpImpl):
    def apply_effect(self, player):
        pass

class TestPowerUp(unittest.TestCase):
    def setUp(self):
        self.power_up = DummyPowerUp(x=10, y=10, width=4, height=4, type=Entity.TypeArea.POWERUP, power_up_type=PowerUpType.LASER, delta=1)

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