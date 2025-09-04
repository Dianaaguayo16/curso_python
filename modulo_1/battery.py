class Battery:
    def __init__(self, size=75):
        self.size = size

    def get_range(self):
        if self.size == 75:
            print("Range: 260 miles")
        elif self.size == 100:
            print("Range: 315 miles")

    def upgrade_battery(self):
        if self.size < 100:
            self.size = 100

class ElectricCar:
    def __init__(self, model):
        self.model = model
        self.battery = Battery()

car = ElectricCar("Model S")
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()
git