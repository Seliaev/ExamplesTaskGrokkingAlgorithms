import unittest

from Chapter_2.main import sorting_by_choise


class TestChapterTwo(unittest.TestCase):
    def setUp(self):
        self.list_nums = [x for x in range(1)]
        self.reversed_list_nums = [x for x in reversed(self.list_nums)]

    def test_sorting_by_choise(self):
        result_funcion = sorting_by_choise(self.reversed_list_nums)
        self.assertEqual(result_funcion, self.list_nums)


if __name__ == '__main__':
    unittest.main()
