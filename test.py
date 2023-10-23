from unittest import TestCase

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from selection_sort import selection_sort


class Test(TestCase):
    def test(self):
        for target, expected in (
                ([], []),
                ([2, 1], [1, 2]),
                ([3, 2, 1], [1, 2, 3]),
                ([2, 2, 3, 5, 4], [2, 2, 3, 4, 5]),
                ([5, 6, 4, 1, 3, 8, 7, 9], [1, 3, 4, 5, 6, 7, 8, 9]),
        ):
            with self.subTest(target=target, expected=expected):
                self.assertEqual(expected, bubble_sort(target))
                self.assertEqual(expected, selection_sort(target))
                self.assertEqual(expected, insertion_sort(target))
                self.assertEqual(expected, merge_sort(target))
