

def usual_search(number: int, list_nums: list) -> int or None:
    """
    Обычный, линейный поиск элемента
    :number: int - искомое значение
    :list_nums: list - массив для поиска
    :return: Индекс искомого значения в массиве, в противном случае None
    """
    for i_numbers in list_nums:
        if number == i_numbers:
            return list_nums.index(number)
    return None


def binary_search(number: int, list_nums: list) -> int or None:
    """
    Бинарный поиск элемента
    :number: int - искомое значение
    :list_nums: list - массив для поиска
    :return: Индекс искомого значения в массиве, в противном случае None
    """
    low = 0
    high = len(list_nums)
    while low <= high:
        mid = (low + high) // 2
        try:
            i_numbers = list_nums[mid]
        except IndexError:
            break
        else:
            if i_numbers == number:
                return list_nums.index(number)
            elif i_numbers > number:
                high = mid - 1
            elif i_numbers < number:
                low = mid + 1
    return None


