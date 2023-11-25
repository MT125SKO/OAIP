#Задание 1 
a = [1, 2, 3, 4, 5, 6, 11, 32, 43,]
c = len (a)
ccd = 32
for i in range (0, c):
    if a [i] == ccd:
        print(i)

#Задание 2
a = [1, 2, 3, 4, 5, 6, 11, 32, 43,]
b = 11
r = 0
f = len(a) - 1
m = (r + f) //2
while b != a[m]:
    if b > a[m]:
        r = m + 1
    else:
        f = m - 1
    m = (r+f) // 2
print(m)

#Задание 3
a1 = 1
a2 = 2
n = int(input())
print(a1,a2, end=' ')
while a2 < n:
    print(a2, end=' ')
    a1, a2, = a2, a1 + a2

#Задание 4
a = 1
d = 100
while True:   
    m = a % d
    print(a, m)
    if m < a:
        print( a - m)
        break
    else:
        a *= 2

