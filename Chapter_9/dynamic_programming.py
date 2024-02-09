def longest_common_substring(word_a: str, word_b: str) -> int:
    """
    Пример алгоритма динамического программирования
    Поиск самой длинной последовательности символов из двух слов.
    :word_a: str Первое слово
    :word_b: str Второе слово
    :return: Число максимальной длины
    """
    size_word_a, size_word_b = len(word_a), len(word_b)
    cell = [[0] * (size_word_b + 1) for _ in range(size_word_a + 1)]
    max_len_substring = 0
    for i_index in range(1, size_word_a + 1):
        for j_index in range(1, size_word_b + 1):
            if word_a[i_index - 1] == word_b[j_index - 1]:
                cell[i_index][j_index] = cell[i_index - 1][j_index - 1] + 1
                max_len_substring = max(max_len_substring, cell[i_index][j_index])
    return max_len_substring


if __name__ == "__main__":
    word_a = "hish"
    word_b = "hish"
    result = longest_common_substring(word_a, word_b)
    print(result)
