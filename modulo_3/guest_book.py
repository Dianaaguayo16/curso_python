with open("guest_book.txt", "a") as file:
    while True:
        name = input("Enter your name (or 'quit'): ")
        if name.lower() == "quit":
            break
        file.write(name + "\n")
        print(f"Welcome, {name}!")
