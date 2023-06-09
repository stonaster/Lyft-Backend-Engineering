from battery.battery import Battery
from utils import service_date


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.criteria = 3

    def needs_service(self):
        return service_date(self.last_service_date, self.criteria) <= self.current_date

