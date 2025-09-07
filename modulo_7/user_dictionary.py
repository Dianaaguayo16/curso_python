import json

user = {
    "username": input("Username: "),
    "age": input("Age: "),
    "location": input("Location: ")
}

with open("user_data.json", "w") as f:
    json.dump(user, f)

with open("user_data.json") as f:
    data = json.load(f)
    print(f"\nWelcome back, {data['username']}!")
    print(f"Age: {data['age']}, Location: {data['location']}")
