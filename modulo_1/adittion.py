try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Sum: {a + b}")
except ValueError:
    print("Please enter valid numbers.")