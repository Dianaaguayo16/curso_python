# 3-11: Intentional Error
languages = ["Python", "JavaScript", "C++"]

# Intentional index error
# print(languages[5])  # This will cause IndexError: list index out of range

# Corrected version
print("Corrected access:", languages[2])  # Accessing the last valid index