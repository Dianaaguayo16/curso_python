# 3-10: Every Function
languages = ["Python", "JavaScript", "C++", "Rust", "Go"]

print("Original list:")
print(languages)

# Accessing elements
print("First language:", languages[0])

# Adding elements
languages.append("TypeScript")
print("After append:", languages)

# Inserting elements
languages.insert(2, "Java")
print("After insert:", languages)

# Removing elements
languages.remove("C++")
print("After remove:", languages)

# Popping elements
popped = languages.pop()
print(f"Popped: {popped}")
print("After pop:", languages)

# Sorting
languages.sort()
print("Sorted:", languages)

# Reversing
languages.reverse()
print("Reversed:", languages)

# Length
print("Total languages:", len(languages))
