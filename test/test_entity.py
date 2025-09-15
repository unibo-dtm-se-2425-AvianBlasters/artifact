import unittest

from Avian_Blasters.model.entity import Entity
from Avian_Blasters.model.entity_impl import EntityImpl

class TestEntity(unittest.TestCase):
    x = 0
    y = 0
    width = 10
    height = 10
    type = Entity.TypeArea.PLAYER
    delta = 1

    def setUp(self):
        self.entity = EntityImpl(self.x, self.y, self.width, self.height, self.type, self.delta)
    
    def test_set_up(self):
        self.assertEqual(self.x, self.entity.get_area().get_position_x)
        self.assertEqual(self.y, self.entity.get_area().get_position_y)
        self.assertEqual(self.width, self.entity.get_area().width)
        self.assertEqual(self.height, self.entity.get_area().height)
        self.assertEqual(self.type, self.entity.get_type)
        self.assertEqual(self.delta, self.entity.delta)
    
    def test_wrong_set_up(self):
        with self.assertRaises(ValueError):
            EntityImpl(self.x, self.y, self.width, self.height, "Hello", self.delta)
        
        with self.assertRaises(ValueError):
            EntityImpl(self.x, self.y, self.width, self.height, self.type, 0.5)
        
    def test_setter_delta(self):
        self.entity.delta = self.delta * 2
        self.assertEqual(self.delta * 2, self.entity.delta)
        
        # Verify that selecting a non int delta, does not change the current one
        with self.assertRaises(Exception):
            self.entity.delta = self.delta / 3
        self.assertEqual(self.delta * 2, self.entity.delta)
    
    def test_overlap(self):
        # Test if the overlap functionality works as intended
        self.assertTrue(self.entity.is_touched(self.entity))
        
        entity2 = EntityImpl(self.x + int(self.width * 1.5), self.y + int(self.height * 1.5), self.width, self.height, self.type, self.delta)
        self.assertFalse(self.entity.is_touched(entity2))
        
        entity3 = EntityImpl(self.x + int(self.width / 2), self.y + int(self.width / 2), self.width, self.height, self.type, self.delta)
        self.assertTrue(self.entity.is_touched(entity3))

        entity4 = EntityImpl(self.x + self.width, self.y + self.height, self.width, self.height, self.type, self.delta)
        self.assertFalse(self.entity.is_touched(entity4))

        with self.assertRaises(ValueError):
            self.entity.is_touched(self.x)
    
    def test_movement(self):
        # Verify that entity moves as envisioned and it can handle wrong inputs
        self.entity.move(self.delta, self.delta, self.width, self.height)
        self.assertEqual(self.x + self.delta * self.delta, self.entity.get_area().get_position_x)
        self.assertEqual(self.y + self.delta * self.delta, self.entity.get_area().get_position_y)
        self.assertEqual(self.width, self.entity.get_area().width)
        self.assertEqual(self.height, self.entity.get_area().height)

        self.entity.move(-self.delta, -self.delta, self.width, self.height)
        self.test_set_up()

        with self.assertRaises(ValueError):
            self.entity.move(self.x, self.y, "Hello", self.height)
        
        with self.assertRaises(ValueError):
            self.entity.move(self.x, self.y, self.width, 5.34)
        