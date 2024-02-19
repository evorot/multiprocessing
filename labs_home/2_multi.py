import math
import multiprocessing

import my_lib


# Функция считает количество попаданий в круг
# Это значаение суммируется к counter через блокировку
def work(points, counter):
    inside_circle_points = my_lib.count_inside_circle(points)
    with counter.get_lock():
        counter.value += inside_circle_points


if __name__ == '__main__':
    total_points = 10_000_000  # Общее количество бросков
    proc_qty = 4  # Количество процессов
    points_by_process = total_points // proc_qty  # вычисление количества бросков на процесс
    # создаем переменную с общим доступом для подсчета всех попаданий
    total_inside_circle = multiprocessing.Value('i', 0)
    processes = []
    # Создаем n процессов, которые выполняют функцию work
    for i in range(proc_qty):
        p = multiprocessing.Process(target=work, args=(points_by_process, total_inside_circle))
        p.start()
        processes.append(p)

    # Ждем выполнения процессов
    for p in processes:
        p.join()

    # Вычисление числа π
    pi = 4 * total_inside_circle.value / total_points
    print("Вычисленное значение числа π:", pi)
    # Для сравнения с встроенным значением π из библиотеки math
    print("Значение π из библиотеки math:", math.pi)
