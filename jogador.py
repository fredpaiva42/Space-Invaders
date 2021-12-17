from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import dados


class Jogador:
    def __init__(self, janela):
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.jogador = Sprite("./img/player/nave1.png")
        self.jogador.set_position(self.janela.width / 2 - self.jogador.width / 2,
                                  (self.janela.height - self.jogador.height) - 30)
        self.vetTiros = []
        self.cdTiro = 0

        self.contagem = 0

        if dados.MODO == 1:
            self.limitetiros = 20
        if dados.MODO == 2:
            self.limitetiros = 15
        if dados.MODO == 3:
            self.limitetiros = 10

    def atirar(self):
        self.tiro = Sprite("./img/player/tiro.png")
        self.tiro.set_position(self.jogador.x + self.jogador.width / 2 - self.tiro.width / 2, self.jogador.y)
        self.vetTiros.append(self.tiro)

    def tirosAtt(self):
        # Tiro:
        for i in range(len(self.vetTiros)):
            self.vetTiros[i].move_y(self.janela.delta_time() * -300)

            # Removendo o tiro:
            if self.vetTiros[i].y <= 0:
                self.vetTiros.pop(i)
                break

    def run(self):
        if dados.MODO == 1:
            self.vel_jogador = 300
            self.limite = 0.3
        if dados.MODO == 2:
            self.vel_jogador = 200
            self.limite = 0.65
        if dados.MODO == 3:
            self.vel_jogador = 100
            self.limite = 0.7

        # Movimentação do Jogador:
        if self.teclado.key_pressed("LEFT"):
            self.jogador.move_x((self.vel_jogador * -1) * self.janela.delta_time())

        if self.teclado.key_pressed("RIGHT"):
            self.jogador.move_x(self.vel_jogador * self.janela.delta_time())

        # Colisão do Jogador:
        if self.jogador.x < 0:
            self.jogador.x = self.janela.width - self.jogador.width

        if self.jogador.x + self.jogador.width > self.janela.width:
            self.jogador.set_position(0, self.janela.height - self.jogador.height * 1.2)

        # Atirar:
        if self.cdTiro >= self.limite:
            if self.teclado.key_pressed("SPACE"):
                self.contagem += 1
                self.atirar()
                self.cdTiro = 0

        self.cdTiro += self.janela.delta_time()
        self.tirosAtt()

        if self.contagem == self.limitetiros:
            self.contagem = 0

        # Draw:
        self.jogador.draw()

        for i in range(len(self.vetTiros)):
            self.vetTiros[i].draw()
