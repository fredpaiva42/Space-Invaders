from PPlay.gameimage import *
from PPlay.sprite import *
import dados


class Menu:
    def __init__(self, janela, fundo):
        self.janela = janela
        self.mouse = janela.get_mouse()
        self.fundo = fundo
        self.titulo = GameImage("./img/background/Title.png")

        # Botões
        self.button_jogar = Sprite("./img/buttons/button_jogar.png")
        self.button_ranking = Sprite("./img/buttons/button_raking.png")
        self.button_dificuldade = Sprite("./img/buttons/button_dificuldade.png")
        self.button_sair = Sprite("./img/buttons/button_sair.png")

        # Posicionamento
        self.titulo.set_position(self.janela.width / 2 - self.titulo.width / 1.7,
                                 self.janela.height / 3.5 - self.titulo.height / 2)

        self.button_jogar.set_position(self.janela.width / 2 - self.button_jogar.width / 2,
                                       self.janela.height / 2.2 - self.button_jogar.height / 2)

        self.button_ranking.set_position(self.janela.width / 2 - self.button_ranking.width / 2,
                                         self.janela.height / 1.85 - self.button_ranking.height / 2)

        self.button_dificuldade.set_position(self.janela.width / 2 - self.button_dificuldade.width / 2,
                                             self.janela.height / 1.6 - self.button_dificuldade.height / 2)

        self.button_sair.set_position(self.janela.width / 2 - self.button_sair.width / 2,
                                      self.janela.height / 1.4 - self.button_sair.height / 2)

    def run(self):
        # Seleção
        self.fundo.draw()
        self.titulo.draw()
        self.button_jogar.draw()
        self.button_ranking.draw()
        self.button_dificuldade.draw()
        self.button_sair.draw()

        if self.mouse.is_over_object(self.button_jogar):
            if self.mouse.is_button_pressed(1):
                dados.GAME_STATE = 1

        if self.mouse.is_over_object(self.button_ranking):
            if self.mouse.is_button_pressed(1):
                dados.GAME_STATE = 5

        if self.mouse.is_over_object(self.button_dificuldade):
            if self.mouse.is_button_pressed(1):
                dados.GAME_STATE = 3

        if self.mouse.is_over_object(self.button_sair):
            if self.mouse.is_button_pressed(1):
                dados.GAME_STATE = 4
