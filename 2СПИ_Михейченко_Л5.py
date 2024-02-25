#1
def groundhog_day(a):
    for d, (previous, current) in enumerate(zip(a, a[1:]), 1):
        res = [ d for d, (x, y) in enumerate(zip(previous, current)) if x !=y]
        if len(res) > 2:
            return (d,) + tuple(res)
    return (0, 0)

data = ["Groundhog Festival in Punxsutawney.",
        "Groundhog Festival in Punksutawney.",
        "Groundhog Festivel in Punxsutowney."]

print(groundhog_day(data))

#2
from fractions import Fraction
data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
def gears(a1, a2, a3):
    for lst1 in a1:
        for el1 in lst1:
            for lst2 in a1:
                for el2 in lst2:
                    if el2 != 0 and Fraction(el1, el2) == Fraction(a2, a3):
                        return el1, el2
print(gears(data, 30, 7))
print(gears(data, 60, 14))
#3
from collections import deque
line = "1{2 + [3}45 - 6] * (7 - 8) 9"
line2 = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
def staples(line2):
    a = {']':'[', ')':'(', '}':'{'}
    d = deque()
    for i in line2:
        if i in '[({':
            d.append(i)
        if i in '])}':
            if len(d):
                i = a[i]
                if i != d.pop():
                    return False
            else:
                return False
    if len(d):
        return False
    return True
print(staples(line))
print(staples(line2))