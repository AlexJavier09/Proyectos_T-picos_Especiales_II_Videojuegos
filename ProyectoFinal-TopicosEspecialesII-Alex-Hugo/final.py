import pygame #ESTA LIBRERÍA ES EL MOTOR DEL JUEGO
import os #ESTA NOS PERMITE LA POSICIÓN DE LAS VENTANAS
import tkinter as tk
from tkinter import messagebox
#from tkinter import messagebox
import input as IN

from grid import Grid #Importamos nuestra clase que dibuja la cuadrícula

#master = tk.Tk()

os.environ['SDL_VIDEO_WINDOW_POS'] = '400, 100' #Esta es la posición de la ventana (X, Y)

surface = pygame.display.set_mode((600,600)) #Esta variable es la que muestra la ventana
pygame.display.set_caption('Tic tac toe') #Este es el título de la ventana


grid = Grid() #Esta variable es de tipo Grid, es la que conecta nuestra libreria con el proyecto

#grid.set_cell_value(1, 1, 'x')


running = True

player = "X"

## ESTE CICLO ES EL QUE CREA LA VENTANA DEL JUEGO
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: #Esto verifica que solo se pueda utilizar el click izquierdo
                pos = pygame.mouse.get_pos() #Esta variable toma la posición (X, Y) del mouse
                a = IN.inputbox()
                #print (a)

                grid.get_mouse(pos[0] // 200, pos[1] // 200, player, a)

                if grid.switch_player:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"

                grid.print_grid()
                print("\n")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                IN.resetList()
                grid.game_over = False
            elif event.key == pygame.K_SPACE:
                running = False




    surface.fill((0,0,0)) #Esto es el color del tablero
    grid.draw(surface)
    pygame.display.flip()
