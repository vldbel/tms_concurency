def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fact_rec(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_rec(n-1)

n = 1
print(f"Факториал {n} = {factorial(n)}")
print(f"Факториал {n} = {fact_rec(n)}")

n = 3
print(f"Факториал {n} = {factorial(n)}")
print(f"Факториал {n} = {fact_rec(n)}")

n = 5
print(f"Факториал {n} = {factorial(n)}")
print(f"Факториал {n} = {fact_rec(n)}")
