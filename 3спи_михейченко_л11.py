import cProfile


def count_words(file_path):
    file = open(file_path, 'r')
    content = file.read()
    words = content.split()
    unique_words = {}
    for word in words:
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    file.close()
    return unique_words


file_path = "file_path.txt"
cProfile.run(f'count_words("{file_path}")')

import cProfile
#########################################################################

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().lower().split()  #
            unique_words = {}
            for word in words:
                unique_words[word] = unique_words.get(word, 0) + 1
            return unique_words
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return None
    except OSError as e:
        print(f"Ошибка: {e}")
        return None


file_path = "file_path.txt"

cProfile.run(f'count_words("{file_path}")')


#3//////////////////////////////////////////////////////////////////////////////////////////////////////////
import cProfile


def count_words(file_path):
    file = open(file_path, 'r')
    content = file.read()
    words = content.split()
    unique_words = {}
    for word in words:
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    file.close()
    return unique_words


file_path = "file_path.txt"
cProfile.run(f'count_words("{file_path}")')


##############################################
import cProfile
import mmap
from collections import Counter


def count_words_mmap(file_path):
    try:
        with open(file_path, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0) as mm:
                words = mm.read().decode('utf-8', errors='ignore').lower().split()
                return dict(Counter(words))
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return None
    except OSError as e:
        print(f"Ошибка: {e}")
        return None
    except UnicodeDecodeError:
        print("Ошибка")
        return None


file_path = "file_path.txt"

cProfile.run(f'count_words_mmap("{file_path}")')

#4444444444444444444444444444444444444444444444444444444444

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

#222222
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


####### 333
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


#5////////////////////////////55555555555555555555555555555555555555555555555555555555555555

import cProfile
import time
import random

def quicksort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = random.choice(numbers)
        less = [i for i in numbers if i < pivot]
        equal = [i for i in numbers if i == pivot]
        greater = [i for i in numbers if i > pivot]
        return quicksort(less) + equal + quicksort(greater)

if __name__ == "__main__":
    try:
        input_str = input("число")
        numbers = [int(x) for x in input_str.split()]

        start_time = time.perf_counter()


        sorted_numbers = quicksort(numbers)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(" список", sorted_numbers)
        print(f"Время {elapsed_time:.6f} ")

    except ValueError:
        print("ошибка")


####################################
import time


def filter_numbers_optimized(start, end):
    return [i for i in range(start, end + 1) if i % 3 == 0 or i <= 0]


def get_input():
    while True:
        try:
            start = int(input("1 число"))
            end = int(input("2 число"))
            if start > end:
                print("Ошибка")
            elif start < 0 and end > 0:
                print("Ошибка")
            else:
                return start, end
        except ValueError:
            print("Неверный ввод")


def time_execution(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time, result


if __name__ == "__main__":
    start, end = get_input()
    elapsed_time, result = time_execution(filter_numbers_optimized, start, end)
    print(f"Врем {elapsed_time:.6f}")
    print(f"итог {result}") 





