#Задача 1
ist = [5, 6, 0, 1, 2, 4, 6, 7, 9, 11, 14,]
for i in range (0, 9):
    if ist[i] > ist[i+1]:
        swap = ist [i]
        ist[i] = ist[i+1]
        ist[i+1] = swap
print(ist)

#Задача 2
a = [-2, -12, 23, 4, 5, 6, 7, 8, -4, -43, 65]
n = len(a)
for i in range (n-1):
    m = a[i]
    c = i
    for t in range(i+1, n):
        if m > a[t]:
            m = a[t]
            c = t
    if c != i:
        d = a[t]
        a[i] = a[c]
        a[c] = d
print(a)