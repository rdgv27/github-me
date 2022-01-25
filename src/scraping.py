import requests


def get_events_from_api(user: str) -> str:

    # Verificar se é possível pegar as informações através da API de eventos
    # https://docs.github.com/en/rest/reference/activity#events

    # url_profile = f'https://github.com/{user}/'

    url_api = f'https://api.github.com/users/{user}/events'

    r = requests.get(
        url_api,
        headers={'accept': 'application/vnd.github.v3+json'}
    )

    data = [
        event
        for event in r.json()
        if event["type"] in ['PushEvent', 'CreateEvent']
    ]

    return r.status_code
