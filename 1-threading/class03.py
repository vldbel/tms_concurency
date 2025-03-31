import threading
from time import sleep

def print_thread_info():
    current = threading.current_thread()
    sleep(1)
    print(f'Текущий поток: {current.name}')
    print(f'Количество активных потоков: {threading.active_count()}')

thread1, thread2, thread3 = [threading.Thread(target=print_thread_info) for _ in range(3)]
thread1.start()
thread2.start()
thread3.start()
print(list(threading.enumerate()))
thread1.join()
thread2.join()
thread3.join()