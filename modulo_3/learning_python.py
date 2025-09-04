with open("learning_python.txt", "w") as file:
    file.write("In Python you can automate tasks.\n")
    file.write("In Python you can build web apps.\n")
    file.write("In Python you can analyze data.\n")

# Read entire file
with open("learning_python.txt") as file:
    content = file.read()
print("Full content:\n", content)

# Read line by line
print("\nLine by line:")
with open("learning_python.txt") as file:
    for line in file:
        print(line.strip())