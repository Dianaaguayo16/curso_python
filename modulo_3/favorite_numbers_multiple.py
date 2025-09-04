# 6-10: Favorite Numbers (Multiple)
favorite_numbers = {
    "Ana": [1, 14],
    "Luis": [3, 6],
    "Diana": [7, 16, 21]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers:")
    for number in numbers:
        print(f"- {number}")