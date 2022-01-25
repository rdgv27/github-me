import requests


def get_events_from_api(user: str) -> str:
    """Acessa a api do github e filtra apenas os eventos de Push e Create"""

    # https://docs.github.com/en/rest/reference/activity#events

    # url_profile = f'https://github.com/{user}/'

    # Verificar como fazer a autenticação para pegar os eventos privados

    url_api = f'https://api.github.com/users/{user}/events'

    r = requests.get(
        url_api,
        headers={'accept': 'application/vnd.github.v3+json'}
    )

    data = [
        event
        for event in r.json()
        if event["type"] in ['PushEvent', 'CreateEvent']
    ]  # Verificar quais outros tipos de evento podem ser considerados (Fork, branch, pull request?)

    # Para cada evento transformar a data event["created_at"] em um objeto datetime

    return r.status_code