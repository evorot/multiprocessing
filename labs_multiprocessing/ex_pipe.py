import multiprocessing


def pipe_func(ch, N_iter):
    a = 0
    # отправояем в канал поочередно значения от 0 до номера итерации
    for i in range(N_iter):
        a += 1
        ch.send(a)

    # отправляем в канал СТОП
    ch.send('STOP')


if __name__ == '__main__':
    # Создаем канал между родительским и дочерним процессами
    parent, child = multiprocessing.Pipe()

    for iter in range(4):
        # создаем процесс с целевой функцией pipe_func, передаем аргумент канал и текущую итерацию
        p = multiprocessing.Process(target=pipe_func, args=(child, iter))
        p.start()  # запускаем процесс р

        result = None
        # пока не получим из канала СТОП, печатаем в терминал номер итерации и результат
        # из канала от функции pipe_func
        while result != 'STOP':
            result = parent.recv()
            print(iter, result)
