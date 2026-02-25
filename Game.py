
from Menu import Menu

import pygame


class Game:

    window = None

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # window size

    def run(self):
        pass


def run(self):

 while True:
    menu = Menu(self.window)
    menu.run()
    pass

 #for event in pygame.event.get():
  #if event.type == pygame.QUIT:
   #pygame.quit()  # close window
    #quit()  # finish pygame
