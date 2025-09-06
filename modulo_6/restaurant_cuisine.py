class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, additional):
        self.number_served += additional
    
    def show_number_served(self):
        print(f"{self.name} has served {self.number_served} customers.")

# Example usage
restaurant = Restaurant("La Casa", "Mexican")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(25)
restaurant.increment_number_served(10)
restaurant.show_number_served()