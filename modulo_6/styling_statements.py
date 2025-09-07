# Styled version of 5-8
usernames = ["admin", "jaden", "luna", "mario", "sofia"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
