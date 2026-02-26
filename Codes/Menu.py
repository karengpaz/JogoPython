import pygame
import os

WIN_WIDTH = 1000
WIN_HEIGHT = 700
C_RED = (90, 0, 0)

class Menu:
    def __init__(self, display):
        self.display = display
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, '..', 'asset', 'imagemenu.png')
        music_path = os.path.join(base_dir, '..', 'asset', 'Menump3.wav')
        self.surf = pygame.image.load(image_path).convert()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.music_path = music_path

    def menu_text(self, size, text, color, position):
        font = pygame.font.SysFont("consolas", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self.display.blit(text_surface, text_rect)

    def run(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display.blit(self.surf, self.rect)
            self.menu_text(80, "Dragon", C_RED, (WIN_WIDTH / 2, 100))
            self.menu_text(80, "Attack", C_RED, (WIN_WIDTH / 2, 160))
            pygame.display.update()

        pygame.mixer.music.stop()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Dragon Attack")
    menu = Menu(screen)
    menu.run()
    pygame.quit()