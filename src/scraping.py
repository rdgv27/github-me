# Utils
import requests
from datetime import timezone, datetime

# Types
from typing import Any

# Errors
from multiprocessing import AuthenticationError

from utils import get_github_auth_token


def get_events_from_api(user: str,
                        event_type: list[str] = [
                            'PushEvent',
                            'CreateEvent',
                            'PullRequestEvent',
                            'ForkEvent'
                        ]) -> list[dict[str, Any]]:
    """Get user events information through the GitHub Events API.

    Only returns events created within the past 90 days. The function will filter the events type based
    on the event name presented in the GitHub Events API. By deafult, the function filters only Push,
    Create Repository, Pull Request and Fork events.

    More datails ca be found in:
        * https://docs.github.com/en/rest/reference/activity
        * https://docs.github.com/en/developers/webhooks-and-events/events/github-event-types

    -----
    Args:
        user: GitHub username.
        event_type: List of event types.

    Returns:
        List of user events created in the last 90 days, filtered by type. Max 100.

    -----
    Raises:
        FileNotFoundError: Happens when the Authentication JSON file is not present in the expected path.
        JSONDecodeError: Happens when the Authentication JSON file is not well formated.
        AuthenticationError: Happens when the Authentication token is invalid/expired.
        ConnectionRefusedError: Happens the username is invalid or when the GitHub server refuses to process your request.
    """

    url_api = f'https://api.github.com/users/{user}/events'

    # Add the Etag to get only new events
    # Maybe I should care about the X-Poll-Interval, but the intention is not request events so frequently
    r = requests.get(
        url_api,
        headers={
            'Authorization': f'token {get_github_auth_token()}',
            'accept': 'application/vnd.github.v3+json'
        }
    )

    if r.status_code == 200:

        data = [
            event for event in r.json()
            if event["type"] in event_type
        ]

        for event in data:
            event['created_at'] = datetime.fromisoformat(event['created_at'][:-1]).astimezone(timezone.utc)

        return data

    elif r.status_code == 304:
        # Status: 304 Not Modified
        return []

    elif r.status_code == 401:
        # Status: 401 Unauthorized
        raise AuthenticationError('Access denied. Please verify your Authentication Token!')

    elif r.status_code == 403:
        # Status: 403 Forbidden
        raise ConnectionRefusedError('The server refused to follow with your request!')

    elif r.status_code == 404:
        # Status: 404 Not Found
        raise ConnectionRefusedError('The server returned "404 Not Found". Are you sure the username is correct?')

    else:
        raise Exception(f'Response: {r.status_code}. The server response was of unknow type.')


# def get_user_info_from_api(user: str ) -> dict[str, Union[str, int]]:
#     """"""
