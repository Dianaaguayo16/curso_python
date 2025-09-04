# 7-5: Movie Tickets
print("Enter your age to see your ticket price (type 'quit' to exit):")

while True:
    age_input = input("Age: ")
    if age_input.lower() == "quit":
        break
    age = int(age_input)
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
