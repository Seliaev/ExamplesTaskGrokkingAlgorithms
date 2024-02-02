import random


class BoxWithKey():
    """Класс обьекта коробки со спрятанным ключем"""
    def __init__(self):
        self._box: str = ''
        self._key: str = 'k'
        self._boxes: list = []
        self._secret_space: tuple = None, None
        self._find_space: tuple = None, None
        self.__generate_box()

    def __generate_box(self) -> None:
        """
        Генерация коробок с коробками.
        В какой-то коробке, рандомно, лежит ключ - k
        :return: Возвращает сгенерированный список с коробками
        """
        bool_key = False
        count_box = random.randint(1, 100)
        level = [random.randint(1, 10) for x in range(1, count_box)]
        for i in range(len(level)):
            inner_box = []
            for j in range(level[i]):
                somethink = self._box
                if j != 0:
                    if bool_key is False:
                        somethink = self.__choise_key_or_box()
                        if somethink == self._key:
                            self._secret_space = i, j
                            bool_key = True

                inner_box.append(somethink)
            self._boxes.append(inner_box)

    def __choise_key_or_box(self) -> str:
        """
        Подкладывание в коробку ключа
        :return: строка с ключем или пустой коробкой.
        """
        return random.choices([self._box, self._key], weights=[50, 1])[0]

    def __key_here(self, box: str) -> bool:
        """
        Проверка ключ или пустая коробка
        :box: - строка с пустой коробкой или с ключем
        :return: True в случае нахождения ключа, False в противном случае
        """
        if box == self._key:
            return True
        return False

    def look_for_key(self, box: list, level: int = 0) -> None:
        """
        Рекурсивный поиск ключа в коробках
        :box: list - Список с коробками и вероятным ключем
        :level: int - для подсчета индекса внешнего
        """
        for item in box:
            if item.__class__.__name__ == 'list':
                self.look_for_key(item, level)
                level += 1
            elif item.__class__.__name__ == 'str':
                if self.__key_here(item):
                    self._find_space = level, box.index(item)
                    break

    def get_boxes(self) -> list:
        """Получить список со всеми коробками и вероятным ключем"""
        return self._boxes

    def get_secret_space(self) -> tuple:
        """Получение места, куда был сохранен ключ"""
        return self._secret_space

    def get_find_space(self) -> tuple:
        """Получение места, где был найден ключ"""
        return self._find_space
