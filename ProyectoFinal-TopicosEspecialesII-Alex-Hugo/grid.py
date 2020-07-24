import pygame
import os
import tkinter as tk
from tkinter import messagebox
from input import inputbox
#Estas variables contienen las imagenes de X y O respectivamente

#ruta = os.path.abspath(os.path.dirname(__file__))


#Estas son as imagenes (Cambiar a su ruta actual)
letraX = pygame.image.load(os.path.join('C:\ProyectoTopicos-master\ProyectoFinal-TopicosEspecialesII\img','x.png'))
letraO = pygame.image.load(os.path.join('C:\ProyectoTopicos-master\ProyectoFinal-TopicosEspecialesII\img','o.png'))

class Grid:
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)), # primera linea horizontal
                           ((0,400), (600,400)), # segunda linea horizontal
                           ((200,0), (200,600)), # primera linea vertical
                           ((400,0), (400,600))] # segunda linea vertical

        self.grid = [[0 for x in range(3)] for y in range(3)]
        self.switch_player = True
        # direcciones         N         NW        W       SW       S       SE      E       NE
        self.search_dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        self.game_over = False



    def draw(self, surface): #Dibuja el grid y las X y O
        for line in self.grid_lines:
            pygame.draw.line(surface, (255,255,255), line[0], line[1], 2)

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == "X":
                    surface.blit(letraX, (x*200, y*200))
                elif self.get_cell_value(x, y) == "O":
                    surface.blit(letraO, (x*200, y*200))


    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def get_mouse(self, x, y, player, a): #Obtiene el valor de X o O y verifica que responda bien
        if a == 1:
            if self.get_cell_value(x, y) == 0:
                self.switch_player = True
                if player == "X":
                    self.set_cell_value(x, y, "X")
                elif player == "O":
                    self.set_cell_value(x, y, "O")
                self.check_grid(x, y, player)
            else:
                self.switch_player = False
        elif a == 2:
            self.switch_player = True

    def is_within_bounds(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def check_grid(self, x, y, player): #Verifica quien gana
        count = 1
        for index, (dirx, diry) in enumerate(self.search_dirs):
            if self.is_within_bounds(x+dirx, y+diry) and self.get_cell_value(x+dirx, y+diry) == player:
                count += 1
                xx = x + dirx
                yy = y + diry
                if self.is_within_bounds(xx+dirx, yy+diry) and self.get_cell_value(xx+dirx, yy+diry) == player:
                    count += 1
                    if count == 3:
                        break
                if count < 3:
                    new_dir = 0
                    # mapping the indices to opposite direction: 0-4 1-5 2-6 3-7 4-0 5-1 6-2 7-3
                    if index == 0:
                        new_dir = self.search_dirs[4] # N to S
                    elif index == 1:
                        new_dir = self.search_dirs[5] # NW to SE
                    elif index == 2:
                        new_dir = self.search_dirs[6] # W to E
                    elif index == 3:
                        new_dir = self.search_dirs[7] # SW to NE
                    elif index == 4:
                        new_dir = self.search_dirs[0] # S to N
                    elif index == 5:
                        new_dir = self.search_dirs[1] # SE to NW
                    elif index == 6:
                        new_dir = self.search_dirs[2] # E to W
                    elif index == 7:
                        new_dir = self.search_dirs[3] # NE to SW

                    if self.is_within_bounds(x + new_dir[0], y + new_dir[1]) \
                            and self.get_cell_value(x + new_dir[0], y + new_dir[1]) == player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1

        if count == 3:
            print(player, 'wins!')
            self.game_over = True
            #messagebox.showinfo(message=player+" ganó",title="GANADOR!!!!!!!!!")

        else:
            self.game_over = self.is_grid_full()


    def is_grid_full(self): #Verifica que el grid esté lleno
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
        return True

    def clear_grid(self): #limpia el grid
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.set_cell_value(x, y, 0)

    def print_grid(self): #Imprime el grid
        for row in self.grid:
            print(row)
