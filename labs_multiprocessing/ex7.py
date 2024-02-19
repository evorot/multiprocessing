import multiprocessing
import time


def daemon():
    print('Starting:', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время
    time.sleep(2)  # ждем 2 секунды
    print('Exiting :', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время


def non_daemon():
    print('Starting:', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время
    print('Exiting :', multiprocessing.current_process().name, time.time())  # печатаем имя процесса и время


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)  # процесс демон, с вызываемой функцией daemon
    d.daemon = True  # признак daemon поставлен в true

    n = multiprocessing.Process(name='non-daemon',
                                target=non_daemon)  # процесс недемон, с вызываемой функцией non-daemon
    n.daemon = False  # признак daemon поставлен в false

    d.start()  # запускаем процесс daemon
    n.start()  # запускаем процесс non-daemon

    d.join(1)  # ждем выполнения процесса daemon с указанием таймаута в 1 секунду, после чего продолжается программа
    print('d.is_alive()', d.is_alive(),
          time.time())  # выводим значение d.is_alive с указанием времени
    # (вернется тру, тк функция демона еще не закончится, а ждали выполнение процесса только 1 сек)
    n.join()  # ждем выполнения процесса non-daemon
    print('End main ', time.time())  # печатаем время завершения основного процесса
