from unittest import TestCase

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort
from shell_sort import sell_sort


class Test(TestCase):
    def test(self):
        for target in (
                ([]),
                ([2, 1]),
                ([3, 2, 1]),
                ([2, 2, 3, 5, 4]),
                ([5, 6, 4, 1, 3, 8, 7, 9]),
                ([2, 5, 6, 7, 3, 2, 8, 1]),
        ):
            with self.subTest(target=target):
                expected = sorted(target)
                self.assertEqual(expected, bubble_sort(target))
                self.assertEqual(expected, selection_sort(target))
                self.assertEqual(expected, insertion_sort(target))
                self.assertEqual(expected, merge_sort(target))
                self.assertEqual(expected, sell_sort(target))
                self.assertEqual(expected, quick_sort(target))
