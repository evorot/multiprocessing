import math
import multiprocessing
import time

import my_lib


# Функция, которая рассчитывает начальный и конечный диапозон ряда, затем вычисляет сумму элементов этого диапозона
# Результат отправляет в очередь
def work(q, total_elements, total_processes, process_number):
    start, end = my_lib.calculate_range(total_elements, total_processes, process_number)
    arctg_sum = my_lib.part_of_sum_arctg1(start, end)
    q.put(arctg_sum)


if __name__ == '__main__':
    start = time.perf_counter()
    num_elements = 10_000_000  # Рассчитываемое кол-во элементов в ряде
    proc_qty = 4  # Количество процессов
    q = multiprocessing.Queue()  # Создаем очередь
    processes = []
    # Создаем n процессов, которые вычисляют сумму элементов части ряда
    for i in range(proc_qty):
        # Создание объекта процесса с целевой функцией work
        p = multiprocessing.Process(target=work, args=(q, num_elements, proc_qty, i))
        # Добавляем процесс в список всех процессов
        processes.append(p)
        # Запускаем процесс
        p.start()

    # Ждем завершения всех процессов
    for p in processes:
        p.join()

    # Суммируем все суммы из очереди
    arctg = 0
    while not q.empty():
        arctg += q.get()

    # Вычисление числа π
    pi = 4 * arctg
    finish = time.perf_counter()

    print("Вычисленное значение числа π:", pi)
    # Для сравнения с встроенным значением π из библиотеки math
    print("Значение π из библиотеки math:", math.pi)
    print(f'Выполнение заняло {finish - start: .2f} секунд.')
