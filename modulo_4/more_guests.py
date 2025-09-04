# 3-6: More Guests
guest_list = ["Ada Lovelace", "Alan Turing", "Marie Curie"]

print("\nGreat news! I found a bigger dinner table!")

# Add guests
guest_list.insert(0, "Grace Hopper")           # Beginning
guest_list.insert(2, "Katherine Johnson")      # Middle
guest_list.append("Stephen Hawking")           # End

# New invitations
for guest in guest_list:
    print(f"Dear {guest}, you're invited to dinner at my place!")
