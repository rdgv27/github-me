import json
from typing import Any
from pathlib import Path


def save_json(data: Any, file_name: str) -> None:

    with open(
        file_name,
        'w',
        encoding='utf-8'
    ) as outfile:
        json.dump(data, outfile)


def get_github_auth_token(file: str = None) -> str:
    """Return the authenticaiton token.

    If the file location is `None`, than the default location is used.

    Args:
        file_location: A str containing the location
    """

    if file is None:
        file_path = (Path(__file__).parent.parent / 'data/git_token.json').resolve()
    else:
        file_path = Path(file)

    if file_path.exists():

        with open(
            file_path.resolve(),
            'r',
            encoding='utf-8'
        ) as infile:
            json_token = json.load(infile)

        token = json_token.get('token', None)

        if token:
            return token
        else:
            raise json.JSONDecodeError(
                'It was not possible to read the Authentication JSON file. Are you sure it is correctly formated?'
            )

    else:
        raise FileNotFoundError('The token file is not in the expected location. Are you sure you setup it?')
