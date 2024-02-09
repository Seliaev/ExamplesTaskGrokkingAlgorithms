def covering_set(data: dict):
    """
    Жадный алгоритм для решения установленной проблемы покрытия:
    Поиск наиболее вещательных станций.
    :stations: dict -
    :return: список со станциями, которые вещают на большее количество городов
    """
    not_cover = set()
    for v in data.values():
        for s in v:
            not_cover.add(s)
    select_stations = []
    while True:
        max_key = ''
        max_num = 0
        for k in data.keys():
            intersection = not_cover.intersection(data[k])
            if len(intersection) > max_num:
                max_key = k
                max_num = len(intersection)
        select_stations.append(max_key)
        for e in data[max_key]:
            if e in not_cover:
                not_cover.remove(e)
        if len(not_cover) == 0:
            break

    return select_stations


if __name__ == '__main__':
    data_unsorted = {'station_1': ['Москва', 'Санкт-Петербург', 'Владимир'],
                     'station_2': ['Нижний Новгород', 'Москва', 'Тверь'],
                     'station_3': ['Иваново', 'Санкт-Петербург', 'Калуга'],
                     'station_4': ['Санкт-Петербург', 'Владимир'],
                     'station_5': ['Калуга', 'Воронеж']}
    print(covering_set(data_unsorted))

