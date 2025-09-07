# 8-13: User Profile
def build_profile(first, last, **info):
    profile = {
        "first_name": first,
        "last_name": last
    }
    profile.update(info)
    return profile

my_profile = build_profile(
    "Diana", "Aguayo",
    location="Ciudad Guzmán",
    field="STEM",
    hobby="coding"
)

print(my_profile)