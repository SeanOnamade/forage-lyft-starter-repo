from car import Serviceable
import datetime

class Battery(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        pass 

class NubbinBattery(Battery):
    def __init__(self, last_service_date, service_threshold_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        

    def needs_service(self):
        return self.service_threshold_date < datetime.today().date()
    

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, service_threshold_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        

    def needs_service(self):
        return self.service_threshold_date < datetime.today().date()