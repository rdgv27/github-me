import requests


def request_profile(user: str) -> str:

    # Verificar se é possível pegar as informações através da API de eventos
    # https://docs.github.com/en/rest/reference/activity#events

    url_profile = f'https://github.com/{user}/'

    r = requests.get(url_profile)

    return r.content