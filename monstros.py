from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import dados
import random

class Monstros:
    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.vel_monstros = 75 + (50 * dados.MODO)
        self.cdDescer = 0

        self.matrizMonstros = []
        self.linhas = 3 + dados.MODO
        self.colunas = 3 + dados.MODO
        self.maxMonstros = self.linhas * self.colunas
        self.spawnarMonstros()

        self.vetTiros = []
        self.cdTiro = 0
        self.limite = 2 / dados.MODO

    def spawnarMonstros(self):
        for i in range(self.linhas):
            self.matrizMonstros.append([])
            for j in range(self.colunas):
                self.matrizMonstros[i].append(Sprite('./img/monstros/invader.png'))
                self.matrizMonstros[i][j].set_position((j + 1) * (self.janela.width / (self.janela.width / 85)),
                                                       (i * 50) + 50)

    def colidiu(self):
        for i in range(len(self.matrizMonstros)):
            if (self.matrizMonstros[i][-1].x + self.matrizMonstros[i][-1].width >= self.janela.width) or (
                    self.matrizMonstros[i][0].x <= 0):
                return True
        return False

    def atirar(self):
        if self.cdTiro > (self.limite):
            self.atirador = random.randint(0, self.maxMonstros)
            self.contagem = 0

            for i in range(len(self.matrizMonstros)):
                for j in range(len(self.matrizMonstros[i])):
                    self.contagem += 1
                    if self.contagem == self.atirador:
                        self.tiro = Sprite("img/monstros/tiroMonstros.png")
                        self.tiro.set_position(
                            self.matrizMonstros[i][j].x + self.matrizMonstros[i][j].width / 2 - self.tiro.width / 2,
                            self.matrizMonstros[i][j].y)
                        self.vetTiros.append(self.tiro)
                        self.cdTiro = 0
                        return
        else:
            self.cdTiro += self.janela.delta_time()

    def tirosAtt(self):
        for i in range(len(self.vetTiros)):
            self.vetTiros[i].move_y(self.janela.delta_time() * 200)
            if self.vetTiros[i].y >= self.janela.height:
                self.vetTiros.pop(i)
                break

    def run(self):
        # Movimentação dos Monstros:
        for i in range(len(self.matrizMonstros)):
            for j in range(len(self.matrizMonstros[i])):
                self.matrizMonstros[i][j].move_x(self.vel_monstros * self.janela.delta_time())

        # Colisão dos Monstros e Descida:
        if self.cdDescer > 0.15:
            if self.colidiu():
                self.vel_monstros = self.vel_monstros * (-1)

                for i in range(len(self.matrizMonstros)):
                    for j in range(len(self.matrizMonstros[i])):
                        self.matrizMonstros[i][j].y += 20
                self.cdDescer = 0

        else:
            self.cdDescer += self.janela.delta_time()

        # Draw:
        for i in range(len(self.matrizMonstros)):
            for j in range(len(self.matrizMonstros[i])):
                self.matrizMonstros[i][j].draw()

        for i in range(len(self.vetTiros)):
            self.vetTiros[i].draw()

        self.atirar()
        self.tirosAtt()