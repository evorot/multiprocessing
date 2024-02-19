import multiprocessing
import sys
import time


def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)  # печатаем имя процесса и идентификатор процесса
    sys.stdout.flush()  # принудительно очищаем буфер вывода
    time.sleep(2)  # ждем 2 секунды
    print('Exiting :', p.name, p.pid)  # печатаем имя процесса и идентификатор процесса
    sys.stdout.flush()  # принудительно очищаем буфер вывода


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid)  # печатаем имя процесса и идентификатор процесса
    sys.stdout.flush()  # принудительно очищаем буфер вывода
    print('Exiting :', p.name, p.pid)  # печатаем имя процесса и идентификатор процесса
    sys.stdout.flush()  # принудительно очищаем буфер вывода


# Скрипт запускает демонический и недемонический процесс. Демонический процесс не успеет до конца отработать,
# так как демонические процессы завершаются, когда основной процесс (главный процесс) завершается
if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)  # процесс демон, с вызываемой функцией daemon
    d.daemon = True  # признак daemon поставлен в true

    n = multiprocessing.Process(name='non-daemon',
                                target=non_daemon)  # процесс недемон, с вызываемой функцией non-daemon
    n.daemon = False  # признак daemon поставлен в false

    d.start()  # запускаем процесс daemon
    time.sleep(1)  # ждем секунду
    n.start()  # запускаем процесс non-daemon
