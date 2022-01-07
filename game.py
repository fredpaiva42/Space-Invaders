import dados
from jogador import Jogador
from monstros import Monstros


class Jogar:

    def __init__(self, janela, fundo):
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.fundo = fundo
        self.jogador = Jogador(self.janela)
        self.monstros = Monstros(self.janela)

        self.tempo = 0
        self.fps = 0
        self.acrescimo = 0
        self.pontos = 0
        self.contador = 0
        self.relogio = 0
        self.vitoria = False

    def hitBox(self):

        self.vetBox = []
        if (len(self.monstros.matrizMonstros)) > 0:
            self.MenorY = int(self.monstros.matrizMonstros[0][0].y)
            self.vetBox.append(self.MenorY)

            self.MaiorY = int(self.monstros.matrizMonstros[-1][0].y + self.monstros.matrizMonstros[-1][0].width)
            self.vetBox.append(self.MaiorY)

        self.MenorX = self.janela.width
        self.MaiorX = 0

        for i in range(len(self.monstros.matrizMonstros)):
            if int(self.monstros.matrizMonstros[i][0].x) < self.MenorX:
                self.MenorX = int(self.monstros.matrizMonstros[i][0].x)

            if int(self.monstros.matrizMonstros[i][-1].x) > self.MaiorX:
                self.MaiorX = int(self.monstros.matrizMonstros[i][-1].x + self.monstros.matrizMonstros[i][-1].height)

        self.vetBox.append(self.MenorX)
        self.vetBox.append(self.MaiorX)

        return self.vetBox

    def colisaotiro(self):
        self.maiorY_Tiro = self.atirado.y + self.atirado.height
        self.menorX_Tiro = self.atirado.x
        self.maiorX_Tiro = self.atirado.x + self.atirado.width

        self.menorY_Nave = self.jogador.jogador.y
        self.menorX_Nave = self.jogador.jogador.x
        self.maiorX_Nave = self.jogador.jogador.x + self.jogador.jogador.width

        if (self.maiorY_Tiro >= self.menorY_Nave):
            if ((self.maiorX_Tiro >= self.menorX_Nave and self.menorX_Tiro <= self.menorX_Nave) or (
                    self.menorX_Tiro >= self.menorX_Nave and self.menorX_Tiro <= self.maiorX_Nave) or (
                    self.maiorX_Tiro >= self.maiorX_Nave and self.menorX_Tiro <= self.maiorX_Nave)):
                return True
        return False

    def acertouMonstros(self):
        self.vetBox = self.hitBox()

        for self.atirado in (self.jogador.vetTiros):
            if (int(self.atirado.y) >= self.vetBox[0]) and (int(self.atirado.y) <= self.vetBox[1]) and (
                    int(self.atirado.x) >= self.vetBox[2]) and (int(self.atirado.x) <= self.vetBox[3]):
                for self.fileira in (self.monstros.matrizMonstros):
                    for self.monstro in self.fileira:
                        for self.tiro in (self.jogador.vetTiros):
                            if (self.monstro.collided(self.tiro)):
                                self.monstros.maxMonstros -= 1

                                if self.monstros.vel_monstros < 0:
                                    self.monstros.vel_monstros -= 12
                                else:
                                    self.monstros.vel_monstros += 12

                                self.pontos += int(10 + 50 / self.tempo)
                                self.fileira.remove(self.monstro)
                                self.jogador.vetTiros.remove(self.tiro)

                                if (len(self.fileira)) == 0:
                                    self.monstros.matrizMonstros.remove(self.fileira)
                                    break

    def level(self):
        self.pontos += 100 * (5 ** (dados.MODO - 1))
        self.acrescimo += 2

        self.monstros.colunas += 1
        self.monstros.linhas += 1

        if self.monstros.colunas > self.janela.width / 60 - 1:
            self.monstros.colunas = int(self.janela.width / 60 - 1)

        if self.monstros.linhas > self.janela.height / 60 - 2:
            self.monstros.linhas = int(self.janela.height / 60 - 2)

        self.monstros.vel_monstros = (75 + (50 * dados.MODO)) + self.acrescimo

        if self.monstros.limite > 0.2:
            self.monstros.limite -= 0.1

        self.monstros.maxMonstros = self.monstros.colunas * self.monstros.linhas
        self.jogador.vetTiros.clear()
        self.tempo = 0
        self.monstros.spawnarMonstros()

    def run(self):
        # FPS
        self.relogio = self.relogio + self.janela.delta_time()
        self.contador += 1

        if self.relogio >= 1:
            self.fps = self.contador
            self.relogio = 0
            self.contador = 1

        if self.monstros.maxMonstros == 0:
            self.level()

        self.fundo.draw()
        self.jogador.run()
        self.monstros.run()
        self.tempo += self.janela.delta_time()

        self.acertouMonstros()

        self.janela.draw_text("FPS: " + str(self.fps), 15, 10, size=30, color=(255, 255, 255), font_name='Impact',
                              bold=False, italic=False)
        self.janela.draw_text(str("PONTOS: ") + str(self.pontos), dados.janela.width - 150, 10, size=25, color=(255, 255, 255),
                              font_name='Impact', bold=False, italic=False)

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0
