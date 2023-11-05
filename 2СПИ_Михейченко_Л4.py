#Задача 1
a = ''
for v in range (8):
    r = input ()
    a += r
    print (a)

#Задача 2
a = int (input())
s = []
for c in range (a):
    s.append (input())
for c in range (a):
    print (c+1, s [c])

#Задача 3
a = int (input("Введите даты вылета\n>>>"))
dd = int (input("Введите шаг\n>>>"))
r = ""
for y in range (a, 32, dd):
    r += str(y) + " "
print ("Возможные даты вылета:" + r)

#Задача 4
a = input ('Введите букву повтора: ')
n = int (input('Введите количество букв: '))
t = input ('Введите буквы для проверки: ')
w = 0
q = 0
for i in range (n):
    if t [i] == a:
        q += 1
        w = max (w, q)
else:
    q = 0
print (w)

#Задача 5
a = int (input('Введите число\n>>>'))
w = sum (range(1, a + 1, a % 2 + 1))
print ('Сумма делителей равна', a, 'и', w)

#Задача 6
a = input ("Введите строку: ")
w = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
d = a.lower ()
r = 0
for i in d:
    if i in w:
        r += 1
        print ('Количество безударных гласных:', r)

#Задача 7
a = input ('Введите слово\n>>>')
d = int (input("Введите число n\n>>>"))
for i in range (1, d+1):
    print(a)

#Задача 8
телефон = input ("Введите номер телефона: ")
if not all (a.isdigit() or a == '+' for a in телефон ):
    print ('Неправильный номер телефона!')
else:
    print ('Авторизация успешна!')

#Задача 9
a = 'аеёиоуыэюя'
d = 'бвгджзйклмнпрстфхцчшщъь'
t = input ('Введите пароль:').lower()
w = ''
for i in t:
    if i in a:
        w += '0'
    else:
        w += '1'
print ('Зашифрованный пароль:', w)

#Задача 10
q = ('ППррииввеетт!! ККаакк ддееллаа?? ССееггоодднняя ттааккааяя ххоорроошшааяя ппооггооддаа, ммоожжеетт '
           'ппооггуулляяеемм??')
aw = ''
for t in range (len(q)):
    if t == len (q) - 1 or q [t] != q [t+1]:
        aw += q [t]
        print (aw)


