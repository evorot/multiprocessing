from math import sin, cos
from multiprocessing import Pool
from time import time


# Функция, которая проводит некие вычисления над переданным аргументом 100 раз,
# результат конечной итерации возвращается
def some_slow_calc(x):
    for i in range(100):
        y = sin(cos(sin(cos(x + i))))
    return y


if __name__ == '__main__':
    # засекается время вычислений последовательного вычисления
    t_start = time()
    for x in range(100000):
        z = some_slow_calc(x)
    t_end = time()
    print('time of non parallel version', t_end - t_start)

    # засекается время вычисления для n-пульных процессов
    for n in [1, 2, 3, 4]:
        t_start = time()
        # создается объект пула из процессов
        p = Pool(processes=n)
        # параллельно вызывается функция some_slow_calc для 0-99999
        p.map(some_slow_calc, [x for x in range(100000)])
        t_end = time()
        print('time of parallel calc on', n, 'proc', t_end - t_start)
