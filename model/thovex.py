from car import Car

class Thovex(Car):
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()