def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Введите число: "))
result = factorial(number)
print(f"Факториал числа {number} равен {result}")

#2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Введите порядковый номер числа Фибоначчи: "))
result = fibonacci(n)
print(f"Число Фибоначчи под номером {n} равно {result}")

#3
a = input('Введи строку: ')
glas = 'aeyuoi'
b = []
for i in a:
    if i in glas:
        b.append(i)
print('гласных :',len(b))
print('Всего символов: ',len(a)) 

#4
def dd(numb, div = None):
    if div is None:
        div = numb - 1
    while div >= 2:
        if numb % div == 0:
            print("число не простое")
            return False
        else:
            return dd(numb, div-1)
    else:
        print("число простое")
        return True
numb = int(input("введите число: "))
dd(numb)

#5
a = (1234577)
def max_number(a, maxn):
    ts = a % 10
    if ts > maxn:
        maxn = ts
    if a > 9:
        return max_number(a // 10, maxn)
    return maxn
print(max_number(a, -1))