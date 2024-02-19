import os
from multiprocessing import Process


# info
def info(title):
    """
    Печатает title, id родительского процесса, id процесса
    """
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    """
    Печатает function f и hello + переданный name
    """
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')  # Выводится информация по main
    p = Process(target=f, args=('bob',))  # Создается новый процесс, с заданной функцией f с аргументом bob
    p.start()  # Запустить процесс
    p.join()  # Ждем выполнение процесса p
