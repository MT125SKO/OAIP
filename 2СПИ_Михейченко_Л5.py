#Задача 1
a = [int(input ('')) for _ in range(int(input('Введите сколько будет чисел, а затем сами числа =')))]
print (len(set(''.join(map(str, a)))))

#Задача 2
a = set(input('Ведите 3 слова. Сейчас водится слово номер 1 '))
a2 = set(input('Сейчас водится слово номер 2 '))
a3 = set(input('Сейчас водится слово номер 3 '))
d1 = (a&a2)
d2 = (a2&a3)
d3 = (a3&a)
print (d1|d2|d3)

#Задача 3
print('Введите число')
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
a = input()
print('Этих цифр небыло')
print(set(numbers) - set(map(int, a)))

#Задача 4
numbers = []
number = int(input())
while number != 0:
    numbers.append (number)
    number = int (input())
count = len(numbers)
a = [num for num in numbersа if num % count == 0]
print(a)

#Задача 5
print ('Введите количество флагов')
n = int(input(''))
print ('Введите какие будут цвета')
flag = [input('') for _ in range(n)]
print ('Количество флагов в гирлянде')
a = int(input(''))
d, a2 = divmod(a,n)
print (*(flag*d+flag[:a2]),sep='\n')

#Задача 6
years = {"Proterozoic": range(635 * 10 ** 6, 2800 * 10 ** 6), "Cenozoic": range(0, 145 * 10 ** 6),
         "Mesozoic": range(145 * 10 ** 6, 300 * 10 ** 6), "Paleozoic": range(300 * 10 ** 6, 635 * 10 ** 6)}
while True:
    x = input('Укажите год: ')
    if x == "":
        break
    x = int(x) * 1000
    for i, val in years.items():
        if x in val:
            print(i)
            break
    else:
        print("Archaea")

#Задача 7
birds = {}
while True:
    observation = input()
    if observation == '':
        print(birds)
        break
    bird, count = observation.split(": ")
    if bird in birds:
        birds[bird] += int(count)
    else:
        birds[bird] = int(count)

#Задача 8
a= input('')
d = [*map( bin, map( int,a.split()))]
s = [{'digits':len(w)-2,'units':w.count('1'),'zeros':w.count('0')-1}for w in d]
print(s)

