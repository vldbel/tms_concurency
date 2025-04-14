from concurrent.futures import thread
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay
        
    def run(self):
        print(f"Starting thread {self.name}")
        thread_lock.acquire(blocking=1)
        thread_count_down(self.name, self.delay)
        thread_lock.release()
        print(f"Thread {self.name} finished")

def thread_count_down(name, delay):
    counter = 5
        
    while counter:
        time.sleep(delay)
        print(f'Thread {name} counting down: {counter}...')
        counter -= 1

thread_lock = threading.Lock()

thread1 = MyThread('A', 0.5)
thread2 = MyThread('B', 0.5)

thread1.start()
thread2.start()

print('Main flow continues')

thread1.join()
thread2.join()

print('Finished')
