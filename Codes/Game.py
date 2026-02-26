import pygame


class Game:
    def __init__(self, display):
        self.display = display
        self.gameLoop = True

    def run(self):
        clock = pygame.time.Clock()

        while self.gameLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameLoop = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                print('Pressed W')
            if keys[pygame.K_s]:
                print('Pressed S')
            if keys[pygame.K_d]:
                print('Pressed D')
            if keys[pygame.K_a]:
                print('Pressed A')

            self.display.fill((0, 0, 0))
            pygame.display.update()
            clock.tick(60)