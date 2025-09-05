import requests

def check_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Status code is 200: Success")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except Exception as e:
        print(f"Other error: {e}")

# Valid request
check_status("https://api.github.com/search/repositories?q=language:python&sort=stars")

# Invalid request
check_status("https://api.github.com/search/repositories?q=language:nonexistentlang&sort=stars")
