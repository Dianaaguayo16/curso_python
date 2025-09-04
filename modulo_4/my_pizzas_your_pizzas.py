# 4-11: My Pizzas, Your Pizzas
pizzas = ["pepperoni", "hawaiian", "bbq chicken"]
friend_pizzas = pizzas[:]

pizzas.append("meat lovers")
friend_pizzas.append("veggie")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)