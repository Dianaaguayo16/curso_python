import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        number = json.load(f)
    print(f"I know your favorite number! It's {number}.")
except FileNotFoundError:
    print("I don't know your favorite number yet.")
    number = input("What's your favorite number? ")
    try:
        with open(filename, "w") as f:
            json.dump(number, f)
        print(f"Thanks! I'll remember that {number} is your favorite number.")
    except Exception as e:
        print(f"Sorry, I couldn't save your favorite number: {e}")
except json.JSONDecodeError:
    print("Sorry, there was an issue with the saved data.")
