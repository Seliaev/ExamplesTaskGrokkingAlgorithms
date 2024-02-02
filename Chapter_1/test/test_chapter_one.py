import unittest

from Chapter_1.main import usual_search, binary_search


class TestChapterOne(unittest.TestCase):
    def setUp(self):
        self.list_nums = [x for x in range(100000000)]
        self.number = 59999

    def test_usual_search(self):
        result_funcion = usual_search(self.number, self.list_nums)
        self.assertEqual(result_funcion, self.number)

    def test_binary_search(self):
        result_funcion = binary_search(self.number, self.list_nums)
        self.assertEqual(result_funcion, self.number)


if __name__ == '__main__':
    unittest.main()
