from random import choice
from time import sleep
from turtle import *

from freegames import floor, square, vector


# -------------------------------------------------
# Estado do jogo
# -------------------------------------------------
padrao = []
palpites = []
pontuacao = 0

azulejos = {
    vector(-400, 0): ('purple', 'darkslateblue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(0, 0): ('red', 'dark red'),
    vector(200, 0): ('orange', 'darkorange'),

    vector(-400, -200): ('pink', 'mediumorchid'),
    vector(-200, -200): ('aqua', 'darkturquoise'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(200, -200): ('yellow', 'khaki'),
}


# -------------------------------------------------
# Entrada e persistência
# -------------------------------------------------
def pedir_nome():
    return textinput("Jogador", "Digite seu nome:")


def registrar_pontuacao(nome, pontos):
    with open("pontuacoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}:{pontos}\n")


# -------------------------------------------------
# Interface
# -------------------------------------------------
def grade():
    for pos, cores in azulejos.items():
        square(pos.x, pos.y, 200, cores[1])
    update()


def piscar(pos):
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
    pos = choice(list(azulejos))
    padrao.append(pos)

    for pos in padrao:
        piscar(pos)

    palpites.clear()


def clique(x, y):
    global pontuacao

    onscreenclick(None)

    x = floor(x, 200)
    y = floor(y, 200)
    pos = vector(x, y)

    indice = len(palpites)

    # Errou
    if pos != padrao[indice]:
        registrar_pontuacao(nome_jogador, pontuacao)
        bye()
        return

    palpites.append(pos)
    piscar(pos)

    # Acertou a sequência inteira
    if len(palpites) == len(padrao):
        pontuacao += 1
        aumentar_sequencia()

    onscreenclick(clique)


def iniciar(x, y):
    aumentar_sequencia()
    onscreenclick(clique)


# -------------------------------------------------
# Inicialização
# -------------------------------------------------
setup(840, 420, 370, 0)
hideturtle()
tracer(False)

nome_jogador = pedir_nome()
pontuacao = 0

grade()
onscreenclick(iniciar)
mainloop()
