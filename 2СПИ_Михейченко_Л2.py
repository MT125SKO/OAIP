#Задание 1
if input () == "Pthon":
    print ("Да")
else:
    print ("Нет")

#Задание 2
a = input()
b = input()
if a == 'да' or a == 'нет' and b == 'да' or b == 'нет':
    print('ВЕРНО')
else:
    print('НЕВЕРНО')

#Задание 3
a = input()
b = input()
c = input()
if a == 'раз' or a == '1':
    if b == 'два' or b == '2':
        if c == 'три' or c == '3':
            print('ГОРИ')
else:
    print('НЕ ГОРИ')

#Задание 4
a1 = "Тула"
a2 = "Пенза"
e = input ()
e2 = input ()
if e == a1 and e2 == a2:
    print ("Да")
else:
    print ("нет")

#Задание 5
n = int (input())
m = int (input())
print ((n + m - 1) // m)

#Задание 6
a = int (input () )
y = int (input () )
t = int (input () )
ayt = a + t // 8
if ayt != 0 and y == 3:
    print ('Подходит')
else:
    print (a, t, ' ', y)

#Задание 7
a = input ('Категория >>> ')
if a == 'продукты':
    w = int (input('Цена >>> '))
    if w < 100:
        print ('Попробуйте нашу выпечку!')
    if 100 <= w < 500:
        print ('Как насчёт орехов в шоколаде?')
    if w > 500:
        print ('Попробуйте экзотические фрукты!')
else:
    print ('Загляните в товары для дома')

#Задание 8
re1 = int (input('Цена первого товара:\n>>>'))
re2 = int (input('Цена второго товара:\n>>>'))
re3 = int (input('Цена третьего товара:\n>>>'))
cost = re1 + re2 + re3
if re1 < re2 < re3:
    print ('Акция!')
    print ('К оплате:', cost / 2)
if re1 > re2 > re3:
    print ('Акция!')
    print ('К оплате:', cost / 3)
 
#Задание 9
a = int (input ('Введите число покупателей позавчера:\n>>>'))
aa = int (input ('Введите число покупателей вчера:\n>>>'))
if aa > a:
    print ('Сегодня магазин посетит:', aa + ( aa - a ), 'человек')
if a > aa:
    print ('Сегодня магазин посетит:', aa - ( a - aa ), 'человек')

#Задание 10
a = int ( input ('Введите год: '))
if a % 4 == 0:
    print ('Год високосный.')
else:
    print ('Год не високосный.')

#Задание 11
a = int ( input ('Введите число\n>>>') )
if a % 2 == 0:
    print ('Число чётное')
else:
    print ('Число нечетное')
