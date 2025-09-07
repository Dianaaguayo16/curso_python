import json

def get_stored_username():
    try:
        with open("username.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("Enter your name: ")
    with open("username.json", "w") as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        confirm = input(f"Are you {username}? (yes/no) ")
        if confirm.lower() == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you, {username}!")

greet_user()
