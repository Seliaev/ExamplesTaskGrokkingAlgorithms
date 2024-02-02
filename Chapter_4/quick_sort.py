
def recursion_quick_sort(num_list: list) -> list:
    """
    Рекурсионная функция быстрой сортировки списка - O(n log n)
    :num_list: list - неотсортированный список
    :return: - отсортированный список
    """
    if len(num_list) < 2:
        return num_list
    else:
        mid_index = len(num_list) // 2
        mid = num_list[mid_index]
        left = [i for i in num_list if i < mid]
        right = [i for i in num_list if i > mid]
        return recursion_quick_sort(left) + [mid] + recursion_quick_sort(right)

