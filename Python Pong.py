from WConio2 import kbhit, cputs, getch, gotoxy, clrscr, textcolor, WHITE, YELLOW
from cursor import hide
from Funcoes_Auxiliares import *

hide()
clrscr()

#scoreboard
score1 = 0
score2 = 0
max_score = 10

#screenposition
screenPos_y = 20
screenPos_x = 80

#screensize
screenMin_y = 1
screenMin_x = 1
screen_y = 20
screen_x = 60

#paddle 1
paddle1_x = (screenMin_x+2)
paddle1_y = int(screen_y/2)

#paddle 2
paddle2_x = (screen_x-3)
paddle2_y = int(screen_y/2)

#ball
ball_x = int(screen_x/2)
ball_y = int(screen_y/2)
ball_direction_x = 1
ball_direction_y = 1

#game speed
game_speed_start = 60
game_speed = game_speed_start

#game over flag
game_over = False

contSpeed = 0
cont = 0
i = 0

# List of menu options
menuDesign = ["\n ==============================\n|  _____   ____  _   _  _____  |\n| |  __ \ / __ \| \ | |/ ____| |\n| | |__) | |  | |  \| | |  __  |\n| |  ___/| |  | | . ` | | |_ | |\n| | |    | |__| | |\  | |__| | |\n| |_|     \____/|_| \_|\_____| |\n ============================== \n"]
options = ["     \n _____        _____       \n|  __ \      |  __ \      \n| |__) |_   _| |__) |     \n|  ___/\ \ / /  ___/      \n| |     \ V /| |          \n|_|      \_/ |_|                         ", "     \n _____        __  __      \n|  __ \      |  \/  |     \n| |__) |_   _| \  / |     \n|  ___/\ \ / / |\/| |     \n| |     \ V /| |  | |     \n|_|      \_/ |_|  |_|","     \n _    _ _       _                                 \n| |  | (_)     | |                                \n| |__| |_  __ _| |__  ___  ___ ___  _ __ ___      \n|  __  | |/ _` | '_ \/ __|/ __/ _ \| '__/ _ \     \n| |  | | | (_| | | | \__ \ (_| (_) | | |  __/     \n|_|  |_|_|\__, |_| |_|___/\___\___/|_|  \___|     \n           __/ |                                  \n          |___/                              ","     \n  ____        _ _        \n / __ \      (_) |       \n| |  | |_   _ _| |_      \n| |  | | | | | | __|     \n| |__| | |_| | | |_      \n \___\_\\__,_|_|\__|"]

# Initialize selected option
selected_option = 0
exit_game = False

while not exit_game:
    # Clear screen
    clrscr()

    # Print menu desgin
    gotoxy(5,5)
    for i in range(len(menuDesign)):
        textcolor(WHITE)
        cputs(" " * 50 + menuDesign[i])
    
    # Print menu options
    for i in range(len(options)):
        textcolor(WHITE)
        if i == selected_option:
            textcolor(YELLOW)
        cputs(options[i] + '\n')

    # Get user input
    key = getch()[1]

    # Navigate through menu options
    if (key in ['w', 'W']) and (selected_option > 0) :
        selected_option -= 1

    elif (key in ['s', 'S']) and (selected_option < (len(options) - 1)):
        selected_option += 1
        
    elif key == '\r':
        # Perform action based on selected option
        
        #Playe vs Player        
        if selected_option == 0: 
            clrscr()                   
            while not game_over:
                gotoxy(0,screenPos_y)

                # draw the score
                print(' '*screenPos_x,"Player 1: " + str(score1) + "  Player 2: " + str(score2) + " GameSpeed: " + str(game_speed))

                print(' '*screenPos_x,'▓'*(screen_x+2))
                for j in range(screen_y):
                    print(' '*screenPos_x, '▓', end='')
                    for k in range(screen_x):
                        char = ' '
                        
                        if j==ball_y and k==ball_x:
                            char="●"
                        
                        if j==paddle1_y and k==paddle1_x:
                            char = "║"
                        if j==paddle1_y-1 and k==paddle1_x:
                            char = "╥"
                        if j==paddle1_y+1 and k==paddle1_x:
                            char = "╨"

                        if j==paddle2_y and k==paddle2_x:
                            char = "║"
                        if j==paddle2_y-1 and k==paddle2_x:
                            char = "╥"
                        if j==paddle2_y+1 and k==paddle2_x:
                            char = "╨"

                        print(char, end='')

                    print('▓')
                print(' '*screenPos_x,'▓'*(screen_x+2))

                # move the ball

                if cont == game_speed:
                    ball_x += ball_direction_x
                    ball_y += ball_direction_y
                    cont = 0
                    contSpeed += 1

                if contSpeed==(screen_x):
                    game_speed -= 1
                    contSpeed = 0

                #bounce ball on the paddle

                if ball_x == (paddle1_x +1) and ball_y in range((paddle1_y-1), (paddle1_y+2)):
                    ball_direction_x = 1

                if ball_x == (paddle2_x-1) and ball_y in range((paddle2_y-1), (paddle2_y+2)):
                    ball_direction_x = -1

                # Check Point
                if ball_x <= (screenMin_x-1):
                    score2 += 1
                    game_speed = game_speed_start

                    #reset ball
                    ball_x, ball_y = resetball(screen_x, screen_y)

                elif ball_x >= (screen_x):
                    score1 += 1

                    game_speed = game_speed_start

                    #reset ball
                    ball_x, ball_y = resetball(screen_x, screen_y)

                # bounce the ball off the walls
                
                if ball_y <= (screenMin_y-1):
                    ball_direction_y = 1

                if ball_y >= (screen_y-1):
                    ball_direction_y = -1

                # check for game over
                if score1 >= 10 or score2 >= 10:
                    game_over = True

                # check for player input
                if kbhit():
                    (key, symbol) = getch()
                    
                    if symbol == "w":
                        paddle1_y -= 1
                    elif symbol == "s":
                        paddle1_y += 1
                    elif symbol == "o":
                        paddle2_y -= 1
                    elif symbol == "l":
                        paddle2_y += 1

                # cap paddles to screen
                if paddle1_y < (screenMin_y):
                    paddle1_y = (screenMin_y)
                elif paddle1_y > (screen_y-2):
                    paddle1_y = (screen_y-2)
                if paddle2_y < (screenMin_y):
                    paddle2_y = (screenMin_y)
                elif paddle2_y > (screen_y-2):
                    paddle2_y = (screen_y-2)

                cont+=1

            if score1 >= max_score:
                clrscr()
                print("Player 1 wins!")
                break
            else:
                clrscr()
                print("Player 2 wins!")
                break

        #player vs AI
        elif selected_option == 1:
            clrscr()
            while not game_over:
                gotoxy(0,screenPos_y)

                # draw the score
                print(' '*screenPos_x,"Player 1: " + str(score1) + "  Player 2: " + str(score2) + " GameSpeed: " + str(game_speed))

                print(' '*screenPos_x,'▓'*(screen_x+2))
                for j in range(screen_y):
                    print(' '*screenPos_x, '▓', end='')
                    for k in range(screen_x):
                        char = ' '
                        
                        if j==ball_y and k==ball_x:
                            char="●"
                        
                        if j==paddle1_y and k==paddle1_x:
                            char = "║"
                        if j==paddle1_y-1 and k==paddle1_x:
                            char = "╥"
                        if j==paddle1_y+1 and k==paddle1_x:
                            char = "╨"

                        if j==paddle2_y and k==paddle2_x:
                            char = "║"
                        if j==paddle2_y-1 and k==paddle2_x:
                            char = "╥"
                        if j==paddle2_y+1 and k==paddle2_x:
                            char = "╨"

                        print(char, end='')

                    print('▓')
                print(' '*screenPos_x,'▓'*(screen_x+2))

                # move the ball

                if cont == game_speed:
                    ball_x += ball_direction_x
                    ball_y += ball_direction_y
                    cont = 0
                    contSpeed += 1

                if contSpeed==(screen_x):
                    game_speed -= 1
                    contSpeed = 0

                #bounce ball on the paddle

                if ball_x == (paddle1_x +1) and ball_y in range((paddle1_y-1), (paddle1_y+2)):
                    ball_direction_x = 1

                if ball_x == (paddle2_x-1) and ball_y in range((paddle2_y-1), (paddle2_y+2)):
                    ball_direction_x = -1

                # Artificial Intelligence for paddle 2
                if ball_direction_x == 1:
                    if paddle2_y < ball_y:
                        paddle2_y += 1
                    elif paddle2_y > ball_y:
                        paddle2_y -= 1

                # Check Point
                if ball_x <= (screenMin_x-1):
                    score2 += 1
                    game_speed = game_speed_start

                    #reset ball
                    ball_x, ball_y = resetball(screen_x, screen_y)

                elif ball_x >= (screen_x):
                    score1 += 1

                    game_speed = game_speed_start

                    #reset ball
                    ball_x, ball_y = resetball(screen_x, screen_y)

                # bounce the ball off the walls
                
                if ball_y <= (screenMin_y-1):
                    ball_direction_y = 1

                if ball_y >= (screen_y-1):
                    ball_direction_y = -1

                # check for game over
                if score1 >= 10 or score2 >= 10:
                    game_over = True

                # check for player input
                if kbhit():
                    (key, symbol) = getch()
                    
                    if symbol == "w":
                        paddle1_y -= 1
                    elif symbol == "s":
                        paddle1_y += 1

                # cap paddles to screen
                if paddle1_y < (screenMin_y):
                    paddle1_y = (screenMin_y)
                elif paddle1_y > (screen_y-2):
                    paddle1_y = (screen_y-2)
                if paddle2_y < (screenMin_y):
                    paddle2_y = (screenMin_y)
                elif paddle2_y > (screen_y-2):
                    paddle2_y = (screen_y-2)

                cont+=1

            if score1 >= max_score:
                clrscr()
                print("Player 1 wins!")
                break
            else:
                clrscr()
                print("Player 2 wins!")
                break

        #Desligando o jogo
        elif selected_option == 3:
            clrscr()
            print("O jogo foi encerrado")
            break
