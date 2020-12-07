import pygame
import os
import csv
import random

SCREENWIDTH = 1500
SCREENHEIGHT = 1000
NUMSQUARESWIDTH = 75
NUMSQUARESHEIGHT = 50
SQUAREWIDTH = round(SCREENWIDTH/NUMSQUARESWIDTH)
SQUAREHEIGHT = round(SCREENHEIGHT/NUMSQUARESHEIGHT)

pygame.init()
WINDOW = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

class Squares:
    def __init__(self):
        with open('squares.csv', 'w', newline='') as table:
            col_keys = [' ']+[str(i) for i in range(0, NUMSQUARESWIDTH)]
            self.writer = csv.DictWriter(table, col_keys)
            self.writer.writeheader()
            for i in range(0, NUMSQUARESHEIGHT):
                writer.writerow(dict(zip(col_keys, [str(i)]+[0]*NUMSQUARESWIDTH)))

    def set_square(self, col, row):
        pass # self.writer.fieldnames[col+1][row] = True


def slice_pic():
    p = pygame.image.load(os.path.join('pictures', 'jerusalem.jpg'))
    # get_square()
    WINDOW.blit(pygame.transform.scale(p, (SCREENWIDTH, SCREENHEIGHT)), (0, 0))

def main():
    # print_grid()
    squares = Squares()
    run = True
    while run:
        # slice_pic()
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
                            squares.set_square(col, row)
                pygame.display.update()

main()