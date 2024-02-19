import multiprocessing


def worker(num):
    """thread worker function"""
    print('Worker:', num)
    return


if __name__ == '__main__':
    # последотельно запускает 5 процессов, которые печают Worker с указанием индекса итерации
    # для чего тут jobs - не ясно
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
