# pool

import multiprocessing
import time

def worker(x):
    time. sleep(1)
    return x * x


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        inputs = [1, 2, 3, 4, 5]
        results = pool.map(worker, inputs)
        print('Реазультаты:', results)
