import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = date(2020, 1, 1)
        current_date = date(2023, 2, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_no_needs_service(self):
        last_service_date = date(2020, 1, 1)
        current_date = date(2022, 2, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
