# 7-6b: Active variable
active = True
while active:
    topping = input("Enter a topping (or 'quit'): ")
    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping} to your pizza.")