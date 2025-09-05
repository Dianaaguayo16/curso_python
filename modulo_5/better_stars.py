from random import randint

# Replace the grid loop with randomness
stars = []
for _ in range(100):  # Create 100 stars
    x = randint(0, 760)  # Adjust for star width
    y = randint(0, 560)  # Adjust for star height
    stars.append(Star(screen, x, y))
