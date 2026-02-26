import pygame
import os

WIN_WIDTH = 1000
WIN_HEIGHT = 700
C_RED = (90, 0, 0)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)

MENU_OPTION = ["START", "EXIT"]

class Menu:
    def __init__(self, display):
        self.display = display
        self.menu_option = 0
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, '..', 'asset', 'imagemenu.png')  #blackground menu
        music_path = os.path.join(base_dir, '..', 'asset', 'Menump3.wav')  #music menu
        self.surf = pygame.image.load(image_path).convert()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.music_path = music_path

    def menu_text(self, size, text, color, position):
        font = pygame.font.SysFont("consolas", size)  #font tittle
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position) #position tittle
        self.display.blit(text_surface, text_rect)

    def run(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)

        running = True
        while running: #event to close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

               #events to select options
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_DOWN:
                        self.menu_option = (self.menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        if MENU_OPTION[self.menu_option] == "START":
                            pygame.mixer.music.stop()
                            return "START"
                        elif MENU_OPTION[self.menu_option] == "EXIT":
                            pygame.quit()
                            exit()

            #positions and size of texts
            self.display.blit(self.surf, self.rect)
            self.menu_text(80, "Dragon", C_RED, (WIN_WIDTH / 2, 200))
            self.menu_text(80, "Attack", C_RED, (WIN_WIDTH / 2, 260))

            self.menu_text(30, "COMMANDS", C_BLACK, (WIN_HEIGHT / 6, 550))
            self.menu_text(24, "PRESS ENTER TO SELECT", C_BLACK, (WIN_HEIGHT / 1, 600))
            self.menu_text(24, "ARROWS TO SELECT OPTIONS", C_BLACK, (WIN_HEIGHT / 1, 630))
            self.menu_text(24, "SPACE - ATTACK", C_BLACK, (WIN_HEIGHT / 6, 580))
            self.menu_text(24, "WASD - MOVE", C_BLACK, (WIN_HEIGHT / 6, 600))

            for i in range(len(MENU_OPTION)):
                if i == self.menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_YELLOW, (WIN_WIDTH / 2, 400 + 25 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, (WIN_WIDTH / 2, 400 + 25 * i))

            pygame.display.flip()

        pygame.mixer.music.stop() #close the game, music stop
        return None