import math


def euclidean_distance(point_a: int, point_b: int) -> float:
    """
    Вычисление Евклидова расстояния между двумя точками
    :point_a: координата точки А
    :point_b: координата точки В
    :return:  квадратный корень из суммы квадратов разностей точек
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point_a, point_b)))


def k_nearest_neighbors(training_set: list, test_instance: list, k: int) -> list:
    """
    Поиск k ближайших соседей
    :training_set: list набор обучающих данных
    :test_instance: list тестовый экземпляр
    :k: int количество ближайщих соседей
    :return: Список с данными ближайших соседей
    """
    distances = [(train_point, euclidean_distance(test_instance, train_point[0]))
                 for train_point in training_set]
    sorted_distances = sorted(distances, key=lambda x: x[1])
    neighbors = [point[0] for point in sorted_distances[:k]]
    return neighbors


if __name__ == "__main__":
    training_set = [([1, 2], 'A'),
                    ([4, 5], 'B'),
                    ([7, 8], 'C'),
                    ([3, 6], 'D')]

    test_instance = [1, 7]

    k_value = 2

    nearest_neighbors = k_nearest_neighbors(training_set, test_instance, k_value)
    print("Ближайшие соседи:", nearest_neighbors)
