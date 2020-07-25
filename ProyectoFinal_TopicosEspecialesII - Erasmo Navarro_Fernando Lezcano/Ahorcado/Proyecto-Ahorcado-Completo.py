import random
import time
import sys

#Elaborado por Erasmo Navarro y Fernando Lezcano

#Se realizan las imagenes para cada letra incorrecta
IMAGENES_AHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
 #Se añadió el menu :)
msg="************MENÚ PRINCIPAL**************\n"
msg1="ESCOJA EL TEMA (letra) DE SU PREFERENCIA\n"
print(msg.center(120," "))
print(msg1.center(120," "))
#time.sleep(1)
print()
choice = ""
while choice == "":
    choice = input("""
                                            A: Aves
                                            B: Flores
                                            C: Países de América
                                            D: Planetas
                                            Q: Salir

                                            Por favor, ingrese su elección: """)

   #y la opcion de tomar las listas desde archivos de texto :D
    if choice == "A" or choice =="a":
        tema = "Aves"
        stream = open("A.txt", "rt", encoding = "utf-8")
        lista = stream.read()
        words = lista.split()
    elif choice == "B" or choice =="b":
        tema = "Flores"
        stream = open("B.txt", "rt", encoding = "utf-8")
        lista = stream.read()
        words = lista.split()
    elif choice == "C" or choice =="c":
        tema = "Países de Centro América"
        stream = open("C.txt", "rt", encoding = "utf-8")
        lista = stream.read()
        words = lista.split()
    elif choice == "D" or choice =="d":
        tema = "Planetas"
        stream = open("D.txt", "rt", encoding = "utf-8")
        lista = stream.read()
        words = lista.split()
    elif choice=="Q" or choice=="q":
        sys.exit()
       #  os.system('cls') 
    else:
        choice = ""
        print("Solo debes seleccionar entre A,B,C, o D.\nIntenta de nuevo...\n")
        time.sleep(1)

#Inician las Funciones

def obtenerPalabraAlAzar(listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]
 
def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()
 
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
 
    espaciosVacíos = '_' * len(palabraSecreta)
 
    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
 
    for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()
 
def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento
 
def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

#Terminan las funciones
    
nomb=input("Introduzca su nombre... ")
time.sleep(0.5)
print("El tema es: " + tema)
time.sleep(1)
print(f"Preparate {nomb}, jugarás al A H O R C A D O, tienes 6 intentos...")
time.sleep(1)
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(words)
juegoTerminado = False
    
while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    
    # Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    
    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
    
        # Verifica si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print(f"¡Sí! ¡La palabra correcta es {palabraSecreta}! ¡Has ganado!")
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento
    
        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print(f"¡Te has quedado sin intentos! \nDespués de  {str(len(letrasIncorrectas))} intentos fallidos y {str(len(letrasCorrectas))} aciertos, la palabra era {palabraSecreta}")
            time.sleep(0.5)
            juegoTerminado = True
    # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(words)
        else:
            break
