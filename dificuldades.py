from PPlay.sprite import *
import dados


class Dificuldade:

    def __init__(self, janela, fundo):
        self.janela = janela
        self.fundo = fundo
        self.mouse = janela.get_mouse()
        self.teclado = janela.get_keyboard()

        # Botões de dificuldades
        self.button_facil = Sprite("./img/buttons/button_facil.png")
        self.button_medio = Sprite("./img/buttons/button_medio.png")
        self.button_dificil = Sprite("./img/buttons/button_dificil.png")

        # Posicionamento
        self.button_facil.set_position(self.janela.width / 2 - self.button_facil.width / 2,
                                       self.janela.height / 2.2 - self.button_facil.height / 2)

        self.button_medio.set_position(self.janela.width / 2 - self.button_medio.width / 2,
                                       self.janela.height / 1.85 - self.button_medio.height / 2)

        self.button_dificil.set_position(self.janela.width / 2 - self.button_dificil.width / 2,
                                         self.janela.height / 1.6 - self.button_dificil.height / 2)

    def run(self):
        self.fundo.draw()
        self.button_facil.draw()
        self.button_medio.draw()
        self.button_dificil.draw()

        if self.mouse.is_over_object(self.button_facil):
            if self.mouse.is_button_pressed(1):
                dados.MODO = 1
                print(dados.MODO)

        if self.mouse.is_over_object(self.button_medio):
            if self.mouse.is_button_pressed(1):
                dados.MODO = 2
                print(dados.MODO)

        if self.mouse.is_over_object(self.button_dificil):
            if self.mouse.is_button_pressed(1):
                dados.MODO = 3
                print(dados.MODO)

        if self.teclado.key_pressed('ESC'):
            dados.GAME_STATE = 0
