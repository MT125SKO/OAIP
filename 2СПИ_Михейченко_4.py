#1
def horse2(pos):
    moves = []
    letters = ['a','b','c','d','e','f','g','h']
    col = letters.index(pos[0])
    row = int(pos[1])
    steps = [(-2, -1),(-2, 1),(-1, -2),(-1, 2),(1, -2),(1, 2),(2, -1),(2, 1)]

    for movement in steps:
        new_col = col + movement[0]
        new_row = row + movement[1]

        if new_col >= 0 and new_col <= 7 and new_row >= 1 and new_row <= 8:
            new_pos = letters[new_col] + str(new_row)
            moves.append(new_pos)
        return "\n".join(str(movement) for movement in moves)
print(horse2(input()))
#2
def template(side_1, side_2, side_3):
    if side_1+side_2 > side_3 and side_2+side_3 > side_1 and side_1 + side_3 > side_2:
        perimeter = side_1+side_2+side_3
        s = (side_1+side_2+side_3) / 2
        area = (s*(s - side_1)*(s - side_2)*(s - side_3)) ** 0.5
        is_isosceles = side_1 == side_2 or side_2 == side_3 or side_1 == side_3
        is_equilateral = side_1 == side_2 and side_2 == side_3
        print(f"Периметр:   {perimeter}")
        print(f"Площадь:    {area}")
        print(f"Равнобедренный: {'да'   if is_isosceles else 'нет'}")
        print(f"Равносторонний: {'да'   if is_equilateral else 'нет'}")
    else:
        print("No")
template(5, 4, 5)
template(2, 1, 3)
#3
def func_table(exp,x,y):
    res = [[eval(exp.replace('x',str(i)).replace('y',str(j))) for j in range(y + 1)] for i in range(x + 1)]
    for i in res:
        for j in i:
            print(j, end='\t')
        print()
x = 3
y = 5
func_table('x ** 2 + y', x, y)

