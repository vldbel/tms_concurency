from multiprocessing import Process, Queue
import queue

def square(numbers, queue:Queue):
    for n in numbers:
        queue.put(n * n)
        
def print_squares(queue:Queue):
    while not queue.empty():
        print(queue.get())
    

if __name__ == '__main__':
    numbers = range(10)
    q = Queue()
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=print_squares, args=(q,))
    p1.start()
    p1.join()
    print('p1 finished')
    p2.start()
    p2.join()
