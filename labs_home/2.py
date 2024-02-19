import math

from mpi4py import MPI

import my_lib

total_points = 10_000_000  # Общее количество бросков
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Получение номера процесса
size = comm.Get_size()  # Получение числа запущенных процессов
points_by_process = total_points // size  # вычисление количества бросков на процесс
# для последнего процесса получаем оставшиеся броски
if size == rank + 1:
    points_by_process += total_points % size
# считаем количество попадний в круг
inside_circle = my_lib.count_inside_circle(points_by_process)

# Суммирование результатов со всех процессов
total_inside_circle = comm.reduce(inside_circle, op=MPI.SUM, root=0)

if rank == 0:
    # Вычисление числа π
    pi = 4 * total_inside_circle / total_points
    print("Вычисленное значение числа π:", pi)
    # Для сравнения с встроенным значением π из библиотеки math
    print("Значение π из библиотеки math:", math.pi)
