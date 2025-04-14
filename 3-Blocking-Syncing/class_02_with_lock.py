import threading

# СОЗДАЕМ МЬЮТЕКС
lock = threading.Lock()

def print_numbers():
    with lock:
        for i in range(10):
            print(i)

def print_letters():
    with lock:
        for letter in 'abcdefghij':
            print(letter)

# СОЗДАЕМ ДВА ПОТОКА
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# ЗАПУСКАЕМ ПОТОКИ
t1.start()
t2.start()

# ЖДЕМ ЗАВЕРШЕНИЯ ПОТОКОВ
t1.join()
t2.join()