from game import Jogar
from menu import Menu
from dificuldades import Dificuldade
from ranking import Ranking
import dados


menu = Menu(dados.janela, dados.fundo)
dificuldade = Dificuldade(dados.janela, dados.fundo)
Ranking = Ranking(dados.janela)
fechado = False

while dados.GAME_STATE != 4:

    if fechado and dados.GAME_STATE != 1:
        fechado = False
    elif not fechado and dados.GAME_STATE == 1:
        fechado = True
        jogo = Jogar(dados.janela, dados.fundo)

    if dados.GAME_STATE == 0:
        menu.run()
    elif dados.GAME_STATE == 1:
        jogo.run()
    elif dados.GAME_STATE == 3:
        dificuldade.run()
    elif dados.GAME_STATE == 4:
        dados.janela.close()
    elif dados.GAME_STATE == 5:
        Ranking.run()

    dados.janela.update()

