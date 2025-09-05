# 6-6: Polling
favorite_languages = {
    "ana": "python",
    "luis": "java",
    "maría": "c++"
}

people_to_poll = ["ana", "maría", "diana", "airi"]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thanks for responding, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll!")
