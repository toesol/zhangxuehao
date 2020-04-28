import pygame, sys   
from pygame.locals import *
from math import pi

pygame.init()   
screen = pygame.display.set_mode((700, 700))   
pygame.display.set_caption('Tic tac toe')  

 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

 
box1 = [50, 50, 195, 195]
box2 = [50, 250, 195, 195]
box3 = [50, 450, 195, 195]
box4 = [250, 50, 195, 195]
box5 = [250, 250, 195, 195]
box6 = [250, 450, 195, 195]
box7 = [450, 50, 195, 195]
box8 = [450, 250, 195, 195]
box9 = [450, 450, 195, 195]
 
boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

 
screen.fill(BLACK)
 
for i in range(0, 9):
    pygame.draw.rect(screen, WHITE, boxes[i], 3)
 
status = 1
 
number = 0
 
nine = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


 
def isWin(q):
     
    if nine[0][0] == q and nine[0][1] == q and nine[0][2] == q:
        drawWin(q)
    elif nine[1][0] == q and nine[1][1] == q and nine[1][2] == q:
        drawWin(q)
    elif nine[2][0] == q and nine[2][1] == q and nine[2][2] == q:
        drawWin(q)
    elif nine[0][0] == q and nine[1][0] == q and nine[2][0] == q:
        drawWin(q)
    elif nine[0][1] == q and nine[1][1] == q and nine[2][1] == q:
        drawWin(q)
    elif nine[0][2] == q and nine[1][2] == q and nine[2][2] == q:
        drawWin(q)
    elif nine[0][0] == q and nine[1][1] == q and nine[2][2] == q:
        drawWin(q)
    elif nine[2][0] == q and nine[1][1] == q and nine[0][2] == q:
        drawWin(q)
    # 平局
    elif number == 9:
        drawDraw()
    else:
        return False


 
def drawWin(q):
    if q == 1:
        font = pygame.font.Font('BankgothicMB.ttf', 45)
        text = font.render('Circle WIN!!!', True, RED)
        screen.blit(text, (210, 300))
    elif q == 2:
        font = pygame.font.Font('BankgothicMB.ttf', 45)
        text = font.render('X WIN!!!', True, RED)
        screen.blit(text, (260, 300))


 
def drawDraw():
    font = pygame.font.Font('BankgothicMB.ttf', 40)
    text = font.render('THE GAME HAS DRAWN!', True, RED)
    screen.blit(text, (85, 300))


while True:   
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            x = (pos[0] - 50) // 200
            y = (pos[1] - 50) // 200

            
            if nine[x][y] == 0 and status == 1:
                
                pygame.draw.arc(screen, GREEN, [x * 200 + 75, y * 200 + 75, 150, 150], 0, 2 * pi, 5)
                nine[x][y] = 1
                number += 1
               
                if number > 4:
                    isWin(1)
                status = 0
            
            elif nine[x][y] == 0 and status == 0:
                 
                pygame.draw.line(screen, BLUE, [x * 200 + 75, y * 200 + 75], [x * 200 + 225, y * 200 + 225], 6)
                pygame.draw.line(screen, BLUE, [x * 200 + 225, y * 200 + 75], [x * 200 + 75, y * 200 + 225], 6)
                nine[x][y] = 2
                number += 1
                if number > 4:
                    isWin(2)
                status = 1
            else:
                pass

    pygame.display.update()  
