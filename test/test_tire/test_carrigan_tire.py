import unittest

from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service(self):
        tire_wear = [0.3, 0.6, 0.9, 1.2]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_no_needs_service(self):
        tire_wear = [0.3, 0.3, 0.5, 0.6]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()
