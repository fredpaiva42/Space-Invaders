from game import Jogar
from menu import Menu
from dificuldades import Dificuldade
import dados


menu = Menu(dados.janela, dados.fundo)
jogo = Jogar(dados.janela, dados.fundo)
dificuldade = Dificuldade(dados.janela, dados.fundo)

while dados.GAME_STATE != 5:

    if dados.GAME_STATE == 0:
        menu.run()
    elif dados.GAME_STATE == 1:
        jogo.run()
    elif dados.GAME_STATE == 3:
        dificuldade.run()
    elif dados.GAME_STATE == 4:
        dados.janela.close()

    dados.janela.update()
