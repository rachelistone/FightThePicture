import pygame
import os
from  enum import Enum

WIDTH = 1000
HEIGHT = 700
BG = pygame.image.load(os.path.join('pictures', 'space.jpg'))

PICS = [
    pygame.image.load(os.path.join('pictures', 'jerusalem.jpg')),
    pygame.image.load(os.path.join('pictures', 'hevron.jpg')),
    pygame.image.load(os.path.join('pictures', 'beersheva.jpg')),
    pygame.image.load(os.path.join('pictures', 'bneibrak.jpg')),
    pygame.image.load(os.path.join('pictures', 'ramatgan.jpg')),
    pygame.image.load(os.path.join('pictures', 'onion.jpg')),
]

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    run = True

    class StateName(Enum):
        Wellcome = 1
        Game = 2

    stateName = StateName.Wellcome

    if stateName is StateName.Wellcome:
        Wellcome().wellcome_draw()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP and stateName is StateName.Wellcome:
                pic = state.select_pic()
                if pic != None:
                    game = Game(pic)
                    stateName = StateName.Game

        if stateName is StateName.Game:
            game.game_draw()


class Wellcome:

    def pixel_to_pic(self):
        def scale_pic(surface):
            return pygame.transform.scale(surface, (round(WIDTH / 5), round(HEIGHT / 5)))
        def pics_pos(x, y):
            return (round(WIDTH - x * WIDTH / 10), round(HEIGHT - y * HEIGHT / 10))
        pix_factor = [(9, 6), (6, 6), (3, 6), (9, 3), (6, 3), (3, 3)]
        return list(zip([pics_pos(x, y) for x,y in pix_factor], [scale_pic(i) for i in PICS]))

    def wellcome_draw(self):
        WINDOW.blit(pygame.transform.scale(BG, (WIDTH, HEIGHT)), (0, 0))

        font = pygame.font.SysFont('calibri', round(HEIGHT / 20))

        text0 = font.render('שלום!'[-1::-1], 1, (255, 255, 255))
        text1 = font.render('איזה תמונה תרצה לבנות?'[-1::-1], 1, (255, 255, 255))

        WINDOW.blit(text0, (WIDTH/2 - text0.get_width()/2, round(HEIGHT - 35*HEIGHT/40)))
        WINDOW.blit(text1, (WIDTH/2 - text1.get_width()/2, round(HEIGHT - 31*HEIGHT/40)))

        for k, v in self.pixel_to_pic():
            WINDOW.blit(v, (k[0], k[1]))
        pygame.display.update()

    def select_pic(self):
        x, y = pygame.mouse.get_pos()
        print(x, y)
        i = enumerate(PICS)
        for pixel, pic in self.pixel_to_pic():
            current = next(i)[0] # always returns 0 in the first selection
            if pic.get_rect(topleft=pixel).collidepoint(x, y): # pic doesnt have the scalesd size so the mouse wasnt inside
                selected_pic_i = current
                print(selected_pic_i)
                return pygame.transform.scale(PICS[selected_pic_i], (WIDTH, HEIGHT))
            return None

class Game:
    def __init__(self, picture):
        self.picture = picture

    def game_draw(picture):
        # if picture == -1:
        #     pygame.draw.rect(WINDOW, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
        # else:
        WINDOW.blit(self.picture, (0, 0))

main()