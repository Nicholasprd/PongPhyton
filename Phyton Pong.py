import os
import WConio2 as WConio2
import cursor
import math

cursor.hide()
os.system('cls')

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
paddle1_y = math.ceil(screen_y/2)

#paddle 2
paddle2_x = (screen_x-3)
paddle2_y = math.ceil(screen_y/2)

#ball
ball_x = math.ceil(screen_x/2)
ball_y = math.ceil(screen_y/2)
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

def resetball():
    ball_x = math.ceil(screen_x/2)
    ball_y = math.ceil(screen_y/2)
    return ball_x, ball_y

# List of menu options
options = [" ___ _ _ ___\n| . | | | . |\n|  _|\_/|  _|\n|_|     |_| ", " ___ _ _ _____ \n| . | | |     |\n|  _|\_/|_|_|_|\n|_|   ", "           _ _   \n __ _ _  _(_) |_ \n/ _` | || | |  _|\n\__, |\_,_|_|\__|\n   |_|  "]

# Initialize selected option
selected_option = 0

while True:
    # Clear screen
    WConio2.clrscr()
    # Print menu options
    for i in range(len(options)):
        WConio2.textcolor(WConio2.WHITE)
        if i == selected_option:
            WConio2.textcolor(WConio2.YELLOW)
        WConio2.cputs(options[i])
        WConio2.cputs("\n")

    # Get user input
    key = WConio2.getch()

    key = key[1];

    # Navigate through menu options
    if key == 'w' or key == 'W':
        if selected_option > 0:
            selected_option -= 1
    elif key == 's' or key == 'S':
        if selected_option < len(options) - 1:
            selected_option += 1
    elif key == '\r':
        # Perform action based on selected option
        
        #Playe vs Player        
        if selected_option == 0: 
            WConio2.clrscr()                   
            while not game_over:
                WConio2.gotoxy(0,screenPos_y)

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
                    ball_x, ball_y = resetball()

                elif ball_x >= (screen_x):
                    score1 += 1

                    game_speed = game_speed_start

                    #reset ball
                    ball_x, ball_y = resetball()

                # bounce the ball off the walls
                
                if ball_y <= (screenMin_y-1):
                    ball_direction_y = 1

                if ball_y >= (screen_y-1):
                    ball_direction_y = -1

                # check for game over
                if score1 >= 10 or score2 >= 10:
                    game_over = True

                # check for player input
                if WConio2.kbhit():
                    (key, symbol) = WConio2.getch()
                    
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
                os.system('cls')
                print("Player 1 wins!")
                break
            else:
                os.system('cls')
                print("Player 2 wins!")
                break

        #player vs AI
        elif selected_option == 1:
            WConio2.clrscr()
            while not game_over:
                WConio2.gotoxy(0,screenPos_y)

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
                    ball_x, ball_y = resetball()

                elif ball_x >= (screen_x):
                    score1 += 1

                    game_speed = game_speed_start

                    #reset ball
                    ball_x, ball_y = resetball()

                # bounce the ball off the walls
                
                if ball_y <= (screenMin_y-1):
                    ball_direction_y = 1

                if ball_y >= (screen_y-1):
                    ball_direction_y = -1

                # check for game over
                if score1 >= 10 or score2 >= 10:
                    game_over = True

                # check for player input
                if WConio2.kbhit():
                    (key, symbol) = WConio2.getch()
                    
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
                os.system('cls')
                print("Player 1 wins!")
                break
            else:
                os.system('cls')
                print("Player 2 wins!")
                break

        #Desligando o jogo
        elif selected_option == 2:
            WConio2.clrscr()
            print("O jogo foi encerrado")
            break
