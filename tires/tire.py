from abc import ABC

class Tire(ABC):
    def needs_service(self):
        pass 

class CarriganTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        for i in self.sensor_array:
            if i > 0.9:
                return True
        return False

    
class OctoprimeTire(Tire):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        return sum(self.sensor_array) >= 3