import random, os, time, math

def factorizacion_forma():
    #Función Aleatorio 
    def aleatorio(a,b):
        num= random.randint(a,b)  #Genera número aleatorios enteros
        return (num) #Regresa la variable num
    
    def revision(n1,n2,c,d):
        if n1*n2 == c*d and n1+n2 == c+d:  #revisa si los valores introducidos son los correctos
            mensaje = 'Excelente ^-^' #Mensaje de afirmación
        else:
            mensaje = 'Intenta de nuevo' #Mensaje de negación
        return(mensaje) #Regresa el mensaje correspondiente 
    
    #Función para seleccionar el nivel
    def nivel(numero):
        if numero == 1:  #Si se selecciona la opción 1
            return(1,10) #Envia de regreso los valores entre 1 y 10
        elif numero == 2: #Si se selecciona la opción 2
            return(1,20) #Envia de regreso los valores entre 1 y 20
        elif numero == 3: #Si se selecciona la opción 3
            return(1,30) #Envia de regreso los valores entre 1 y 30
        
    os.system('cls')   #Función usada para limpiar la consola
    print()
    #Se guarda los mensajes en variables separadas
    msg1 = "¡¡Excelente!! Factorizaciones de la forma x^2+bx+c"
    msg2 = "Tienes 3 oportunidades para acertar"
    msg3 = "Selecciona tu nivel"
    opc1 = "1. Números entre 1 y 10"
    opc2 = "2. Números entre 1 y 20"
    opc3 = "3. Números entre 1 y 30"
    #Esto es para poder imprimir el mensaje de la cadena y poder centrarlo
    print(msg1.center(120, " "))
    print()
    time.sleep(2)  #La función sleep es para dar un retrasa a la ejecución
    print(msg2.center(120, " "))
    #Se hace lo mismo para centrar el texto, hay que tener en cuenta que el valor de 120 puede variar
    print()
    time.sleep(2)
    print(msg3.center(120, " "))
    print(opc1.center(120, " "))
    print(opc2.center(120, " "))
    print(opc3.center(120, " "))
    #Se pide la eleccion y se asigna lo que devuelve la funcion nivel a las variables a y b
    try:
        selecc = int(input("¿Cúal es tu selección? "))
        a,b = nivel(selecc)  
        #Se generan los valores aleatorios
        c=aleatorio(a,b)
        d=aleatorio(a,b)    
        vidas=3  #Se define la cantidad de vidas que tendra el jugador
        while vidas>0:  #Mientras las vidas sean mayor que cero
            print("\n\n")
            incog = 'x'+chr(178)  
            print("Factorice")
            #Se imprime la ecuación en formato matemático
            print(incog,'+',c+d,"x +",c*d) 
            
            #Lectura de números
            x1 = 'x'+chr(8321) 
            x2 = 'x'+chr(8322) 
            print()
            #Se introducen los factores
            n1=int(input("Introduzca el valor de "+x1+"= ")) 
            n2=int(input("Introduzca el valor de "+x2+"= "))
            print(revision(n1,n2,c,d)) #Se imprime la respuesta que devuelve la función revisión
    
            if revision(n1,n2,c,d) == 'Intenta de nuevo': #Si lo que devuelve revisión es igual a la cadena
                vidas -= 1 #Se resta una vida
                print("Vidas restantes:", vidas) #Se imprime la cantidad de vidas restantes
                input()
                if(vidas == 0): #Si las vidas son igual a 0
                    print("La factores correctos son: (x +"+str(c)+") (x +"+str(d)+")") #Se imprime la respuesta correcta al jugador
                    input()
                    os.system('cls') #Se limpia la pantalla de la consola
            elif revision(n1,n2,c,d) == 'Excelente ^-^': #En caso de que la revisión devuelva la cadena positiva
                print()
                op = input("Felicidades, ¿Deseas intentar nuevamente? (y/n): ") #Se pregunta si el usuario quiere continuar o no
                if op == 'n': #En el caso de darle a no
                    break #Se rompe el ciclo y vuelve al menú principal
                    os.system('cls') #Se limpia la pantalla de la consola
                elif op == 'y': #En el caso de que diga que sí
                    try:
                        selecc = int(input("¿Cúal es tu selección? "))
                        a,b = nivel(selecc)  
                        #Se generan los valores aleatorios
                        c=aleatorio(a,b)
                        d=aleatorio(a,b)
                    except ValueError:
                        print("Introduzca una elección válida")
                        break
                else:
                    print("Introduzca una opción correcta")
                    break
                print()                    
        print("Gracias por participar!!") #Impresión de despedida del modo de juego
        print()
    except ValueError:
        print("Introduzca una elección válida")

def factorizacion_trinomio():
    #Función Aleatorio 
    def aleatorio2(a,b):
        num= random.randint(a,b)  #Genera número aleatorios enteros
        return (num) #Regresa la variable num
    
    def revision2(n1,n2,c,d):
        if (n1**2 == c**2 or n1**2 == d**2) and (n2**2 == c**2 or n2**2 == d**2) and (2*n1*n2== 2*c*d):  #revisa si los valores introducidos son los correctos
            mensaje = 'Excelente ^-^' #Mensaje de afirmación
        else:
            mensaje = 'Intenta de nuevo' #Mensaje de negación
        return(mensaje) #Regresa el mensaje correspondiente
    #Función para seleccionar el nivel
    def nivel2(numero):
        if numero == 1:  #Si se selecciona la opción 1
            return(1,10) #Envia de regreso los valores entre 1 y 10
        elif numero == 2: #Si se selecciona la opción 2
            return(1,20) #Envia de regreso los valores entre 1 y 20
        elif numero == 3: #Si se selecciona la opción 3
            return(1,30) #Envia de regreso los valores entre 1 y 30
    os.system('cls')   #Función usada para limpiar la consola
    print()
    #Se guarda los mensajes en variables separadas
    msg1 = "¡¡Vamos a practicar factorizaciones de trinomio cuadrado perfecto!!"
    msg2 = "Tienes 3 oportunidades para acertar"
    msg3 = "Selecciona tu nivel"
    opc1 = "1. Números entre 1 y 10"
    opc2 = "2. Números entre 1 y 20"
    opc3 = "3. Números entre 1 y 30"
    #Esto es para poder imprimir el mensaje de la cadena y poder centrarlo
    print(msg1.center(120, " "))
    print()
    time.sleep(2)  #La función sleep es para dar un retrasa a la ejecución
    print(msg2.center(120, " "))
    #Se hace lo mismo para centrar el texto, hay que tener en cuenta que el valor de 120 puede variar
    print()
    time.sleep(2)
    print(msg3.center(120, " "))
    print(opc1.center(120, " "))
    print(opc2.center(120, " "))
    print(opc3.center(120, " "))
    #Se pide la eleccion y se asigna lo que devuelve la funcion nivel a las variables a y b
    try:
        selecc = int(input("¿Cúal es tu selección? "))
        a,b = nivel2(selecc)  
        #Se generan los valores aleatorios
        if selecc == 3:
            c=aleatorio2(a,b)
            d=(-1)*aleatorio2(a,b)
        else:
            c=aleatorio2(a,b)
            d=aleatorio2(a,b)
        vidas=3  #Se define la cantidad de vidas que tendra el jugador
        while vidas>0:  #Mientras las vidas sean mayor que cero
            incog = 'x'+chr(178)
            print("\n\n")
            print("Factorice")
            if selecc == 3:
                print(str(c**2)+incog+" ",str(2*c*d),"x +"+str(d**2))
            else:
                print(str(c**2)+incog+" +",str(2*c*d),"x +"+str(d**2))
            print()
            #Se introducen los factores
            n1=int(input("Introduzca el valor de a = "))
            n2=int(input("Introduzca el valor de b = "))
            print(revision2(n1,n2,c,d)) #Se imprime la respuesta que devuelve la función revisión
            if revision2(n1,n2,c,d) == 'Intenta de nuevo': #Si lo que devuelve revisión es igual a la cadena
                vidas -= 1 #Se resta una vida
                print("Vidas restantes:", vidas) #Se imprime la cantidad de vidas restantes
                input()
                if(vidas == 0): #Si las vidas son igual a 0
                    squad = chr(178)
                    if selecc == 3:
                        print("La factorización resultante correcta es: ("+str(c)+"x "+str(d)+")"+squad)#Se imprime la respuesta correcta al jugador
                    else:
                        print("La factorización resultante correcta es: ("+str(c)+"x +"+str(d)+")"+squad) #Se imprime la respuesta correcta al jugador
                    input()
                    os.system('cls') #Se limpia la pantalla de la consola
            elif revision2(n1,n2,c,d) == 'Excelente ^-^': #En caso de que la revisión devuelva la cadena positiva
                print()
                op = input("Felicidades, ¿Deseas intentar nuevamente? (y/n): ") #Se pregunta si el usuario quiere continuar o no
                if op == 'n': #En el caso de darle a no
                    break #Se rompe el ciclo y vuelve al menú principal
                    os.system('cls') #Se limpia la pantalla de la consola
                elif op == 'y': #En el caso de que diga que sí
                    try:
                        selecc = int(input("¿Cúal es tu selección? "))
                        if selecc == 3:
                            c=aleatorio2(a,b)
                            d=(-1)*aleatorio2(a,b)
                        else:
                            c=aleatorio2(a,b)
                            d=aleatorio2(a,b)
                    except ValueError:
                        print("Introduzca una elección válida")
                        break
                else:
                    print("Introduzca una opción correcta")
                    break   
                print()                    
        print("Gracias por participar!!") #Impresión de despedida del modo de juego
        print()
    except ValueError:
        print("Introduzca una elección válida")

def factorizacion_diferencia_de_cuadrado():
    #Función Aleatorio 
    def aleatorio3(a,b):
        num= random.randint(a,b)  #Genera número aleatorios enteros
        return (num) #Regresa la variable num
    
    def revision3(n1,n2,c,d):
        if (n1**2 == c**2 or n1**2 == d**2) and (n2**2==c**2 or n2**2==d**2):  #revisa si los valores introducidos son los correctos
            mensaje = 'Excelente ^-^' #Mensaje de afirmación
        else:
            mensaje = 'Intenta de nuevo' #Mensaje de negación
        return(mensaje) #Regresa el mensaje correspondiente

    #Función para seleccionar el nivel
    def nivel3(numero):
        if numero == 1:  #Si se selecciona la opción 1
            return(1,10) #Envia de regreso los valores entre 1 y 10
        elif numero == 2: #Si se selecciona la opción 2
            return(1,20) #Envia de regreso los valores entre 1 y 20
        elif numero == 3: #Si se selecciona la opción 3
            return(1,30) #Envia de regreso los valores entre 1 y 30
    os.system('cls')   #Función usada para limpiar la consola
    print()
    #Se guarda los mensajes en variables separadas
    msg1 = "¡¡Excelente!! Diferencia de cuadrado"
    msg2 = "Tienes 3 oportunidades para acertar"
    msg3 = "Selecciona tu nivel"
    opc1 = "1. Números entre 1 y 10"
    opc2 = "2. Números entre 1 y 20"
    opc3 = "3. Números entre 1 y 30"
    #Esto es para poder imprimir el mensaje de la cadena y poder centrarlo
    print(msg1.center(120, " "))
    print()
    time.sleep(2)  #La función sleep es para dar un retrasa a la ejecución
    print(msg2.center(120, " "))
    #Se hace lo mismo para centrar el texto, hay que tener en cuenta que el valor de 120 puede variar
    print()
    time.sleep(2)
    print(msg3.center(120, " "))
    print(opc1.center(120, " "))
    print(opc2.center(120, " "))
    print(opc3.center(120, " "))
    #Se pide la eleccion y se asigna lo que devuelve la funcion nivel a las variables a y b
    try:
        selecc = int(input("¿Cúal es tu selección? "))
        a,b = nivel3(selecc)  
        #Se generan los valores aleatorios
        c=aleatorio3(a,b)
        d=aleatorio3(a,b)    
        vidas=3  #Se define la cantidad de vidas que tendra el jugador
        while vidas>0:  #Mientras las vidas sean mayor que cero
            print("\n\n")
            incog = 'x'+chr(178)  
            print("Factorice")
            #Se imprime la ecuación en formato matemático
            print(c**2,incog,'-',d**2)
            #Se introducen los factores
            n1=int(input("Introduzca el coeficiente a = "))
            n2=int(input("Introduzca el coeficiente b = "))
            print(revision3(n1,n2,c,d)) #Se imprime la respuesta que devuelve la función revisión
            if revision3(n1,n2,c,d) == 'Intenta de nuevo': #Si lo que devuelve revisión es igual a la cadena
                vidas -= 1 #Se resta una vida
                print("Vidas restantes:", vidas) #Se imprime la cantidad de vidas restantes
                input()
                if(vidas == 0): #Si las vidas son igual a 0
                    print("La factores correctos son: ("+str(c)+"x +"+str(d)+") ("+str(c)+"x-"+str(d)+")") #Se imprime la respuesta correcta al jugador
                    input()
                    os.system('cls') #Se limpia la pantalla de la consola
            elif revision3(n1,n2,c,d) == 'Excelente ^-^': #En caso de que la revisión devuelva la cadena positiva
                print()
                op = input("Felicidades, ¿Deseas intentar nuevamente? (y/n): ") #Se pregunta si el usuario quiere continuar o no
                if op == 'n': #En el caso de darle a no
                    break #Se rompe el ciclo y vuelve al menú principal
                    os.system('cls') #Se limpia la pantalla de la consola
                elif op == 'y': #En el caso de que diga que sí
                    try:
                        selecc = int(input("¿Cúal es tu selección? "))
                        a,b = nivel3(selecc)  
                        #Se generan los valores aleatorios
                        c=aleatorio3(a,b)
                        d=aleatorio3(a,b)
                    except ValueError:
                        print("Introduzca una elección válida")
                        break
                else:
                    print("Introduzca una opción correcta")
                    break
                print()                    
        print("Gracias por participar!!") #Impresión de despedida del modo de juego
        print()
    except ValueError:
        print("Introduzca una elección válida")
            
def FormulaGeneral():    
    def respuesta1(a,b,c):
        x1 = 'x'+chr(8321) 
        resp1=round((-b+(math.sqrt((b**2)-(4*a*c))))/(2*a),2)
        res = x1+"="+str(resp1)
        return(res)   
    def respuesta2(a,b,c):
        x2 = 'x'+chr(8322)
        resp2=round((-b-(math.sqrt((b**2)-(4*a*c))))/(2*a),2)
        res2 = x2+'='+str(resp2)
        return(res2)
        
    os.system('cls')   #Función usada para limpiar la consola
    print()
    #Se guarda los mensajes en variables separadas
    msg1 = "Bienvenido a la sección de ayuda de factorizaciones usando fórmula general"
    msg2 = "Puedes hallar los factores que no sabes cómo encontrar fácilmente"
    msg3 = "Introduzca los coeficientes de la ecuación cuadrática"
    #Esto es para poder imprimir el mensaje de la cadena y poder centrarlo
    print(msg1.center(120, " "))
    print()
    time.sleep(2)  #La función sleep es para dar un retrasa a la ejecución
    print(msg2.center(120, " "))
    #Se hace lo mismo para centrar el texto, hay que tener en cuenta que el valor de 120 puede variar
    print()
    time.sleep(2)
    print(msg3.center(120, " "))
    incog = 'x'+chr(178)
    a = int(input("Coeficiente a: "))
    b = int(input("Coeficiente b: "))
    c = int(input("Coeficiente c: "))
    print()
    while True:
        if b<0:
            if c<0:
                print("La ecuación queda así: "+ str(a)+incog+" "+str(b)+"x "+str(c))
            else:
                print("La ecuación queda así: "+ str(a)+incog+" "+str(b)+"x +"+str(c))
        else:
            print("La ecuación queda así: "+ str(a)+incog+" +"+str(b)+"x +"+str(c))
        time.sleep(2)   
        print("Procederemos a resolver su ecuación, espere...")
        try:
            time.sleep(3)
            print("Gracias por esperar, aquí están los factores")
            print(respuesta1(a,b,c))
            print(respuesta2(a,b,c))
            input()
            opc = input("¿Quiere intentar con otra ecuación? (y/n) ")
            if opc == 'n':
                break
                os.system('cls')
            elif opc == 'y':
                try:
                    a = int(input("Coeficiente a: "))
                    b = int(input("Coeficiente b: "))
                    c = int(input("Coeficiente c: "))
                except ValueError:
                    print("Introduzca un valor válido")
                    
        except ZeroDivisionError:
            print("La división entre cero es imposible")
            break
        except ValueError:
            print("Algo esta mal con la ecuación")
            break
        

#############################################################################################

while True:
    titulo = "Math Factors".upper() #Titulo del juego guardado en una variable para darle formato mayúscula cerrada
    print (titulo.center(120," ")) #Se centra el título
    print()
    #Igualmente se guardan los mensajes en variables
    nivel_1 = "1. Nivel Básico (Trinomio Forma x^2+bx+c)"
    nivel_2 = "2. Nivel Medio (Diferencia de cuadrados)" 
    nivel_3 = "3. Nivel Dificil (Trinomio Cuadrado Perfecto)"
    extra = "4. Calculadora de Fórmula General"    
    salir= "5. Salir"
    #Para poder imprimir los mensajes centrados
    print(nivel_1.center(125," "))
    print(nivel_2.center(123," "))
    print(nivel_3.center(129," "))
    print(extra.center(118," "))
    print()
    print(salir.center(92," "))
    print()
    op = input("Opción elegida (1,2,3,4,5): ")
    if op == '1':    #Si se elege la opción 1
        #Se hace el llamado a la función factorizacion_forma()                        
        factorizacion_forma()  
        input()
        os.system('cls') 
    elif op == '2':        #Si se elige la opción 2   
        #Se hace el llamado a la función factorizacion_diferencia_de_cuadrado()          
        factorizacion_diferencia_de_cuadrado()
        input()
        os.system('cls')
    elif op == '3':       #Si elige la opción 3  
        #Se hace el llamado a la función factorizacion_trinomio() 
        factorizacion_trinomio()  
        input()
        os.system('cls')
    elif op == '4':      #Si elige la opción 4   
        #Se hace el llamado a la función formulageneral()
        FormulaGeneral()
        input()
        os.system('cls')
    elif op == '5':   #Si elige la opción 5                         
            print("¡Gracias por jugar!")      #Manda un mensaje de despedida del juego    
            break                           #Se se cierra el juego    
    else:
        print("Introduzca una opción correcta")    #Manda un mensaje de error
        time.sleep(2)
        os.system('cls')
