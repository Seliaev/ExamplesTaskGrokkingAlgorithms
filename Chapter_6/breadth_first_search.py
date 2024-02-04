from collections import deque



def need_person(name: str, letter: str) -> bool:
    """
    Проверка условия, начальная буква имени
    :name: str - проверяемое имя
    :letter: str - искомая буква
    :return: При нахождении True, в противном False
    """
    try:
        if len(letter) == 1:
            return letter is name[0]
        else:
            raise SyntaxError
    except SyntaxError as se:
        print("Длина параметра 'letter' должна быть равна 1")
        exit()


def fun_deque(graph: dict, letter: str) -> bool:
    """
    Алгоритм поиска в ширину.
    ---
    Создание очереди для проверки
    :graph: dict - граф в виде словаря
    :letter: str - искомое значение, потребуется для другой функции
    :return: При нахождении True, в противном False
    """
    search_queue = deque()
    search_queue += graph['me']
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if need_person(person, letter):
                # print(f"This is person with name - {person}")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == "__main__":
    from social_bond import SocialBond
    sb = SocialBond()
    print(fun_deque(graph=sb.get_graph(), letter='a'))
