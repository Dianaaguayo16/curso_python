# 3-5: Changing Guest List
guest_list = ["Ada Lovelace", "Nikola Tesla", "Marie Curie"]

# Tesla can't make it
print(f"\nUnfortunately, {guest_list[1]} can't make it to dinner.")

# Replace Tesla with Alan Turing
guest_list[1] = "Alan Turing"

# New invitations
for guest in guest_list:
    print(f"Dear {guest}, you're still invited to dinner!")
