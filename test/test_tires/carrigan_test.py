import unittest

from tires.tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [1, 0.9, 0.5, 0]
        tire = CarriganTire(sensor_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_array = [0.2, 0.8, 0.5, 0]
        tire = CarriganTire(sensor_array)
        self.assertFalse(tire.needs_service())