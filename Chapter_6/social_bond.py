class SocialBond:
    """Класс обьекта социальных связей"""

    def __init__(self):
        """Задаются пользователи, их связи, на основе всего этого строится граф в виде словаря"""
        self._names = ["me", "alice", "bob", "marta", "claire", "anuj", "peggy", "thom"]
        self._bonds = [(self._names[0], self._names[1]), (self._names[0], self._names[2]), (self._names[0], self._names[3]),
                       (self._names[1], self._names[4]), (self._names[1], self._names[5]),
                       (self._names[2], self._names[5]), (self._names[2], self._names[6]),
                       (self._names[3], self._names[7])
                       ]
        self._graph = {}
        self.__full_graph()

    def __full_graph(self) -> None:
        """Заполнение графа данными"""
        for name in self._names:
            self._graph[name] = []
        for bond in self._bonds:
            self._graph[bond[0]].append(bond[1])

    def get_graph(self) -> dict:
        """Получение графа"""
        return self._graph
