from platform import release
from random import randint
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_routine():
    while True:
        time.sleep(randint(1, 5))
        if lock1.acquire(timeout=1):  # Пытаемся захватить первую блокировку
            print("Thread 1 acquired lock 1")
            time.sleep(1)  # Делаем паузу для имитации работы
            if lock2.acquire(timeout=1):  # Пытаемся захватить вторую блокировку
                print("Thread 1 acquired lock 2")
                lock2.release()
                lock1.release()
                break
        print("Thread 1 failed to acquire locks, retrying...")
        lock2.release
        
def thread2_routine():
    time.sleep(randint(1, 5))
    while True:
        if lock2.acquire(timeout=1):  # Пытаемся захватить вторую блокировку
            print("Thread 2 acquired lock 2")
            time.sleep(1)  # Делаем паузу для имитации работы
            if lock1.acquire(timeout=1):  # Пытаемся захватить первую блокировку
                print("Thread 2 acquired lock 1")
                lock1.release()
                lock2.release()
                break
        print("Thread 2 failed to acquire locks, retrying...")
        lock2.release

thread1 = threading.Thread(target=thread1_routine)
thread2 = threading.Thread(target=thread2_routine)

thread1.start()
thread2.start()

thread1.join()
thread2.join()