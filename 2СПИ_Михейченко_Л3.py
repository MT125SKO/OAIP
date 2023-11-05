#Задание 1
while True:
    a = input ('Введи строку:')
    if a == '':
        break
    print ('Столько ты написал: ', len(a))

#Задание 2
a= 0
while (x := float(input())) <= 36.6:
    if x < 0:
        a += 1
        print(a)

#Задание 3
a = []
while True:
    r = int (input())
    if abs (r) >= 1000:
        break
    a+= [r]
print (sorted(set (a) )[-2])

#Задание 4
a = input ('Введите числа: ')
n = a.split ()
n = [int (num) for num in n]
d = n [0]
for s in n:
    if s < d:
        d = i
print ('Наименьшее число:', d)

#Задание 5
while True:
    a = int (input())
    if a == 0: break
    if not a % 7 and not a % 3:
        print ('Караул!')
    elif not a % 3:
        print ('несчасливая')
    elif not a % 7:
        print ('опасное')
    else:
        print (a)

#Задание 6
a = 0   
for w in range (int(input())+1):   
    if len ([m for m in range(1, w+1) if w % m == 0]) == 2: 
        a += w 
print(a)

#Задание 7
a, a2, q = map (int, input().split())
x = 0
while True:
    sma, r, er = map (int, input().split())
    if sma == 0 and r == 0 and er == 0:
        break
    x += sma * r * er
    bi = a * a2 * q
    if x <= bi:
        print ("Да")
    else:
        print ("Нет")

#Задание 8
s = []
while True:
    r = input ("Введите слово: ")
    if r == 'стоп':
        break
    s.append(r)
t= s [0]
for r in s:
    if len (r) < len (t):
        t = r
print ('Самое короткое слово:', t)

#Задание 9
a = int (input())
aa = input ()
t = a
while aa != 'стоп':
    if aa == '+':
        t += a
    if aa == '-':
        t -= a
    a = int (input())
    aa = input ()
print (t)

#Задание 10
d = []
while True:
    a = input ("Введите слово\n>>>")
    if a == "стоп":
        break
    d.append (a)
    dd= ' '.join (d)
    w = dd.split ('!')
    for w in w:
        print (w.strip())