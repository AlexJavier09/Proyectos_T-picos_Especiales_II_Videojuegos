import pygame
from game import Game

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():
    # Inicializar los modulos de pygame importados
    pygame.init()
    # Definir las dimensiones de la pantalla, ancho y alto
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Titulo de la ventana
    pygame.display.set_caption("Math Games")
    #Bucle hasta que el jugador presione el boton para cerrar
    done = False
    # Se utiliza para controlar que tan rapido se actualiaza la pantalla
    clock = pygame.time.Clock()
    # Crear el objeto del juego
    game = Game()
    # -------- Programa principal -----------
    while not done:
        # --- Procesa eventos, como pulsaciones de teclado o clicks.
        done = game.process_events()
        # --- Se encarga de la logica del juego
        game.run_logic()
        # --- Dibuja el frame actual
        game.display_frame(screen)
        # --- Limita los frames por segundo a 30
        clock.tick(30)

    #Cerrar la ventana y salir, de olvidar esta linea el programa se quedara en stand by al salir
    pygame.quit()

if __name__ == '__main__':
    main()
