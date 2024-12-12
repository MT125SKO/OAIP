############ 5 зд
import time
def filter_numbers():
    numbers = []
    try:
        start = int(input("Первое число: "))
        end = int(input("Второе число: "))
        start_time = time.perf_counter()

        for i in range(start, end + 1):
            if i % 3 == 0 or i <= 0:
                numbers.append(i)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Время  {elapsed_time:.6f}")
        return numbers
    except ValueError:
        return "Ошибка:"


if __name__ == "__main__":
    result = filter_numbers()
    print(result)
######################
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