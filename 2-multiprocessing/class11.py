import multiprocessing
from os import name
import time

def producer(queue):
    for i in range(10):
        time.sleep(1)
        item = f"Item {i}"
        queue.put(item)
        print(f'Производитель: {item} добавлен в очередь')
    
def consumer(queue):
    while True:
        print(f"Размер очереди: {queue.qsize()}")
        item = queue.get()
        if item is None:
            break
        print(f"Потребитель: {item} обработан")
        time.sleep(2)
        

if __name__ == '__main__':
    
    queue = multiprocessing.Queue()
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))
    
    producer_process.start()
    consumer_process.start()
    
    producer_process.join()
    queue.put(None)
    consumer_process.join()
