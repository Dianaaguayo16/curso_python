# 3-7: Shrinking Guest List
guest_list = ["Grace Hopper", "Ada Lovelace", "Katherine Johnson", "Alan Turing", "Marie Curie", "Stephen Hawking"]

print("\nBad news... the new dinner table won't arrive in time. I can only invite two guests.")

# Remove guests until only two remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner this time.")

# Confirm remaining guests
for guest in guest_list:
    print(f"{guest}, you're still invited to dinner!")

# Empty the list
del guest_list[0]
del guest_list[0]

print(f"\nFinal guest list: {guest_list}")  # Should print []
