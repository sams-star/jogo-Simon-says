from random import choice
from time import sleep
from turtle import *

from freegames import floor, square, vector


padrao = []
palpites = []

azulejos = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
    vector(-200, -400): ('pink', 'mediumorchid'),
    #vector(-400, 0): ('purple', 'darkslateblue'),
    #vector(-200, -200): ('aqua', 'darkturquoise'),
    #vector(-200, -200): ('orange', 'darkorange'),
}


# -------------------------------------------------
# Desenho da interface
# -------------------------------------------------
def grade():
    """Desenha o tabuleiro inicial."""
    # TODO:
    # Percorra o dicionário azulejos
    # e desenhe cada azulejo usando sua cor escura
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    square(-400, -200, 200, 'mediumorchid')
    square(-200, -200, 200, 'darklateblue')
    square(-200, -200, 200, 'darkturquoise')
    square(-200, -200, 200, 'darkorange')
    
    update()


def piscar(pos):
    """Pisca um azulejo."""
       # TODO:
    # 1. desenhe o azulejo com a cor clara
    # 2. espere um tempo
    # 3. desenhe o azulejo com a cor escura
    claro, escuro = azulejos[pos]
    square(pos.x, pos.y, 200, claro)
    update()
    sleep(0.2)
    square(pos.x, pos.y, 200, escuro)
    update()
    sleep(0.2)


# -------------------------------------------------
# Lógica do jogo
# -------------------------------------------------
def aumentar_sequencia():
    """Adiciona um azulejo ao padrão."""
    pos = choice(list(azulejos))
    padrao.append(pos)

    for pos in padrao:
        piscar(pos)

    palpites.clear()


def clique(x, y):
    """Responde ao clique do jogador."""
    onscreenclick(None)

    x = floor(x, 200)
    y = floor(y, 200)
    pos = vector(x, y)

    indice = len(palpites)

    # Condição de erro: clique incorreto
    if pos != padrao[indice]:
        bye()

    palpites.append(pos)
    piscar(pos)

    # Se o jogador completou a sequência,
    # o padrão cresce
    if len(palpites) == len(padrao):
        aumentar_sequencia()

    onscreenclick(clique)


def iniciar(x, y):
    aumentar_sequencia()
    onscreenclick(clique)


# -------------------------------------------------
# Configuração da janela
# -------------------------------------------------
setup(840, 420, 370, 0)
hideturtle()
tracer(False)

grade()
onscreenclick(iniciar)
mainloop()

