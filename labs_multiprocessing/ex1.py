import multiprocessing


def worker():
    """worker function,
        печатает текст Worker
    """

    print('Worker')

    return


if __name__ == '__main__':
    # Выводит доступное количество процессов
    print('Threads available: ', multiprocessing.cpu_count())
    jobs = []

    # Создаем пять процессов, которые печатают Worker
    for i in range(5):
        print(i)
        p = multiprocessing.Process(target=worker)

        jobs.append(p)

        p.start()
        p.join()
    # Печатает информацию о всех процессах
    print(jobs)
