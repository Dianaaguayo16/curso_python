class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("La Diana", "Fusion")
print(restaurant.number_served)

restaurant.number_served = 20
print(restaurant.number_served)

restaurant.set_number_served(50)
print(restaurant.number_served)

restaurant.increment_number_served(30)
print(restaurant.number_served)