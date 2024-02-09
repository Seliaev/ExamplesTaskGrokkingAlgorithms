import unittest
import datetime

from Chapter_8.greedy_algorithm import greedy_sorting


class TestChapterEightGreedy(unittest.TestCase):
    def setUp(self):
        self.dt_format = '%H:%M'
        self.start_time_str = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30']
        self.finish_time_str = ['10:00', '10:30', '11:00', '11:30', '12:00', '12:30']
        self.data_unsorted = {
            "start_time_str": [datetime.datetime.strptime(x, self.dt_format).timestamp() for x in self.start_time_str],
            "finish_time_str": [datetime.datetime.strptime(x, self.dt_format).timestamp() for x in
                                self.finish_time_str],
            "lesson": ["Рисование", "Английский", "Математика", "Информатика", "Биология", "Музыка"]
        }

    def test_result_correct(self):
        result_function = greedy_sorting(self.data_unsorted)
        self.assertListEqual(result_function, ['Рисование', 'Математика', 'Биология'])

    def test_result_incorrect(self):
        result_function = greedy_sorting(self.data_unsorted)
        self.assertNotEqual(result_function, ["Биология", "Музыка"])


if __name__ == '__main__':
    unittest.main()
