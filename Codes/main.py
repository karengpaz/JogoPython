import pygame
from Menu import Menu
from Game import Game

WIN_WIDTH = 1000
WIN_HEIGHT = 700

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Dragon Attack")

    while True:
        menu = Menu(screen)
        result = menu.run()

        if result == "START":
            game = Game(screen)
            game.run()
            #esc or game over, returns to the menu

if __name__ == "__main__":
    main()