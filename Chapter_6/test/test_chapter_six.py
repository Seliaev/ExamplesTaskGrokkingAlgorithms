import unittest

from Chapter_6.social_bond import SocialBond
from Chapter_6.breadth_first_search import fun_deque


class TestChapterThreeDAR(unittest.TestCase):
    def setUp(self):
        self.sb = SocialBond()
        self.search_letter = self.sb.get_graph()['alice'][0][0]  # Получаем первую букву имени claire из связи alice
        self.another_letter = 'x'  # буква, которая не попадется.

    def test_BFS_true(self):
        result_funcion = fun_deque(graph=self.sb.get_graph(), letter=self.search_letter)
        self.assertTrue(result_funcion)

    def test_BFS_false(self):
        result_funcion = fun_deque(graph=self.sb.get_graph(), letter=self.another_letter)
        self.assertFalse(result_funcion)


if __name__ == '__main__':
    unittest.main()
