import pygame


grid = [[0 for x in range(3)] for y in range(3)] #Esta sentencia crea las 3 tuplas
for row in grid:
    print(row)

print("\n")

grid[0][2]="X"
grid[0][0]="X"
grid[0][1]="X"

for item in grid:
    print(item)

print("\n")




grid2 = [["X" for x in range(3)] for y in range(3)] #Esta sentencia crea las 3 tuplas
for item in grid2:
    print(item)

print("\n")

"""def gamewin_check(grid1):

    grid = [[[x][y] for x in range(3)] for y in range(3)] #Esta sentencia crea las 3 tuplas


    for item in gamewinlist:
        gamewinlist_1 = [grid1[item[0]],grid1[item[1]],grid1[item[2]]]
        if gamewinlist_1 == ['X','X','X'] or gamewinlist_1 == ['O','O','O']:
            gamewincheck = True
            break
        else:
            gamewincheck = False
    return gamewincheck

print(gamewin_check(grid))"""
