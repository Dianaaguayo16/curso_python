word = input("Your favorite word: ").lower()

try:
    with open("gutenberg_text.txt", encoding="utf-8") as file:
        content = file.read().lower()
        count = content.count(word)
        print(f"'{word}' appears {count} times.")
except FileNotFoundError:
    print("Sorry, the file 'gutenberg_text.txt' was not found.")
except UnicodeDecodeError:
    print("Sorry, there was an encoding issue with the file.")
