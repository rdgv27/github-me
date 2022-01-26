import json
from typing import Any


def load_json(file_name: str) -> Any:

    with open(
        file_name,
        'r',
        encoding='utf-8'
    ) as infile:
        return json.load(infile)


def save_json(data: Any, file_name: str) -> None:

    with open(
        file_name,
        'w',
        encoding='utf-8'
    ) as outfile:
        json.dump(data, outfile)