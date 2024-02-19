import multiprocessing


# Класс Worker, который наследует класс Process
class Worker(multiprocessing.Process):

    # Переопределяем процеес run, который выводит сообщение о том, в каком процессе он выполняется
    def run(self):
        print('In %s' % self.name)
        return


if __name__ == '__main__':
    # Создаем список jobs, куда будем добавлять Worker
    jobs = []

    # Создаем 5 экземпляров класса Worker, добавляем их в список jobs и запускаем каждый процесс
    for i in range(5):
        p = Worker()  # инициализируем Worker
        jobs.append(p)  # добавляем всех воркера в jobs
        p.start()  # запускаем процесс

    for j in jobs:
        j.join()  # ждем завершения всех воркеров
