#1
lst = [("AA", 2, "AA"), ("DD", 1, "DD")];st = sorted(lst, key=lambda x: (x[2], x[1], len(x[0]), -x[1]))
print(st) 
#2
a = ('Expanding the space available for living').split()
print(*list(map(lambda d: d.rjust(len(max(a, key = len)), "*"), a)), sep = "\n")

#3
def nearby(data, places=1):
    return list(filter(lambda a: '0' * places in a, data))
data = ["100100011",
        "0001100001",
        "100001001",
        "1110010111"]
print(*nearby(data, places=4), sep='\n')