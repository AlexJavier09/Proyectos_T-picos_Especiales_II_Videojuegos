import tkinter as tk
import random
from tkinter import messagebox

#Esta lista contiene las preguntas
preguntas = ["¿Quién fue el segundo presidente de Panamá?\nA. Federico Boyd\nB. José Domingo De Obaldía\nC. José Agustín Arango",
"                  ¿Cómo se llamó el periódico que narra con detalle el fusilamiento de Victoriano Lorenzo?\nA. La Prensa\nB. La Estrella de Panamá\nC. El Lápiz",
"¿Quien ideo el escudo Nacional?\nA. Don Santos Jorge A.\nB. Don Jerónimo de la Ossa\nC. Don Nicanor Villalaz",
"                           ¿Qué ciudadano istmeño empezó a trabajar en secreto la preparación del movimiento separatista?\nA. José Agustín Arango\nB. Tomas Herrera\nC. Ricardo Arias",
"¿Cuántos corregimientos tiene el país Panamá?\nA. 697\nB. 679\nC. 689",
"¿Cuántos corregimientos tiene la provincia de Chiriquí?\nA. 91\nB. 103\nC. 93",
"¿Cuál es la cabecera de Pinogana (Darién)?\nA. San Blas\nB. La Palma\nC. El Real de Santa María",
"¿Cuántos presidentes ha tenido panamá?\nA. 47\nB. 48\nC. 49",
"¿Cuántos años tiene el vicepresidente?\nA. 37\nB. 38\nC. 36",
"¿Cuánto mide en superficie Panamá en km 2?\nA. 75845\nB. 74865\nC. 77626",
"¿Qué serpiente no es venenosa?\nA. La X\nB. Patoca\nC. La Culebra",
"¿Cuál es el barco más grande que ha pasado por Panamá?\nA. Neo Panamax\nB. Nimitz\nC. Suezmax",
"¿Cuál es el día de la chiricanidad?\nA. 19 de marzo\nB. 26 de mayo\nC. 9 de abril",
"¿Cuántas islas tiene Panamá?\nA. 89 islas\nB. 76 islas\nC. 81 islas",
"¿Cuál fue el primer parque nacional de panamá?\nA. Parque internacional La Amistad\nB. Parque Nacional Portobelo\nC. Parque Nacional Altos de Campana",
"¿Cuál es primer museo de Panamá?\nA. Museo de Panamá la Vieja\nB. Museo Historia de Panamá\nC. Museo Belisario Porras",
"¿Quién fue el segundo jefe militar de Panamá?\nA. Omar Torrijos\nB. Manuel Noriega\nC. Florencio Flores",
"¿Cuántos expresidentes siguen con vida?\nA. 11\nB. 9\nC. 15",
"¿Cuándo ocurrió el incidente de la tajada de sandía?\nA. 15 de abril de 1856\nB. 7 de enero de 1846\nC. 18 de julio de 1862",
"¿Cuántas especies de anfibios hay registradas en Panamá?\nA. 359\nB. 143\nC. 221",
"¿En qué año se descubrió del istmo de Panamá?\nA. 1503\nB. 1492\nC. 1501"]


respuesta = ["B", "C", "C", "A", "B", "B", "C", "B", "A", "A", "C", "A", "B", "C", "C", "C", "C", "B", "A", "C", "C"]
#class inputbox():


#Esta variable contiene la cantidad de perguntas y respuestas
r = 20

a = 0 #Esta es una variable auxiliar que determina si el usuario responde correctamente o no

def inputbox(): #Esta funcion invoca nuestro inputbox
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 550, height = 300)
    canvas1.pack()
    entry1 = tk.Entry (root)
    canvas1.create_window(200, 140, window=entry1)

    p = random.randrange(r)



    label = tk.Label(root, text=str(preguntas[p]))
    canvas1.create_window(230, 30, window=label)


    def leer(): #Esta funcion almacena el valor de la respuesta
        #respu=True
        global a
        global r
        x1 = entry1.get()
        label1 = tk.Label(root, text=str(x1))
        if str(x1).upper() == respuesta[p]:
            messagebox.showinfo(message="Correcto", title="Respuesta")
            respuesta.pop(p)
            preguntas.pop(p)
            r-=1
            i = 1
            for items in preguntas:
                print(i,str(items))
                i+=1
            root.destroy()
            print(r)
            #respu = True
            a = 1
        else:
            #i = 1
            a = 2
            messagebox.showinfo(message="incorrecto", title="Respuesta")
            root.destroy()
            i = 1
            for items in preguntas:
                print(i,str(items))
                i+=1
            print(r)
            #respu = False

    button1 = tk.Button(text='Aceptar', command=leer) #Este es el boton que ejecuta la funcion de leer
    canvas1.create_window(200, 180, window=button1)

    root.mainloop()
    return a

def resetList(): #Esta funcion reinicia las listas a su estado original
    global preguntas
    global respuesta
    global r
    preguntas = ["¿Quién fue el segundo presidente de Panamá?\nA. Federico Boyd\nB. José Domingo De Obaldía\nC. José Agustín Arango",
    "                  ¿Cómo se llamó el periódico que narra con detalle el fusilamiento de Victoriano Lorenzo?\nA. La Prensa\nB. La Estrella de Panamá\nC. El Lápiz",
    "¿Quien ideo el escudo Nacional?\nA. Don Santos Jorge A.\nB. Don Jerónimo de la Ossa\nC. Don Nicanor Villalaz",
    "                           ¿Qué ciudadano istmeño empezó a trabajar en secreto la preparación del movimiento separatista?\nA. José Agustín Arango\nB. Tomas Herrera\nC. Ricardo Arias",
    "¿Cuántos corregimientos tiene el país Panamá?\nA. 697\nB. 679\nC. 689",
    "¿Cuántos corregimientos tiene la provincia de Chiriquí?\nA. 91\nB. 103\nC. 93",
    "¿Cuál es la cabecera de Pinogana (Darién)?\nA. San Blas\nB. La Palma\nC. El Real de Santa María",
    "¿Cuántos presidentes ha tenido panamá?\nA. 47\nB. 48\nC. 49",
    "¿Cuántos años tiene el vicepresidente?\nA. 37\nB. 38\nC. 36",
    "¿Cuánto mide en superficie Panamá en km 2?\nA. 75845\nB. 74865\nC. 77626",
    "¿Qué serpiente no es venenosa?\nA. La X\nB. Patoca\nC. La Culebra",
    "¿Cuál es el barco más grande que ha pasado por Panamá?\nA. Neo Panamax\nB. Nimitz\nC. Suezmax",
    "¿Cuál es el día de la chiricanidad?\nA. 19 de marzo\nB. 26 de mayo\nC. 9 de abril",
    "¿Cuántas islas tiene Panamá?\nA. 89 islas\nB. 76 islas\nC. 81 islas",
    "¿Cuál fue el primer parque nacional de panamá?\nA. Parque internacional La Amistad\nB. Parque Nacional Portobelo\nC. Parque Nacional Altos de Campana",
    "¿Cuál es primer museo de Panamá?\nA. Museo de Panamá la Vieja\nB. Museo Historia de Panamá\nC. Museo Belisario Porras",
    "¿Quién fue el segundo jefe militar de Panamá?\nA. Omar Torrijos\nB. Manuel Noriega\nC. Florencio Flores",
    "¿Cuántos expresidentes siguen con vida?\nA. 11\nB. 9\nC. 15",
    "¿Cuándo ocurrió el incidente de la tajada de sandía?\nA. 15 de abril de 1856\nB. 7 de enero de 1846\nC. 18 de julio de 1862",
    "¿Cuántas especies de anfibios hay registradas en Panamá?\nA. 359\nB. 143\nC. 221",
    "¿En qué año se descubrió del istmo de Panamá?\nA. 1503\nB. 1492\nC. 1501"]
    respuesta = ["B", "C", "C", "A", "B", "B", "C", "B", "A", "A", "C", "A", "B", "C", "C", "C", "C", "B", "A", "C", "C"]
    r = 20
