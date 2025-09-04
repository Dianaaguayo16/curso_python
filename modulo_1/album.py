# 8-7: Album
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album("Adele", "30"))
print(make_album("Laufey", "Lovergirl"))
print(make_album("Imagine Dragons", "Origins", songs=12))
