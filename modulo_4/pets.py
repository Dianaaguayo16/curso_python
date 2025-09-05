# 6-8: Pets
pet1 = {"animal": "dog", "owner": "Juan"}
pet2 = {"animal": "cat", "owner": "María"}
pet3 = {"animal": "giraffe", "owner": "Diana"}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nPet Info:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")