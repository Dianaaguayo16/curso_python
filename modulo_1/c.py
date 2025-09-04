with open("learning_python.txt") as file:
    for line in file:
        print(line.replace("Python", "C").strip())
