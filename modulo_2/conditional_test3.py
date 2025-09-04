 # 7-6c: Using break
while True:
    topping = input("Enter a topping (or 'quit'): ")
    if topping == "quit":
        break
    print(f"Adding {topping} to your pizza.")