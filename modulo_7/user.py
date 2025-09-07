class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.age}, from {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

u1 = User("Diana", "Aguayo", 22, "Ciudad Guzmán")
u2 = User("Luis", "Torres", 25, "Portugal")

u1.describe_user()
u1.greet_user()
u2.describe_user()
u2.greet_user()
