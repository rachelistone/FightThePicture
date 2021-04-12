import pygame
import os
import random

SCREENWIDTH = 1500
SCREENHEIGHT = 1000
NUMSQUARESWIDTH = 15
NUMSQUARESHEIGHT = 10
SQUAREWIDTH = round(SCREENWIDTH/NUMSQUARESWIDTH)
SQUAREHEIGHT = round(SCREENHEIGHT/NUMSQUARESHEIGHT)

pygame.init()
WINDOW = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

#--------------------- wellcome -----------------
PICS = [
    pygame.image.load(os.path.join('pictures', 'jerusalem.jpg')),
    pygame.image.load(os.path.join('pictures', 'hevron.jpg')),
    pygame.image.load(os.path.join('pictures', 'beersheva.jpg')),
    pygame.image.load(os.path.join('pictures', 'bneibrak.jpg')),
    pygame.image.load(os.path.join('pictures', 'ramatgan.jpg')),
    pygame.image.load(os.path.join('pictures', 'onion.jpg')),
]

PICS_POS = [
    (round(SCREENWIDTH - 9*SCREENWIDTH/10), round(SCREENHEIGHT - 6*SCREENHEIGHT/10)),
    (round(SCREENWIDTH - 6*SCREENWIDTH/10), round(SCREENHEIGHT - 6*SCREENHEIGHT/10)),
    (round(SCREENWIDTH - 3*SCREENWIDTH/10), round(SCREENHEIGHT - 6*SCREENHEIGHT/10)),
    (round(SCREENWIDTH - 9*SCREENWIDTH/10), round(SCREENHEIGHT - 3*SCREENHEIGHT/10)),
    (round(SCREENWIDTH - 6*SCREENWIDTH/10), round(SCREENHEIGHT - 3*SCREENHEIGHT/10)),
    (round(SCREENWIDTH - 3*SCREENWIDTH/10), round(SCREENHEIGHT - 3*SCREENHEIGHT/10))
]

def scale_pic(surface):
    return pygame.transform.scale(surface, (round(SCREENWIDTH / 5), round(SCREENHEIGHT / 5)))
PIXEL_TO_PIC = list(zip(PICS_POS, [scale_pic(i) for i in PICS]))

pygame.init()
WINDOW = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

def wellcome_draw():
    font = pygame.font.SysFont('calibri', round(SCREENHEIGHT / 20))

    text0 = font.render('שלום!'[-1::-1], 1, (255, 255, 255))
    text1 = font.render('איזה תמונה תרצה לבנות?'[-1::-1], 1, (255, 255, 255))

    WINDOW.blit(text0, (SCREENWIDTH/2 - text0.get_width()/2, round(SCREENHEIGHT - 35*SCREENHEIGHT/40)))
    WINDOW.blit(text1, (SCREENWIDTH/2 - text1.get_width()/2, round(SCREENHEIGHT - 31*SCREENHEIGHT/40)))

    for k, v in PIXEL_TO_PIC:
        WINDOW.blit(v, (k[0], k[1]))
    pygame.display.update()

#-------------------- game --------------------
class SquareDetails():
    # states = ['default', 'users', 'other']
    def __init__(self, row, col):
        self.state = 'default'
        self.row = row
        self.col = col

        
class Gragh:
    def __init__(self):
        self.matrix = [[None for col in range(0,NUMSQUARESWIDTH)] for row in range(0,NUMSQUARESHEIGHT)]
        for row in range(0,NUMSQUARESHEIGHT):
            for col in range(0,NUMSQUARESWIDTH):
                self.matrix[row][col] = SquareDetails(row, col)
                
    def set_square(self, row, col, state):
        self.matrix[row][col].state = state
      
    def get_square(self, row, col):
        return self.matrix[row][col]
        
    def printAll(self):
        for row in range(0,NUMSQUARESHEIGHT):
            for col in range(0,NUMSQUARESWIDTH):
                if self.matrix[row][col].state == 'default':
                    rect = pygame.Rect(col*SQUAREWIDTH, row*SQUAREHEIGHT, SQUAREWIDTH, SQUAREHEIGHT)
                    pygame.draw.rect(WINDOW, (0, 0, 0), rect)
                elif self.matrix[row][col].state == 'other':
                    rect = pygame.Rect(col*SQUAREWIDTH, row*SQUAREHEIGHT, SQUAREWIDTH, SQUAREHEIGHT)
                    pygame.draw.rect(WINDOW, (0, 200, 0), rect)

def printGrid():
    for x in range(0, SCREENWIDTH, SQUAREWIDTH):
        for y in range(0, SCREENHEIGHT, SQUAREHEIGHT):
            rect = pygame.Rect(x, y, SQUAREWIDTH, SQUAREHEIGHT)
            pygame.draw.rect(WINDOW, (100, 100, 100), rect, 1)
      
# --------------------- main process ----------------
def main():
    gragh = Gragh()
    run = True
    game = False

    while run and not game:

        wellcome_draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                i = enumerate(PICS)
                for pixel, pic in PIXEL_TO_PIC:
                    current = next(i)[1]
                    bg_pic = -1
                    if pic.get_rect(topleft=pixel).collidepoint(x, y):
                        bg_pic = current
                        game = True 
                        break
            if game:
                break
                  
    while run and game:
    
        pygame.display.update()
        WINDOW.blit(pygame.transform.scale(bg_pic, (SCREENWIDTH, SCREENHEIGHT)), (0, 0))
        gragh.printAll()
        printGrid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                for row in range(0,NUMSQUARESHEIGHT):
                    for col in range(0,NUMSQUARESWIDTH):
                        if col*SQUAREWIDTH < x < col*SQUAREWIDTH + SQUAREWIDTH and row*SQUAREHEIGHT < y < row*SQUAREHEIGHT + SQUAREHEIGHT:
                            gragh.set_square(row, col, 'users')
    

main()