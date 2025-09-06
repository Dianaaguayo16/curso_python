# 3-8: Seeing the World
places = ["Kyoto", "Osaka", "Machu Picchu", "Cairo", "Venice"]

print("Original list:")
print(places)

print("\nAlphabetical order (using sorted):")
print(sorted(places))

print("\nOriginal list again:")
print(places)

print("\nReverse alphabetical order (using sorted):")
print(sorted(places, reverse=True))

print("\nOriginal list again:")
print(places)

print("\nReversed list (using reverse):")
places.reverse()
print(places)

print("\nBack to original order (reverse again):")
places.reverse()
print(places)

print("\nSorted list (using sort):")
places.sort()
print(places)

print("\nSorted in reverse order (using sort with reverse=True):")
places.sort(reverse=True)
print(places)