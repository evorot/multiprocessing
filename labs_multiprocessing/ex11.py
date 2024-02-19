import logging
import multiprocessing
import sys


def worker():
    print('Doing some work')  # печатает текст
    sys.stdout.flush()  # принудительно очищаем буфер вывода


if __name__ == '__main__':
    multiprocessing.log_to_stderr()  # устанавливаем вывод логов в терминал
    logger = multiprocessing.get_logger()  # получем логгер
    logger.setLevel(logging.INFO)  # устанавливаем для логгера уровень INFO
    p = multiprocessing.Process(target=worker)  # инициализируем процесс с вызываемой функцией worker
    p.start()  # запускает процесс р
    p.join()  # ждем выполнения процесса р
