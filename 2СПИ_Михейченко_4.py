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
