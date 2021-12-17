from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import dados


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
