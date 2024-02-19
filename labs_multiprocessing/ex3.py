import multiprocessing

import multiprocessing_import_worker

if __name__ == '__main__':
    # последотельно запускает 5 процессов, которые вызывают worker из пакета multiprocessing_import_worker
    # печатают Worker с указанием индекса итерации
    # для чего тут jobs - не ясно
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=multiprocessing_import_worker.worker)
        jobs.append(p)
        p.start()
