class DevideAndRule:
    """Поиск максимального размера квадрата, при разделении поля"""
    def __init__(self, field=(1680, 640)):
        """Инициализация обьекта"""
        self._field: tuple = field
        self._max_sq: int = 0
        self.find_sq(self._field)

    def find_sq(self, field: tuple) -> None:
        """Рекурсионная функция поиска размера квадрата"""
        temp_size_min = min(field)
        temp_size_max = max(field)
        if temp_size_max % temp_size_min == 0:
            self._max_sq = temp_size_min
        else:
            smallest_field = (temp_size_min, (temp_size_max % temp_size_min))
            self.find_sq(smallest_field)

    def get_max_sq(self) -> int:
        """Получение размера квадрата"""
        return self._max_sq

