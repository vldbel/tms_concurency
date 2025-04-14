import threading
import time

loop_count = 10000
sleep_time = 0
threads_count = 10

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            current_value = self.value
            time.sleep(sleep_time) # Искусственная задержка для усиления эффекта гонки
            self.value = current_value + 1

def worker(counter:Counter):
    for _ in range(loop_count):
        counter.increment()

shared_counter = Counter()
threads = [threading.Thread(target=worker, args=(shared_counter,)) for _ in range(threads_count)]

for thread in threads:
    thread.start()
    print(f"{thread.name} started")

for thread in threads:
    thread.join()
    print(f"{thread.name} finished")

print(f"Final counter value: {shared_counter.value}")
print(f"Expected counter value: {loop_count * threads_count}")


"""
No Locks = race condition

Final counter value: 10064
Expected counter value: 100000
"""

"""With lock:
Final counter value: 100000
Expected counter value: 100000
"""