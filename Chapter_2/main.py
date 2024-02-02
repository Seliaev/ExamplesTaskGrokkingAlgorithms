
def find_smallest(any_list: list) -> int:
    """
    Поиск наименьшего значения в списке
    :any_list: list - список
    :return: индекс наименьшего значения
    """
    smallest_index = 0
    smallest = any_list[smallest_index]
    for i in range(1, len(any_list)):
        if any_list[i] < smallest:
            smallest_index = i
            smallest = any_list[smallest_index]
    return smallest_index


def sorting_by_choise(unsorted_list: list) -> list:
    """
    Сортировка выбором
    :any_list: list - неотсортированный список
    :return: отсортированный список
    """
    sorted_list = []
    for i in range(len(unsorted_list)):
        smallest = find_smallest(unsorted_list)
        sorted_list.append(unsorted_list.pop(smallest))
    return sorted_list
