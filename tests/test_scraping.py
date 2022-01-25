import os
import sys
import unittest
from pathlib import Path


class TestScraping(unittest.TestCase):

    def setUp(self) -> None:
        sys.path.insert(
            0,
            os.path.join(Path(__file__).parent.parent.resolve(), 'src')
        )

    def test_get_events_from_api(self) -> None:

        from scraping import get_events_from_api

        user = 'rdgv27'
        self.assertEqual(get_events_from_api(user), 200)


if __name__ == '__main__':
    unittest.main()
