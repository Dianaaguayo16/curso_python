while True:
    try:
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"Sum: {a + b}")
    except ValueError:
        print("Invalid input. Try again.")