filename = "gutenberg_text.txt"

try:
    with open(filename, encoding="utf-8") as file:
        content = file.read().lower()
        count = content.count(" the ")
        print(f"'the' appears {count} times.")
except FileNotFoundError:
    print(f"Sorry, the file {filename} was not found.")
except UnicodeDecodeError:
    print(f"Sorry, there was an encoding issue with {filename}.")
