import random


# Вычисление диапозона для расчета
def calculate_range(total_elements, total_processes, process_number):
    # Вычисляем размер "шага" для каждого процесса
    step = total_elements // total_processes

    # Определяем начальный и конечный индексы для текущего процесса
    start = process_number * step
    end = start + step
    # Если это последний процесс, учитываем оставшиеся элементы
    if process_number == total_processes - 1:
        end = total_elements
    return start, end


def part_of_sum_arctg1(start_num, end_num):
    sum = 0

    s = -1 if start_num % 2 != 0 else 1

    for n in range(start_num, end_num):
        sum += s / (2 * n + 1)
        s = -s
    return sum


def count_inside_circle(points):
    # Счетчик точек, попавших внутрь окружности
    inside_circle = 0

    # Генерация случайных точек и подсчет точек, попавших внутрь окружности
    for _ in range(points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    return inside_circle
