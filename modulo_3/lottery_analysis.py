from random import sample


attempts = 0
elements = [str(n) for n in range(10)] + list("ABCDE")
my_ticket = ["1", "B", "7", "E"]

while True:
    attempts += 1
    drawn = sample(elements, 4)
    if drawn == my_ticket:
        break

print(f"It took {attempts} attempts to win.")