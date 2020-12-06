import pygame
import os

SCREENWIDTH = 1500
SCREENHEIGHT = 1000
NUMSQUARESWIDTH = 75
NUMSQUARESHEIGHT = 50
SQUAREWIDTH = round(SCREENWIDTH/NUMSQUARESWIDTH)
SQUAREHEIGHT = round(SCREENHEIGHT/NUMSQUARESHEIGHT)

pygame.init()
WINDOW = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

def slice_pic(Picture):
    pass

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                for row in range(0, SCREENHEIGHT, SQUAREHEIGHT):
                    for col in range(0, SCREENWIDTH, SQUAREWIDTH):
                        if col < x < col + SQUAREWIDTH and row < y < row + SQUAREHEIGHT:
                            pygame.draw.rect(WINDOW, (255, 0, 0), (col, row, SQUAREWIDTH, SQUAREHEIGHT))
        pygame.display.update()

main()