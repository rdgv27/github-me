import os
import requests
from datetime import timezone
from datetime import datetime

from utils import load_json


def get_events_from_api(user: str) -> str:
    """Acessa a api do github e filtra apenas os eventos de Push e Create"""

    # https://docs.github.com/en/rest/reference/activity#events

    # url_profile = f'https://github.com/{user}/'

    EVENT_TYPES = ['PushEvent', 'CreateEvent', 'PullRequestEvent', 'ForkEvent']

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
        if event["type"] in EVENT_TYPES
    ]

    for event in data:
        event['created_at'] = datetime.fromisoformat(event['created_at'][:-1]).astimezone(timezone.utc)

    return r.status_code