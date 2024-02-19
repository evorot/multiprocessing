import multiprocessing
import time


def slow_worker():
    print('Starting worker', time.time())  # печатаем время начала slow_worker
    time.sleep(0.1)  # ждем 0.1 секунды
    print('Finished worker', time.time())  # печатаем время завершения slow_worker


# создается процесс, после выводится информация о состоянии процесса после различных манипуляций
if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)  # инициализируем процесс с вызываемой функцией slow_worker
    print('BEFORE:', p, p.is_alive(),
          time.time())  # печатаем информацию о процессе и его текущее состояние is_alive() (false)

    p.start()  # запускаем процесс
    print('DURING:', p, p.is_alive(), time.time())  # печатаем состояние процесса is_alive() (true)

    p.terminate()  # отправляем сигнал об уничтожении процесса (функция slow_worker ничего не успеет сделать!)
    print('TERMINATED:', p, p.is_alive(), time.time())  # печатаем состояние процесса is_alive() (true)

    p.join()  # ждем отработки процесса
    print('JOINED:', p, p.is_alive(), time.time())  # печатаем состояние процесса is_alive() (false)
