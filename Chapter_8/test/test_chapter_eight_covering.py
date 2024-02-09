import unittest

from Chapter_8.covering_set import covering_set


class TestChapterEightCovering(unittest.TestCase):
    def setUp(self):
        self.data_unsorted = {'station_1': ['Москва', 'Санкт-Петербург', 'Владимир'],
                              'station_2': ['Нижний Новгород', 'Москва', 'Тверь'],
                              'station_3': ['Иваново', 'Санкт-Петербург', 'Калуга'],
                              'station_4': ['Санкт-Петербург', 'Владимир'],
                              'station_5': ['Калуга', 'Воронеж']}

    def test_result_correct(self):
        result_function = covering_set(self.data_unsorted)
        self.assertListEqual(result_function, ['station_1', 'station_2', 'station_3', 'station_5'])

    def test_result_incorrect(self):
        result_function = covering_set(self.data_unsorted)
        self.assertNotEqual(result_function, ['station_4', 'station_5'])


if __name__ == '__main__':
    unittest.main()
