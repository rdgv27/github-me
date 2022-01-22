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

    def test_request_profile(self) -> None:

        from scraping import request_profile

        # Given
        user = 'rdgv27'

        self.assertEqual(request_profile(user), user)


if __name__ == '__main__':
    unittest.main()
