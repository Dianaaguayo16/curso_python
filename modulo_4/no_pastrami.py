# 7-9: No Pastrami
sandwich_orders = ["tuna", "pastrami", "chicken", "pastrami", "egg", "pastrami"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

# Remove all pastrami sandwiches
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Process remaining sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
