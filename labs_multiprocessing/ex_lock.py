from multiprocessing import Process, Lock


def f(lос, i):
    lос.acquire()  # блокируем локер
    print('hello world', i)  # печатаем hello world c указанием индекса
    lос.release()  # высвобождаем локер


if __name__ == '__main__':
    # создаем локер
    lock = Lock()

    # Создаем и запускаем 10 процессов с целевой функией f с агрументами локером и индексом
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
