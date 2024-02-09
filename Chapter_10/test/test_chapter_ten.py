import unittest

from Chapter_10.neighbors_k import k_nearest_neighbors


class TestChapterTen(unittest.TestCase):
    def setUp(self):
        self.training_set = [([1, 2], 'A'),
                        ([4, 5], 'B'),
                        ([7, 8], 'C'),
                        ([3, 6], 'D')]
        self.test_instance = [1, 7]
        self.k_value = 2
        self.correct_result = [([3, 6], 'D'), ([4, 5], 'B')]
        self.wrong_result = [([1, 1], 'D')]

    def test_result_k_nearest_neighbors(self):
        nearest_neighbors = k_nearest_neighbors(self.training_set, self.test_instance, self.k_value)
        self.assertListEqual(nearest_neighbors, self.correct_result)

    def test_wrong_result_k_nearest_neighbors(self):
        nearest_neighbors = k_nearest_neighbors(self.training_set, self.test_instance, self.k_value)
        self.assertNotEqual(nearest_neighbors, self.wrong_result)


if __name__ == '__main__':
    unittest.main()
