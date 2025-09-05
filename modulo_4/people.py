# 6-7: People
person1 = {"name": "Ana", "age": 22, "city": "Madrid"}
person2 = {"name": "Louis", "age": 25, "city": "Australia"}

people = [person1, person2]

for person in people:
    print("\nPerson Info:")
    for key, value in person.items():
        print(f"{key.title()}: {value}")
