from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        for wear_value in self.tire_wear:
            if wear_value >= 0.9:
                return True
        return False
