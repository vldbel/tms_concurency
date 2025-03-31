import threading
from time import sleep

def print_numbers():
    for i in range(5):
        print(i)
        sleep(1)

    
thread = threading.Thread(target=print_numbers)
thread.start()
print('main flow')
sleep(6)
print(thread.is_alive())
print('main flow')
