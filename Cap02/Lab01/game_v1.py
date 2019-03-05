# Game Ping-Pong

# Importa modulos
from tkinter import *
import random
import time

# Atribui a level o valor inteiro lido pelo teclado do usuário
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
# Define tamanho da barra inversamento proporcional ao level
length = 500/level

# Cria uma aplicação Tkinter
root = Tk()
# Adiciona título à aplicação
root.title("Ping Pong")
# Faz a aplicação a janela de aplicação não ser redimensionável
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Cria uma caixa de desenho em formato quadrado 800x800
canvas = Canvas(root, width=800, height=800, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Declara variável inteira de "pontos"
count = 0
# Declara variável booleana de "Game over"
lost = False

class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # Declara lista de inteiros
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        # Define atributo x de bola como a primeira posição da lista starts_x
        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                # Incrementa a variável count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True


class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

# Inicia o jogo com 0 pontos (global = 0) e reseta status de game over (lost = False)
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(0.1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()