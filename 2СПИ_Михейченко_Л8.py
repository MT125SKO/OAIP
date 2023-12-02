#Задание 1
n = int(input())
a = []
z = []
d = 0
for i in range(n):
    c = int(input())
    a.append(c)
    t = a
    t.reverse()
for i in a:
    d = i
    for j in t:
        razn = d - j
        z.append(razn)
        z = set(z)
        z = list(z)
        z.sort()
for i in z:
    print(i, end='\n')

#Задание 2
d = input().split(';')
for i in range(len(d)):
    f = d[i].split(',')
    e= []
    for j in  f:
        if int(j) > 1000000:
            e.append(j)
    print(','.join(e))\

#Задание 3
a = input()
a1 = ''
for i in a:
    print(2*i,end='')