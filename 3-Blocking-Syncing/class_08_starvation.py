import threading
import time
from collections import deque

class FairLock:
    def __init__(self):
        self._lock = threading.Lock()
        self._waiting_threads = deque() # Очередь ожидания для потоков
        self._internal_lock = threading.Lock() # Внутренний лок, который изначально заблокирован

    def acquire(self):
        queue_lock = threading.Lock() # Заблокируем перед добавлением в очередь
        with self._lock:
            self._waiting_threads.append(queue_lock)
            if len(self._waiting_threads) == 1:
                # Если это первый лок в очереди, немедленно его освобождаем
                queue_lock.acquire() # Ожидаем освобождения
        queue_lock.acquire()

    def release(self):
        with self._lock:
            self._waiting_threads.popleft() # Удаляем текущий лок из очереди
            if self._waiting_threads:
                # Освобождаем следующий лок в очереди
                self._waiting_threads[0].release()

fair_lock = FairLock()

def task():
    for _ in range(5):
        fair_lock.acquire()
        print(f"{threading.current_thread().name} is running")
        time.sleep(1) # Имитация работы
        fair_lock.release()

threads = [threading.Thread(target=task, name=f"Thread-{i}") for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()