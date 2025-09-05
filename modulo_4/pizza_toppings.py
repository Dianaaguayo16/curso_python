# 7-4: Pizza Toppings
print("Enter pizza toppings (type 'quit' to finish):")

while True:
    topping = input("Topping: ")
    if topping.lower() == "quit":
        break
    print(f"Adding {topping} to your pizza.")
