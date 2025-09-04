# 5-2: More Conditional Tests

# Equality and inequality with strings
fruit = "banana"
print("Is fruit == 'banana'? I predict True.")
print(fruit == "banana")

print("Is fruit != 'apple'? I predict True.")
print(fruit != "apple")

print("Is fruit == 'Banana'? I predict False.")
print(fruit == "Banana")

# Using lower()
name = "Diana"
print("Is name.lower() == 'diana'? I predict True.")
print(name.lower() == "diana")

print("Is name.lower() == 'Diana'? I predict False.")
print(name.lower() == "Diana")

# Numerical tests
age = 20
print("Is age == 20? I predict True.")
print(age == 20)

print("Is age != 18? I predict True.")
print(age != 18)

print("Is age > 25? I predict False.")
print(age > 25)

print("Is age >= 20? I predict True.")
print(age >= 20)

print("Is age < 18? I predict False.")
print(age < 18)

# Using and/or
print("Is age > 18 and age < 30? I predict True.")
print(age > 18 and age < 30)

print("Is age < 18 or age > 30? I predict False.")
print(age < 18 or age > 30)

# In a list
fruits = ["banana", "apple", "mango"]
print("Is 'apple' in fruits? I predict True.")
print("apple" in fruits)

print("Is 'grape' not in fruits? I predict True.")
print("grape" not in fruits)