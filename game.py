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
        self.contador = 0
        self.relogio = 0

    def run(self):
        # FPS
        self.relogio = self.relogio + self.janela.delta_time()
        self.contador += 1

        if self.relogio >= 1:
            self.fps = self.contador
            self.relogio = 0
            self.contador = 1

        self.fundo.draw()
        self.jogador.run()
        self.monstros.run()
        self.tempo += self.janela.delta_time()

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0
