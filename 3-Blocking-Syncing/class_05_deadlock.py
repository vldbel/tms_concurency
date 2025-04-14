import threading
from time import sleep

# Создаем две блокировки
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_routine():
    print("Thread 1 acquiring lock 1")
    with lock1:
        print("Thread 1 acquired lock 1")
        print("Thread 1 acquiring lock 2")
        sleep(1)
        with lock2:
            print("Thread 1 acquired lock 2")
            sleep(1)
    print("Thread 1 released both locks")

def thread2_routine():
    print("Thread 2 acquiring lock 2")
    with lock2:
        print("Thread 2 acquired lock 2")
        print("Thread 2 acquiring lock 1")
        sleep(1)
        with lock1:
            print("Thread 2 acquired lock 1")
            sleep(1)
    print("Thread 2 released both locks")

# Создаем и запускаем потоки
thread1 = threading.Thread(target=thread1_routine)
thread2 = threading.Thread(target=thread2_routine)

thread1.start()
thread2.start()

thread1.join()
thread2.join()