import unittest

from Chapter_7.dijkstra_algorithm import Node, DijkstraAlgorithm


class TestChapterSeven(unittest.TestCase):
    def setUp(self):
        self.start = Node('start')
        self.a = Node('a')
        self.b = Node('b')
        self.finish = Node('finish')

        self.start.add_edge(node=self.a, weight=6)
        self.start.add_edge(node=self.b, weight=2)
        self.b.add_edge(node=self.a, weight=3)
        self.b.add_edge(node=self.finish, weight=5)
        self.a.add_edge(node=self.b, weight=3)
        self.a.add_edge(node=self.finish, weight=1)

        self.da = DijkstraAlgorithm()
        self.da.add_node(self.start)
        self.da.add_node(self.finish)

    def test_result_finish_dijkstra(self):
        self.da.main()
        result_finish = self.da.get_result()[self.finish]
        self.assertEqual(result_finish, 6)


if __name__ == '__main__':
    unittest.main()
