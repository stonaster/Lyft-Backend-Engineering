from engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.criteria = 30_000

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 30_000



