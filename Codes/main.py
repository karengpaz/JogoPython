import pygame

from Game import Game
from Menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Dragon Attack")

    menu = Menu(screen)
    menu.run()

    game = Game(screen)
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()