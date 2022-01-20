import requests


def request_profile(user: str) -> str:

    url_profile = f'https://github.com/{user}/'

    r = requests.get(url_profile)

    return r.content