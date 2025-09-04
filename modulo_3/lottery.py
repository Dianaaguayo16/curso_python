import random

elements = [str(n) for n in range(10)] + list("ABCDE")
winning_ticket = random.sample(elements, 4)
print("Winning ticket:", winning_ticket)

user_ticket = random.sample(elements, 4)
print("Your ticket:", user_ticket)

if user_ticket == winning_ticket:
    print("You win!")
else:
    print("Try again!")
