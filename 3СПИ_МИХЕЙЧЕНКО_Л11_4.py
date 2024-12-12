#1 код задание 4
import time


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = 35

start_time = time.time()
recursive_result = fibonacci_recursive(n)
end_time = time.time()
print(f"Recursive: {recursive_result}, Time: {end_time - start_time:.6f} seconds")

##################################2222222222
import time


def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


n = 35

start_time = time.time()
memoization_result = fibonacci_memoization(n)
end_time = time.time()
print(f"Memoization: {memoization_result}, Time: {end_time - start_time:.6f} seconds")

#########################3333
import time


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


n = 35

start_time = time.time()
iterative_result = fibonacci_iterative(n)
end_time = time.time()
print(f"Iterative: {iterative_result}, Time: {end_time - start_time:.6f} seconds")

