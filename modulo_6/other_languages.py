import requests

languages = ["JavaScript", "Ruby", "C", "Java", "Perl", "Haskell", "Go"]

for language in languages:
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    response = requests.get(url)
    data = response.json()
    print(f"\nTop {language} Repos:")
    for repo in data["items"][:5]:
        print(f"{repo['name']} - ⭐ {repo['stargazers_count']}")
