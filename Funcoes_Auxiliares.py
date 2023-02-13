#Criado com o intuito de não poluir o código.

"""
Aqui ficam as funções que auxiliam no funcionamento o game.

"""

def resetball(screen_x, screen_y):
    ball_x = int(screen_x/2)
    ball_y = int(screen_y/2)
    return ball_x, ball_y