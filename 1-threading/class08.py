# exercise with class

import  threading
import time

class PrintNumbersThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__()
        self.name = name
        
    def run(self):
        print(f"Поток {self.name} начал выполнение")
        for i in range(5):
            time.sleep(1)
        print(f"Поток {self.name} завершил выполнение")
    

thread1 = PrintNumbersThread(name="Thread-1")
thread2 = PrintNumbersThread(name="Thread-2")

thread1.start()
thread2.start()

print('Потоки Запущены')

thread1.join()
thread2.join()

print('Потоки Завершены')
