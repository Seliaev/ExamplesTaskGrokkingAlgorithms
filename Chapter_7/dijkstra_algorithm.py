class Node:
    """Класс обьекта узла"""

    def __init__(self, node):
        self.node: str = node
        self.edges: dict = {}

    def add_edge(self, node, weight: int):
        """
        Добавление ребер к узлу
        :node: - узел
        :weight: - вес ребра
        """
        self.edges[node] = weight


class DijkstraAlgorithm:
    """Класс реализации алгоритма Дейкстры"""

    def __init__(self):
        self._infinity = float('inf')
        self._graph: dict = {}
        self._weights: dict = {}
        self._parents: dict = {}
        self._processed: list = []

    def add_node(self, node: Node):
        """
        Добавление узла в граф
        Установка родителей узлов
        Установка веса ребер
        :node: - узел
        """
        self._graph[node] = node.edges
        self.__set_parents(node)
        self.__set_weight(node)

    def __set_parents(self, node: Node):
        """
        Установка родителей узла
        Если узел finish, то его родитель None
        :node: - узел
        """
        if node.node == 'finish':
            self._parents[node] = None
        else:
            for i in node.edges:
                self._parents[i] = node

    def __set_weight(self, node: Node):
        """
        Установка веса ребер
        Если узел finish, то его вес inf
        :node: - узел
        """
        if node.node == 'finish':
            self._weights[node] = self._infinity
        else:
            for node, cost in node.edges.items():
                self._weights[node] = cost

    def __find_lowest_weight_node(self) -> Node:
        """
        Поиск узла с самым низким весом для ребра
        :return: узел с самым низким весом ребра
        """
        lowest_weight = self._infinity
        lowest_weight_node = None
        for key_node in self._weights.keys():
            value_weight = self._weights[key_node]
            if value_weight < lowest_weight and key_node not in self._processed:
                lowest_weight = value_weight
                lowest_weight_node = key_node
        return lowest_weight_node

    def main(self) -> None:
        """
        Основной метод запускающий алгоритм.
        Методом __find_lowest_weight_node находится узел с самым низким весом ребра и возрващает этот узел
        Складываются вес ребра узла с весом ребра соседнего узла, проверяется полученный вес и сохраненный до этого вес
        Если новый вес меньше, он сохраняется.
        Сохраняется новый родитель узла
        """
        node = self.__find_lowest_weight_node()
        while node is not None:
            weight = self._weights[node]
            neighbors = node.edges
            for neighbor, weight_neighbor in neighbors.items():
                new_weight = weight + weight_neighbor
                if neighbor in self._weights and self._weights[neighbor] > new_weight:
                    self._weights[neighbor] = new_weight
                    self._parents[neighbor] = node
            self._processed.append(node)
            node = self.__find_lowest_weight_node()

    def get_result(self):
        """Получение результата суммы веса ребер до финиша для теста"""
        return self._weights

    def print_weights(self):
        """Вывод полученных узлов и весов в удобночитаемом виде"""
        result_for_print = {}
        for node, weight in self._weights.items():
            result_for_print[node.node] = weight
        print(result_for_print)

    def print_parents(self):
        """Вывод полученных узлов и их родителей в удобночитаемом виде"""
        result_for_print = {}
        for cheld, parent in self._parents.items():
            try:
                result_for_print[cheld.node] = parent.node
            except AttributeError:
                result_for_print[cheld.node] = None
        print(result_for_print)


if __name__ == '__main__':
    start = Node('start')
    a = Node('a')
    b = Node('b')
    finish = Node('finish')

    start.add_edge(node=a, weight=6)
    start.add_edge(node=b, weight=2)
    b.add_edge(node=a, weight=3)
    b.add_edge(node=finish, weight=5)
    a.add_edge(node=b, weight=3)
    a.add_edge(node=finish, weight=1)

    da = DijkstraAlgorithm()
    da.add_node(start)
    da.add_node(finish)

    da.print_weights()
    da.print_parents()
    da.main()
    print()
    da.print_weights()
    da.print_parents()

