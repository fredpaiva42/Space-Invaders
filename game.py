import dados

class Jogar:

    def __init__(self, janela, fundo):
        self.janela = janela
        self.teclado = janela.get_keyboard()
        self.fundo = fundo

    def run(self):
        self.fundo.draw()

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0
