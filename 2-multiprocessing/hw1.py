from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from cryptography.hazmat.primitives.asymmetric import rsa
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        time_spent = (end_time - start_time)
        print(f"Время выполнения функции: {func} составило: {time_spent:.2f} секунд")
        return res
    return wrapper

# Целевая функция, возвращает ключи в сериализуемом формате
def generate_rsa_key_pair():
    """Генерация пары RSA-ключей, возвращает числа n, e, d"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096
    )
    public_key = private_key.public_key()
    
    # Извлекаем числа из ключей
    n = public_key.public_numbers().n
    e = public_key.public_numbers().e
    d = private_key.private_numbers().d
    
    return (n, e, d)  # Кортеж чисел, который можно сериализовать

@time_it
def generate_one_thread(repeats):
    key_pairs = [generate_rsa_key_pair() for _ in range(repeats)]
    return key_pairs 

@time_it
def generate_multi_threads(repeats, threads_count=4):
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        futures = [executor.submit(generate_rsa_key_pair) for _ in range(repeats)]
        key_pairs = [future.result() for future in futures]    
    return key_pairs

@time_it
def generate_multi_process(repeats, threads_count=4):
    with ProcessPoolExecutor(max_workers=threads_count) as executor:
        futures = [executor.submit(generate_rsa_key_pair) for _ in range(repeats)]
        key_pairs = [future.result() for future in futures]    
    return key_pairs

if __name__ == '__main__':
    # Количество пар ключей
    num_keys = 100

    # ### linear ###   Генерация 100 пар ключей последовательно
    key_pairs = generate_one_thread(num_keys)

    # ### parallel - threads ###  Генерация 100 пар ключей в потоках        
    threads = 4
    key_pairs = generate_multi_threads(num_keys, threads)

    # ### parallel - threads ###  Генерация 100 пар ключей в потоках        
    threads = 4
    key_pairs = generate_multi_process(num_keys, threads)
