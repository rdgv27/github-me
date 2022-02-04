import sys
import unittest
from pathlib import Path


class TestScraping(unittest.TestCase):

    def setUp(self) -> None:
        sys.path.insert(
            0,
            str(((Path(__file__).parent.parent) / 'src').resolve())
        )

    def test_get_events_from_api(self) -> None:

        from scraping import get_events_from_api

        user = 'rdgv27'
        self.assertIsInstance(get_events_from_api(user), list)
        self.assertRaises(ConnectionRefusedError, get_events_from_api, 'notavalidusername_56sa4d65sa46d5s')


if __name__ == '__main__':
    unittest.main()
