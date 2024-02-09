import unittest

from Chapter_9.dynamic_programming import longest_common_substring


class TestChapterNine(unittest.TestCase):
    def setUp(self):
        self.word_a = "hish"
        self.word_b = "fish"
        self.correct_answer = 3
        self.wrong_answer = 2

    def test_result_len_substing(self):
        result = longest_common_substring(self.word_a, self.word_b)
        self.assertEqual(result, self.correct_answer)

    def test_wrong_result_len_substing(self):
        result = longest_common_substring(self.word_a, self.word_b)
        self.assertNotEqual(result, self.wrong_answer)


if __name__ == '__main__':
    unittest.main()
