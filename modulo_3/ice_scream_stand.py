from restaurant import Restaurant
class IceCreamStand(Restaurant):
    """
    Class IceCreamStand is a subclass of Restaurant that represents an ice cream stand
    with a variety of flavors.
    Attributes:
        name (str): The name of the ice cream stand (inherited from Restaurant).
        cuisine (str): The type of cuisine offered (inherited from Restaurant).
        flavors (list): A list of strings representing the available ice cream flavors.
    Methods:
        show_flavors():
            Prints the available ice cream flavors in a formatted list.
    """
    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors

    def show_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

stand = IceCreamStand("Sweet Freeze", "Dessert", ["vanilla", "chocolate", "mango"])
stand.show_flavors()
