#1
def quarters(*tt):
    list = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
    for a, y in tt:
        if a > 0 and y > 0:
            list['I'] += 1
        elif a < 0 and y > 0:
            list['II'] += 1
        elif a < 0 and y < 0:
            list['III'] += 1
        elif a > 0 and y < 0:
            list['IV'] += 1
    return list
#.................................
from RET import quarters
list = [(1, 1), (-1, 2), (-3, -1)]
for a, d in sorted(quarters(*list).items()):
    print(f'{a}:\t{d}')


#2

def future(*mass, **const):
    quantity = 1
    for key, value in const.items():
        quantity *= float(value)
    summ = sum(mass) * quantity
    if summ > VIN:
        return 'ACCELERATION'
    elif summ < VIN:
        return 'DECELERATION'
    return 'UNCHANGED'
VIN=3
mass=[1,2,3,4]
const={'charge':1.6, 'alpha': 0.137, 'pi': 3.14}
print(future(*mass, **const))

#3
def circuit_resistance(*resis,road='serial'):
    if road =='serial':
        return sum(resis)
    elif road =='parallel':
        s = sum(map(lambda x: 1 / x, resis))
        return 1 / s
    else:
        raise ValueError("Bad connection type")
data=[10,20,30]
print(circuit_resistance(*data))
data=[30,30,30]
print(circuit_resistance(*data, road='parallel'))