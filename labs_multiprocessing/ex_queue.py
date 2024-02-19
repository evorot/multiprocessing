from multiprocessing import Process, Queue


def func(q_in, q_out):
    # получаем значение из очереди
    x = q_in.get()
    # печатаем значение, которое получили из очереди
    print('func get: ', x)
    # отправляем в очередь q_out квадрат, полученного значаения
    q_out.put(x ** 2)


if __name__ == '__main__':
    # создаем две очереди
    q_in = Queue()
    q_out = Queue()
    # создаем и запускаем 4 процесса, которые выполняют func с аргументами q_in, q_out
    for x in range(4):
        p = Process(target=func, args=(q_in, q_out))
        p.start()
    # отправляем в очередь q_in номер итерации
    # печатаем значаением, полученное из очереди q_out
    for x in range(4):
        q_in.put(x)
        print('in main recv: ', q_out.get())
