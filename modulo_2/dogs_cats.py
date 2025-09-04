filenames = ["cats.txt", "dogs.txt"]

for file in filenames:
    try:
        with open(file) as f:
            print(f"\nContents of {file}:")
            print(f.read())
    except FileNotFoundError:
        print(f"Sorry, {file} not found.")
