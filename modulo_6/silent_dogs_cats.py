filenames = ["cats.txt", "dogs.txt"]

for file in filenames:
    try:
        with open(file) as f:
            print(f.read())
    except FileNotFoundError:
        pass  # Silent fail
