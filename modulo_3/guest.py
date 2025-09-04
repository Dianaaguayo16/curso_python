name = input("What's your name? ")

with open("guest.txt", "w") as file:
    file.write(name)
