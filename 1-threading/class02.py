from multiprocessing import process
import threading
from time import sleep

def print_numbers():
    for i in range(6):
        print(i)
        sleep(1)

thread = threading.Thread(target=print_numbers)
thread.start()

print('PROCESS: we are in the main flow')
while thread.is_alive():
    print('thread is running')
    sleep(2)
thread.join()
print('END: we are in the main flow')
