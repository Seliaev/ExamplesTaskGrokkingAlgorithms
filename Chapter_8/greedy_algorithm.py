def greedy_sorting(data: dict) -> list:
    """
    Пример жадного альгоритма
    Проходит по списку с уроками, находит тот, который заканчивается раньше всех, сохраняет его
    затем находит урок, которым первым начинается после законченного и так далее.
    :data: dict Словарь с данными, список с временем начала уроков, их окончания и названием.
    :return: Список с выбранными уроками
    """
    selected_lesson = []
    start_position = 0
    for i in range(0, len(data['finish_time_str'])):
        for j in range(0, len(data['finish_time_str'])):
            if data['finish_time_str'][i] < data['finish_time_str'][j]:
                temp = data['lesson'][i], data['finish_time_str'][i], data['start_time_str'][i]
                data['lesson'][i], data['finish_time_str'][i], data['start_time_str'][i] = data['lesson'][j], \
                    data['finish_time_str'][j], data['start_time_str'][j]
                data['lesson'][j], data['finish_time_str'][j], data['start_time_str'][j] = temp

    selected_lesson.append(data['lesson'][start_position])
    for pos in range(len(data['finish_time_str'])):
        if data['start_time_str'][pos] >= data['finish_time_str'][start_position]:
            selected_lesson.append(data['lesson'][pos])
            start_position = pos
    return selected_lesson


if __name__ == "__main__":
    import datetime
    dt_format = '%H:%M'
    start_time_str = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30']
    finish_time_str = ['10:00', '10:30', '11:00', '11:30', '12:00', '12:30']

    data_unsorted = {
        "start_time_str": [datetime.datetime.strptime(x, dt_format).timestamp() for x in start_time_str],
        "finish_time_str": [datetime.datetime.strptime(x, dt_format).timestamp() for x in finish_time_str],
        "lesson": ["Рисование", "Английский", "Математика", "Информатика", "Биология", "Музыка"]
    }
    selected_lesson = greedy_sorting(data_unsorted)

    print(f"Уроки, которые будут проводиться: {selected_lesson}")
