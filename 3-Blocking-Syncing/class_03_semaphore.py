import threading
from time import sleep

# Создаем семафор, который позволяет двум потокам захватить его за раз
semaphore = threading.Semaphore(2)

def print_numbers():
    with semaphore:
        for t in range(10):
            print(t)
            sleep(1)

def print_letters():
    with semaphore:
        for letter in 'abcdefghij':
            print(letter)
            sleep(1)
            
# Создаем четыре потока
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_numbers)
t3 = threading.Thread(target=print_letters)
t4 = threading.Thread(target=print_letters)

# Запускаем потоки
t1.start()
t2.start()
t3.start()
t4.start()

# Ждем завершения потоков
t1.join()
t2.join()
t3.join()
t4.join()