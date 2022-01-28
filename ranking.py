from PPlay.window import *
from PPlay.sprite import *
import dados


class Ranking(object):
    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.titulo = Sprite("./img/background/ranking.png")


    def run(self):
        namesVet = []
        pointsVet = []

        self.titulo.draw()

        ranking = open('ranking.txt', 'r')
        linhas = ranking.readlines()

        for i in range(len(linhas)):
            linha = linhas[i].split()
            namesVet.append(linha[0])
            pointsVet.append(int(linha[1].rstrip('\n')))

        for j in range(len(linhas)):
            for i in range(len(pointsVet) - 1):
                if pointsVet[i] < pointsVet[i + 1]:
                    pointsVet[i + 1], pointsVet[i] = pointsVet[i], pointsVet[i + 1]
                    namesVet[i + 1], namesVet[i] = namesVet[i], namesVet[i + 1]

        ranking.close()

        for i in range(len(namesVet)):
            if i > 4:
                break
            self.janela.draw_text("{}. {}: {} pontos.".format(i + 1, namesVet[i], pointsVet[i]), 480, 400 + i * 45,
                                  size=32, color=(255, 255, 255), font_name="Impact")

        if (self.teclado.key_pressed("ESC")):
            dados.GAME_STATE = 1