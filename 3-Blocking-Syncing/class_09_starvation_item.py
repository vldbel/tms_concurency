import threading
import time

class Item:
    def __init__(self):
        self.available = False
        self.condition = threading.Condition()

    def produce(self):
        with self.condition:
            time.sleep(1) # Имитация производства
            self.available = True
            print(f"{threading.current_thread().name} produced an item.")
            self.condition.notify_all() # Уведомление потребителей о доступности предмета

    def consume(self):
        with self.condition:
            while not self.available:
                self.condition.wait() # Ожидание уведомления
            print(f"{threading.current_thread().name} consumed the item.")
            self.available = False # Потреблен предмет

def producer(item):
    item.produce()

def consumer(item):
    item.consume()

# Создание объекта, который будет использоваться потоками
shared_item = Item()

# Запуск потоков
producer_thread = threading.Thread(target=producer, name="Producer", args=(shared_item,))
consumer_thread = threading.Thread(target=consumer, name="Consumer", args=(shared_item,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
