#Задача 1

film = input('Введите название фильма ')
theatre = input('Введите имя кинотеатра ')
time = input('Введите время ')
print("Билет на", film, "в", theatre, "на", time, "забронирован")

#Задача 2
print ("ведите заплату"),
te = int (input ())
print ("число отрабатанных выходных часов: ")
t2 = int (input())
print ("доплата сотруднику"),
tt = (te*00.1)
y5 = (tt*t2)
print (y5)
#Задача 3
print ("введите сумму")
p = int (input (">>>"))
a = p // 1000
aa= p % 1000
b = aa // 100
bb = aa  % 100
c = bb // 10
cc = bb % 10
d = cc // 1
print (d, "- по 1р")
print (c, "- по 10р")
print (d, "- по 100р")
print (a, "- по 1000р")
#Задача 4 Используется find 
a = input ("Оцените развлекательный комплекс:\n>>>")
a2 = a .find ('весело')
a3 = a .find ('увлекательно')
a4 = a .find ('развлечения')
print ("Результат анализа:", a2, a3, a4 )
#Задача 5
while True:
    a = input()
    print(a[-(len(a) // 2) - 1])

#Задача 6
a = 'Алиса и Вася, большое спасибо за теплый приём!'
a2 = a[0:5]
dd = a[8:12]
print ('Назначить премию:', a2 + '/' + dd)
#Задача 7
while True:
    a = int (input('a = '))
    s = ''
    for i in range (a-1, a+3):
        s += chr (ord('c') + i%26)
    print(s)
#Задача 8
# Создание списка
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n.pop(8)  # Удаление элемента
num = n[3:7] # # Срез
n.reverse() # Перевернуть список
numb = n[::-1] # Сделать двумерный список
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1]) # Вывод цифры 5 из списка 2
n.clear() # Очистка
#Задача 9
a = tuple()
w = ('12', '23', '25','1243','36437')
#Задача 10
a = set () # пустое множество
a = set ('ffff') # Создаем множество с элементами
a.update ('dsf', 'djh')
d3 = {1, 2, 3} # Операции над множествами
mr = {2, 3, 4, 5, 6, 7, 8 ,9 ,10}
w = d3.union (mr)
w = d3.intersection (mr)
w = d3.difference (mr)
w = d3.symmetric_difference (mr)
#Задача 11
some_dict = {} # Создать пустой словарь
some_dict = {'car1': 'mark2', 'car2': 'chaser'} #Создать словарь с элементами
some_dict['car3'] = 'supra A70' #Добавить значение
del some_dict['car2'] #Удалить значение
some_dict['car2'] = 'supra A80' #Изменить значение




