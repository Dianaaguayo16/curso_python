# 4-12: More Loops
foods = ["tacos", "sushi", "pasta", "takoyaki"]

print("My favorite foods are:")
for food in foods:
    print(food)

friend_foods = foods[:]
friend_foods.append("pizza")

print("\nMy friend’s favorite foods are:")
for food in friend_foods:
    print(food)
    