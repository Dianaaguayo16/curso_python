# 8-14: Cars
def make_car(manufacturer, model, **features):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }
    car.update(features)
    return car

car = make_car("subaru", "outback", color="red", tow_package=True)
print(car)
