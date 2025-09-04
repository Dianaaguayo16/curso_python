# 6-11: Cities

def city_country(city, country, population=None):
    """Return a formatted string with city and country information."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

cities = {
    "kyoto": {
        "country": "japan",
        "population": "1.5 million",
        "fact": "Known for its temples and gardens."
    },
    "venice": {
        "country": "italy",
        "population": "260,000",
        "fact": "Built on canals."
    },
    "reykjavik": {
        "country": "iceland",
        "population": "130,000",
        "fact": "One of the cleanest cities in the world."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")

# Test the function
print(f"\nTest: {city_country('santiago', 'chile', 5000000)}")
