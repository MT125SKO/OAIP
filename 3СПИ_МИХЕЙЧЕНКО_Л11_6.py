############# 6 задание
import cProfile
import time


def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    try:
        input_str = input("число  ")
        numbers = [int(x) for x in input_str.split()]

        start_time = time.perf_counter()
        sorted_numbers = bubble_sort(numbers)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print("список", sorted_numbers)
        print(f"Время  {elapsed_time:.6f} ")

    except ValueError:
        print("ошибка")


###############################################
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