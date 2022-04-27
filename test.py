import unittest

import numpy as np
from main import score

class TestScore(unittest.TestCase):

    def test_score_works_on_known_values(self):
        count = np.array([
            [0, 2, 0, 1],
            [2, 0, 0, 3],
            [0, 0, 0, 6],
            [1, 3, 6, 0],
        ])
        assignment = [
            [1, 0],
            [2, 3],
        ]
        self.assertEqual(score(count, assignment), 8)

    def test_score_with_one_kid_groups(self):
        count = np.array([
            [1, 0, 0],
            [0, 5, 0],
            [0, 0, 0],
        ])
        assignment = [
            [0], [2], [1]
        ]
        self.assertEqual(score(count, assignment), 6)

if __name__ == '__main__':
    unittest.main()