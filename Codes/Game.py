import pygame
import os
from Config import WIN_WIDTH, WIN_HEIGHT, FPS, C_WHITE, C_BLACK
from Player import Player  #importing classes
from DragonFire import DragonFire
from Demon import Demon

class Game:
    def __init__(self, display):
        self.display = display
        self.clock = pygame.time.Clock()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        bg_path = os.path.join(base_dir, '..', 'asset', 'Battleground1.png') #add blackground
        music_path = os.path.join(base_dir, '..', 'asset', 'Fase1mp3.wav') #add music

        self.background = pygame.image.load(bg_path).convert()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))
        self.music_path = music_path

        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.fires = pygame.sprite.Group()
        self.demons = pygame.sprite.Group()

        self.all_sprites.add(self.player)

        self.spawn_timer = 0
        self.fire_cooldown = 0

    def spawn_demon(self):
        demon = Demon()
        self.demons.add(demon)
        self.all_sprites.add(demon)

    def game_text(self, size, text, color, position):
        font = pygame.font.SysFont("consolas", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)
        self.display.blit(text_surface, text_rect)

    def run(self):
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)

        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        return
                    if event.key == pygame.K_SPACE and self.fire_cooldown <= 0:
                        fire = DragonFire(
                            self.player.rect.right,
                            self.player.rect.centery
                        )
                        self.fires.add(fire)
                        self.all_sprites.add(fire)
                        self.fire_cooldown = 15

            # cooldown
            if self.fire_cooldown > 0:
                self.fire_cooldown -= 1

            # spawn demons
            self.spawn_timer += 1
            if self.spawn_timer >= 60:
                self.spawn_demon()
                self.spawn_timer = 0

            # atualizar sprites
            self.all_sprites.update()

            #fire x demon
            pygame.sprite.groupcollide(self.fires, self.demons, True, True)

            #takes damage
            demon_hits = pygame.sprite.spritecollide(self.player, self.demons, True)
            for hit in demon_hits:
                self.player.health -= 20

            # game over
            if self.player.health <= 0:
                self.game_over()
                pygame.mixer.music.stop()
                return


            self.display.blit(self.background, (0, 0))
            self.all_sprites.draw(self.display)
            self.player.draw_health_bar(self.display)

            #instruction
            self.game_text(16, "ESC - MENU | SPACE - FIRE | WASD - MOVE", C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT - 20))

            pygame.display.flip()

    def game_over(self):
        self.display.fill(C_BLACK)
        self.game_text(60, "GAME OVER", (200, 0, 0), (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 40))
        self.game_text(20, "Press ENTER to return to menu", C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 30))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False