import unittest
from search import *


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        arr = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

        cases = [
            {
                'name': 'Element is present in the middle array',
                'target': 2.0,
                'expected': (1, 2.0)
            },
            {
                'name': 'Element is present not in the middle array',
                'target': 0.5,
                'expected': (2, 0.5)
            },
            {
                'name': 'Element is not present in the array',
                'target': 2.2,
                'expected': (3, 2.5)
            },
            {
                'name': 'Element is smaller than all elements in the array',
                'target': 0.05,
                'expected': (3, 0.1)
            },
            {
                'name': 'Element is larger than all elements in the array',
                'target': 5.0,
                'expected': (4, None)
            },
        ]

        for case in cases:
            with self.subTest(case=case['name']):
                actual = binary_search(arr, case['target'])
                self.assertEqual(case['expected'], actual)


if __name__ == '__main__':
    unittest.main()
