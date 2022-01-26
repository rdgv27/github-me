import os
import requests

from utils import load_json, save_json


def get_events_from_api(user: str) -> str:
    """Acessa a api do github e filtra apenas os eventos de Push e Create"""

    # https://docs.github.com/en/rest/reference/activity#events

    # url_profile = f'https://github.com/{user}/'

    url_api = f'https://api.github.com/users/{user}/events'

    token = load_json(os.path.join('data', 'git_token.json'))['token']

    r = requests.get(
        url_api,
        headers={
            'Authorization': f'token {token}',
            'accept': 'application/vnd.github.v3+json'
        }
    )

    data = [
        event
        for event in r.json()
        if event["type"] in ['PushEvent', 'CreateEvent']
    ]  # Verificar quais outros tipos de evento podem ser considerados (Fork, branch, pull request?)

    # Para cada evento transformar a data event["created_at"] em um objeto datetime

    return r.status_code