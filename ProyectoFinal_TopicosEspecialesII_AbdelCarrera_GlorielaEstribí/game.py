import pygame, random
from menu import Menu

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

class Game(object):
    def __init__(self):
        # Crea un nuevo font object
        self.font = pygame.font.Font(None,65)
        # Crea un font para el mensaje de score
        self.score_font = pygame.font.Font("kenvector_future.ttf",20)
        # Crea un diccionario con las llaves num1, num2,result que seran usadas para crear los problemas aritmeticos
        self.problem = {"num1":0,"num2":0,"result":0}
        # Crea una variable que contiene el nombre de la operacion
        self.operation = ""
        self.symbols = self.get_symbols()
        self.button_list = self.get_button_list()
        self.reset_problem = False
        # Crea el menu principal
        items = ("Suma","Resta","Multiplicacion","Division")
        self.menu = Menu(items,ttf_font="XpressiveBlack Regular.ttf",font_size=50,font_color=BLUE)
        # True: muestra el menu
        self.show_menu = True
        # Crea el contador del score
        self.score = 0
        # Cuenta el numero de problemas
        self.count = 0
        # Carga el fondo
        self.background_image = pygame.image.load("background.jpeg").convert()
         # Carga los sonidos que vamos a utilizar
        self.correct = pygame.mixer.Sound("correct.ogg")
        self.wrong = pygame.mixer.Sound("wrong.ogg")

    def get_button_list(self):
        """ Devuelve una lista con 4 botones """
        button_list = []
        # Asigna uno de los botones como la respuesta correcta
        choice = random.randint(1,4)
        # define las dimensiones
        width = 100
        height = 100
        # t_w: ancho total
        t_w = width * 2 + 50
        posX = (SCREEN_WIDTH / 2) - (t_w /2)
        posY = 150
        if choice == 1:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150
        
        if choice == 2:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w /2)
        posY = 300

        
        if choice == 3:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150
            
        if choice == 4:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        return button_list
    

    def get_symbols(self):
        """ Crea un diccionario con los simbolos de las operaciones """
        symbols = {}
        sprite_sheet = pygame.image.load("symbols.png").convert()
        image = self.get_image(sprite_sheet,0,0,64,64)
        symbols["addition"] = image
        image = self.get_image(sprite_sheet,64,0,64,64)
        symbols["subtraction"] = image
        image = self.get_image(sprite_sheet,128,0,64,64)
        symbols["multiplication"] = image
        image = self.get_image(sprite_sheet,192,0,64,64)
        symbols["division"] = image
        
        return symbols

    def get_image(self,sprite_sheet,x,y,width,height):
        """ Este metodo recortara una imagen y la devolvera """
        # Crea una imagen en blanco
        image = pygame.Surface([width,height]).convert()
        image.blit(sprite_sheet,(0,0),(x,y,width,height))
        # Devuelve la imagen
        return image

    def addition(self):
        """ Setea num 1, num 2 y result para la suma """
        a = random.randint(0,100)
        b = random.randint(0,100)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a + b
        self.operation = "addition"

    def subtraction(self):
        """ Setea num 1, num 2 y result para la resta """
        a = random.randint(0,100)
        b = random.randint(0,100)
        if a > b:
            self.problem["num1"] = a
            self.problem["num2"] = b
            self.problem["result"] = a - b
        else:
            self.problem["num1"] = b
            self.problem["num2"] = a
            self.problem["result"] = b - a
        self.operation = "subtraction"
            

    def multiplication(self):
        """ Setea num 1, num 2 y result para la multiplicacion """
        a = random.randint(0,12)
        b = random.randint(0,12)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a * b
        self.operation = "multiplication"

    def division(self):
        """ Setea num 1, num 2 y result para la division """
        divisor = random.randint(1,12)
        dividend = divisor * random.randint(1,12)
        quotient = dividend // divisor
        self.problem["num1"] = dividend
        self.problem["num2"] = divisor
        self.problem["result"] = quotient
        self.operation = "division"

    def check_result(self):
        """ Verifica el resultado al hacer click en un boton """
        for button in self.button_list:
            if button.isPressed():
                if button.get_number() == self.problem["result"]:
                    # Hace que el boton se ponga en verde cuando es correcto
                    button.set_color(GREEN)
                    # Incrementa el puntaje
                    self.score += 5
                    # Reproduce un sonido
                    self.correct.play()
                else:
                    # Hace que el boton se ponga en rojo cuando es incorrecto
                    button.set_color(RED)
                    # Reproduce un sonido
                    self.wrong.play()
                # True para que vuelva a cargar otro problema
                self.reset_problem = True

    def set_problem(self):
        """ Crear el siguiente problema """ 
        if self.operation == "addition":
            self.addition()
        elif self.operation == "subtraction":
            self.subtraction()
        elif self.operation == "multiplication":
            self.multiplication()
        elif self.operation == "division":
            self.division()
        self.button_list = self.get_button_list()
        
        

    def process_events(self):
        for event in pygame.event.get():  # Si el usuario hizo algo
            if event.type == pygame.QUIT: # Si el usuario hizo click en cerrar
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_menu:
                    if self.menu.state == 0:
                        self.operation = "addition"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 1:
                        self.operation = "subtraction"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 2:
                        self.operation = "multiplication"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 3:
                        self.operation = "division"
                        self.set_problem()
                        self.show_menu = False
                
                # check_result verifica si el usuario contesto bien el problema
                else:
                    self.check_result()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu = True
                    self.score = 0
                    self.count = 0

        return False

    def run_logic(self):
        # Actualiza el menu
        self.menu.update()

        
    def display_message(self,screen,items):
        """ Muestra cada cadena que esta dentro de una tupla """
        for index, message in enumerate(items):
            label = self.font.render(message,True,BLACK)
            # Alto y ancho de la etiqueta
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: Altura total del text block
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
              

    def display_frame(self,screen):
        # Dibuja la imagen de fondo
        screen.blit(self.background_image,(0,0))
        time_wait = False
        if self.show_menu:
            self.menu.display_frame(screen)
        elif self.count == 20:
            # Cuando este contador llega a 20 significa que el juego ha acabado
            #Le dira al usuario su puntaje y cuantas preguntas acerto correctamente
            msg_1 = "Contestaste " + str(self.score // 5) + " bien"
            msg_2 = "Tu puntaje es " + str(self.score)
            self.display_message(screen,(msg_1,msg_2))
            self.show_menu = True
            # reset score y contador a 0
            self.score = 0
            self.count = 0
            # Espera 3 segundos
            time_wait = True
        else:
            # Crea etiquetas para cada numero
            label_1 = self.font.render(str(self.problem["num1"]),True,BLACK)
            label_2 = self.font.render(str(self.problem["num2"])+" = ?",True,BLACK)
            # t_w: ancho total
            t_w = label_1.get_width() + label_2.get_width() + 64 # 64: length of symbol
            posX = (SCREEN_WIDTH / 2) - (t_w / 2)
            screen.blit(label_1,(posX,50))
            # imprime el simbolo en pantalla
            screen.blit(self.symbols[self.operation],(posX + label_1.get_width(),40))
            
            screen.blit(label_2,(posX + label_1.get_width() + 64,50))
            # Recorre la lista de botones y los dibuja
            for btn in self.button_list:
                btn.draw(screen)
            # Muestra la puntuacion
            score_label = self.score_font.render("Puntaje: "+str(self.score),True,BLACK)
            screen.blit(score_label,(50,10))
            
        # --- Actualiza la pantalla que se ha dibujado
        pygame.display.flip()
        # --- Espera unos segundos para poder mostrar lo que se ha dibujado antes de pasar al siguiente frame
        if self.reset_problem:
            # Espera 1 segundo
            pygame.time.wait(1000)
            self.set_problem()
            # Incrementa el contador en 1
            self.count += 1
            self.reset_problem = False
        elif time_wait:
            # Espera 3 segundos
            pygame.time.wait(3000)

class Button(object):
    def __init__(self,x,y,width,height,number):
        self.rect = pygame.Rect(x,y,width,height)
        self.font = pygame.font.Font(None,40)
        self.text = self.font.render(str(number),True,BLACK)
        self.number = number
        self.background_color = WHITE

    def draw(self,screen):
        """ Este metodo va a dibujar los botones en la pantalla """
        # Rellena la pantalla con el color de fondo selecciondo
        pygame.draw.rect(screen,self.background_color,self.rect)
        # Dibujara los bordes del boton
        pygame.draw.rect(screen,BLACK,self.rect,3)
        # Ancho y alto de la superficie del texto
        width = self.text.get_width()
        height = self.text.get_height()
        # Calcula posX y posY que son las posiciones donde se van a dibujar los botones
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        # Dibuja la imagen en la pantalla
        screen.blit(self.text,(posX,posY))

    def isPressed(self):
        """ Devuelve cierto si el mouse esta sobre el boton """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def set_color(self,color):
        """ Define el color de fondo"""
        self.background_color = color

    def get_number(self):
        """ Devuelve el numero del boton"""
        return self.number