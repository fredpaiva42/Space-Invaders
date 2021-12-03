from PPlay.gameimage import GameImage
from PPlay.window import *

# inicialização
janela = Window(1252, 840)
janela.set_title('Space Invaders')

fundo = GameImage("./img/background/space.png")
titulo = GameImage("./img/background/Title.png")

GAME_STATE = 0
MODO = 1
