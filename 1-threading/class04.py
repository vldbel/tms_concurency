import threading
import time

def print_nums():
    for i in range(6):
        time.sleep(1)
        print(i)
        

def print_letters():
    for letter in 'abcde':
        time.sleep(1.5)
        print(letter)
        

thread1 = threading.Thread(target=print_nums)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()
