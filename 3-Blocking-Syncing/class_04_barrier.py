import threading
import time

def worker(barrier):
    print(f"Поток {threading.current_thread().name} начинает работу.")
    time.sleep(1) # Имитация работы потока
    print(f"Поток {threading.current_thread().name} дошел до барьера.")
    barrier.wait()
    time.sleep(1) # Имитация работы потока
    print(f"Поток {threading.current_thread().name} прошел через барьер и продолжил работу")

# Создаем барьер для трех потоков
barrier = threading.Barrier(3)

# Создаем три потока, которые будут использовать барьер
t1 = threading.Thread(target=worker, args=(barrier,))
t2 = threading.Thread(target=worker, args=(barrier,))
t3 = threading.Thread(target=worker, args=(barrier,))

# Запускаем потоки
t1.start()
time.sleep(2) # Имитация работы потока
t2.start()
time.sleep(2) # Имитация работы потока
t3.start()

# Ждем завершения потоков
t1.join()
t2.join()
t3.join()