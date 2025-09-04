# 7-6a: Conditional test in while
topping = ""
while topping != "quit":
    topping = input("Enter a topping (or 'quit'): ")
    if topping != "quit":
        print(f"Adding {topping} to your pizza.") 