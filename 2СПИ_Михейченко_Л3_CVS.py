#1
with open ('tovars.csv', 'r', encoding = 'utf-8') as file:
    lines = sorted (file.readlines(), key = lambda x: float (x.strip().split(';')[1]))
    target = 1001
    result = []

    for line in lines:
        name, price = line.strip().split(';')
        try:
            price = float(price)
        except ValueError:
            print ('ERROR: нет такой цены.')
            exit()

        coust = min(10, int(target // price))

        if coust > 0:
            result.extend ([name] * coust)
            target -= coust * price

    if result:
        print (', '.join(result))
    else:
        print ('ERROR')

#2

limit = int(input("Введите пороговое значение процента выпускников: "))

with open('STYDENT.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        specialty = data[0]
        correct_summ = data[-1]

        if int(correct_summ) >= limit:
            print(specialty)

#3

with open('tovar2.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        if line.startswith('Name;'):
            continue

        data = line.strip().split(';')
        name = data[0]
        old_price = int(data[1])
        new_price = int(data[2])

        if new_price < old_price:
            print(name) 