import threading
import time

# Создаем блокировку
lock = threading.Lock()

def high_priority_task():
    for _ in range(5):
        with lock:
            print(f"High-priority task running by {threading.current_thread().name}")
            time.sleep(1)  # Имитация длительной работы

def low_priority_task():
    for _ in range(5):
        print(f"Low-priority task waiting by {threading.current_thread().name}")
        with lock:
            print(f"Low-priority task running by {threading.current_thread().name}")

# Запускаем потоки
high_priority_threads = [threading.Thread(target=high_priority_task, name=f"High-Priority-Thread-{i}") for i in range(3)]
low_priority_threads = [threading.Thread(target=low_priority_task, name=f"Low-Priority-Thread-{i}") for i in range(3)]

for t in high_priority_threads:
    t.start()

time.sleep(2)  # Задержка для демонстрации преимущества потоков высокого приоритета

for t in low_priority_threads:
    t.start()

for t in high_priority_threads + low_priority_threads:
    t.join()
