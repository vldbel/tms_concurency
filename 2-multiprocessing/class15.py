import concurrent.futures
import time
from unittest import result

def worker(x):
    time.sleep(1)
    return x * x

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        input = [1, 2, 3, 4, 5]
        results = list(executor.map(worker, input))
        print(results)