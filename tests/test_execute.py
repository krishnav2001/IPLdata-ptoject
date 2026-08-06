import sys
import os
import unittest

# ensure src is on path
HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, os.pardir))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

import matches_played
import matches_won
import extra_runs
import top_economy

DATA_DIR = os.path.join(ROOT, "data")
MOCK_MATCHES = os.path.join(DATA_DIR, "mock_matches.csv")
MOCK_DELIVERIES = os.path.join(DATA_DIR, "mock_deliveries.csv")

class TestExecuteFunctions(unittest.TestCase):

    def test_matches_played(self):
        result = matches_played.execute(MOCK_MATCHES)

        expected = {
            '2015': {'TeamA': 2, 'TeamB': 1, 'TeamC': 1},
            '2016': {'TeamB': 1, 'TeamC': 1, 'TeamD': 1, 'TeamA': 1},
            '2017': {'TeamA': 1, 'TeamD': 1}
        }

        self.assertEqual(result, expected)

    def test_matches_won(self):
        result = matches_won.execute(MOCK_MATCHES)

        expected = {
            '2015': {'TeamA': 1, 'TeamC': 1},
            '2016': {'TeamB': 1, 'TeamD': 1},
            '2017': {'TeamA': 1}
        }

        self.assertEqual(result, expected)

    def test_extra_runs_2016(self):
        result = extra_runs.execute(MOCK_DELIVERIES, MOCK_MATCHES)

        expected = {
            'TeamC': 3,
            'TeamA': 0
        }

        self.assertEqual(result, expected)

    def test_top_economy_2015(self):
        result = top_economy.execute(MOCK_DELIVERIES, MOCK_MATCHES)

        expected = {
            'BowlerB': 0.0,
            'BowlerD': 0.0,
            'BowlerA': 15.0,
            'BowlerC': 15.0
        }

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
