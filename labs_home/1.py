import math

from mpi4py import MPI

import my_lib

num_elements = 10_000_000  # Рассчитываемое кол-во элементов в ряде
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Получение номера процесса
size = comm.Get_size()  # Получение числа запущенных процессов
start, end = my_lib.calculate_range(num_elements, size, rank)  # Вычисление диапозона для расчета
arctg_sum = my_lib.part_of_sum_arctg1(start, end)  # Вычисление суммы элементов ряда

# Суммирование результатов со всех процессов
arctg = comm.reduce(arctg_sum, op=MPI.SUM, root=0)

if rank == 0:
    # Вычисление числа π
    pi = 4 * arctg
    print("Вычисленное значение числа π:", pi)
    # Для сравнения с встроенным значением π из библиотеки math
    print("Значение π из библиотеки math:", math.pi)
