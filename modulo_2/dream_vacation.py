# 7-10: Dream Vacation
responses = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != "yes":
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")