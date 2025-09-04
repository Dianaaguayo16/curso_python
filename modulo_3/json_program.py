import json

filename = "favorite_number.json"
number = input("What's your favorite number? ")

try:
    with open(filename, "w") as f:
        json.dump(number, f)
    print(f"Your favorite number {number} has been saved!")
    
    with open(filename) as f:
        loaded_number = json.load(f)
    print(f"I know your favorite number! It's {loaded_number}.")
except FileNotFoundError:
    print(f"Sorry, couldn't create or access {filename}.")
except json.JSONDecodeError:
    print("Sorry, there was an issue with the JSON data.")