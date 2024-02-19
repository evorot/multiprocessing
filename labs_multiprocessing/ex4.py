import multiprocessing
import time


def worker():
    """
        Функция печатает время старта, ждет 2 секунды и печатает время завершения с указанием имени процесса
    """
    name = multiprocessing.current_process().name
    print(name, 'Starting', time.time())  # печатаем имя процесса и время
    time.sleep(2)  # ждем 2 секунды
    print(name, 'Exiting', time.time())  # печатаем имя процесса и время


def my_service():
    """
    Функция печатает время старта, ждет 3 секунды и печатает время завершения с указанием имени процесса
    """
    name = multiprocessing.current_process().name
    print(name, 'Starting', time.time())  # печатаем имя процесса и время
    time.sleep(3)  # ждем 3 секунды
    print(name, 'Exiting', time.time())  # печатаем имя процесса и время


if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service',
                                      target=my_service)  # инициализируем процесс с именем my_service с вызываемой функцией my_service
    worker_1 = multiprocessing.Process(name='worker 1',
                                       target=worker)  # инициализируем процесс с именем worker 1 с вызываемой функцией worker
    worker_2 = multiprocessing.Process(target=worker)  # инициализируем процесс с вызываемой функцией worker

    worker_1.start()  # запускаем процесс worker_1
    worker_2.start()  # запускаем процесс worker_2
    service.start()  # запускаем процесс service
