# 4-13: Buffet

# Original menu stored as a tuple
menu = ("rice", "beans", "chicken", "salad", "bread")

print("Original buffet menu:")
for item in menu:
    print(f"- {item}")

# Attempt to modify an item (this will raise an error if uncommented)
# menu[0] = "pasta"  # ❌ Tuples are immutable

# Revised menu with two items changed
menu = ("pasta", "beans", "chicken", "salad", "fruit")

print("\nRevised buffet menu:")
for item in menu:
    print(f"- {item}")