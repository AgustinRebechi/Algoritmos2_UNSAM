from typing import List

Matriz = List[List[int]]

def resolver_laberinto(laberinto: Matriz, x,y, solution,n):

    if x == n-1 and y == n-1 and laberinto[x][y] == 1:
        solution[x][y] = 1
        return True

    if is_safe(laberinto,x,y,n):
        solution[x][y] = 1

        if resolver_laberinto(laberinto, x+1,y, solution,n):
            return True
        if resolver_laberinto(laberinto, x, y+1, solution,n):
            return True
        if resolver_laberinto(laberinto, x - 1, y, solution, n):
            return True
        if resolver_laberinto(laberinto, x, y - 1, solution, n):
            return True

        # Backtracking
        laberinto[x][y] = 0
        return False
    return False


def is_safe(laberinto,x,y,n):
    if (0 <= x < n and
            0 <= y < n and
            laberinto[x][y] == 1 and
            solution[x][y] == 0):
        return True
    return False

lab= [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], # [0][0] es la Entrada
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # [9][9] es la Salida
]

n = len(lab)
solution = [[0 for _ in range(n)] for _ in range(n)]

if resolver_laberinto(lab,0,0,solution,n):
    for i in solution:
        for j in i:
            print(str(j),'',end='')
        print('')