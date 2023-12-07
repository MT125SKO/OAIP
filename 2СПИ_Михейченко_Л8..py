#Задание 1
try:
    num1 = int(input())
    num2 = int(input())
    result = num1 + num2
except ValueError:
    print("Ошибка!! \nВведите только целочисленные числа")
else:
    print(result)

#Задание 2
while True:
    try:
        num1 = int(input())
        num2 = int(input())
        result = num1 + num2
    except ValueError:
        print("Ошибка!! \nВведите только целочисленные числа")
    else:
        print(result)
        break

#Задание 3
m1 = int(input())
m2 = int(input())
try:
    result = m1 // m2
except ZeroDivisionError:
    print("Ошибка!! \nДеление на 0")
else:
    print(result)

#Задание 4 
try:
    m1 = int(input())
    m2 = int(input())
    result = m1 // m2
except ZeroDivisionError:
    print("Ошибка! \nДеление на 0!!!")
except ValueError:
    print("Ошибка! \nВведите только целочисленные числа")
else:
    print(result)

#Задание 5
try:
    num1 = int(input())
    num2 = int(input())
    result = num1 // num2
except ZeroDivisionError:
    print("Ошибка!! \nДеление на 0!!!")
except ValueError:
    print("Ошибка!! \nВведите только целочисленные числа")
else:
    print(result)
finally:
    print("Выход из программы!")