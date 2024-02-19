import multiprocessing
import time


def daemon():
    print('Starting:', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время
    time.sleep(2)  # ждем 2 секунды
    print('Exiting :', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время


def non_daemon():
    print('Starting:', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время
    print('Exiting :', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время


# Скрипт запускает демонический и недемонический процесс.
# Оба процесса отработают (daemon/non-daemon), т.к. есть ожидание процессов
if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)  # процесс демон, с вызываемой функцией daemon
    d.daemon = True  # признак daemon поставлен в true

    n = multiprocessing.Process(name='non-daemon',
                                target=non_daemon)  # процесс недемон, с вызываемой функцией non-daemon
    n.daemon = False  # признак daemon поставлен в false

    d.start()  # запускаем процесс daemon
    time.sleep(1)  # ждем секунду
    n.start()  # запускаем процесс non-daemon

    d.join()  # ждем выполнения процесса daemon
    n.join()  # ждем выполнения процесса non-daemon
    print('End main ', time.time())  # печатаем время завершения основного процесса
