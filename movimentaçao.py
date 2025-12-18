def movimentos_rei(x, y):
    return [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]

def movimentos_torre(x, y):
    return [(x, i) for i in range(8) if i != y] + [(i, y) for i in range(8) if i != x]

def movimentos_bispo(x, y):
    return [[(x+i, y+i) for i in range(1, 8) if x+i < 8 and y+i < 8] +
            [(x-i, y-i) for i in range(1, 8) if x-i >= 0 and y-i >= 0] +
            [(x+i, y-i) for i in range(1, 8) if x+i < 8 and y-i >= 0] +
            [(x-i, y+i) for i in range(1, 8) if x-i >= 0 and y+i < 8]][0]

print("Movimentos do Rei em (4,4):", movimentos_rei(4, 4))
print("Movimentos da Torre em (4,4):", movimentos_torre(4, 4))
print("Movimentos do Bispo em (4,4):", movimentos_bispo(4, 4))


