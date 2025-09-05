from user import User


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges(["can add post", "can delete post", "can ban user"])

admin = Admin("Diana", "Aguayo", 22, "Ciudad Guzmán")
admin.privileges.show_privileges()