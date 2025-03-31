import threading

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Факториал {n} = {result}")
    

nums = range(20, 48, 2)
# print(list(nums))

threads = []

for num in nums:
    thread = threading.Thread(target=factorial, args=(num,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
