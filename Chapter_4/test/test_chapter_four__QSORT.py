import unittest
from random import shuffle

from Chapter_4.quick_sort import recursion_quick_sort

class TestChapterThree_QSORT(unittest.TestCase):
    def setUp(self):
        self.source_list = [x for x in range(1, 100)]
        self.base_list = self.source_list[:]
        shuffle(self.source_list)

    def test_list_eq(self):
        result_list = recursion_quick_sort(self.source_list)
        self.assertListEqual(self.base_list, result_list)

    def test_list_not_eq(self):
        self.assertNotEqual(self.base_list, self.source_list)


if __name__ == '__main__':
    unittest.main()
