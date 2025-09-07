# 8-8: User Albums
def make_album(artist, title):
    return {"artist": artist, "title": title}

while True:
    print("\nEnter album info (or type 'quit' to exit):")
    artist = input("Artist: ")
    if artist.lower() == "quit":
        break
    title = input("Album Title: ")
    if title.lower() == "quit":
        break

    album = make_album(artist, title)
    print("Album created:", album)