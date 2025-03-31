import random
import threading
import time


class RandomNumberThread(threading.Thread):
    def __init__(self, thread_name, min_num, max_num):
        super().__init__()
        self.thread_name = thread_name
        self.min_num = min_num
        self.max_num = max_num
        
    def run(self):
        for _ in range(5):
            number = random.randint(self.min_num, self.max_num)
            print(f"{self.thread_name} сгенерированно число: {number}")
            time.sleep(1)
            
thread1 = RandomNumberThread("Поток 1", 1, 5)
thread2 = RandomNumberThread("Поток 2", 10, 20)

thread1.start()
thread2.start()

print('Main flow continue')

thread1.join()
thread2.join()
