from cities import city_country

def test_city_country_population():
    result = city_country("santiago", "chile", 5000000)
    assert result == "Santiago, Chile - population 5000000"
    print("Test passed: city_country with population works correctly!")

def test_city_country_no_population():
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"
    print("Test passed: city_country without population works correctly!")

if __name__ == "__main__":
    test_city_country_population()
    test_city_country_no_population()
    print("All tests passed!")