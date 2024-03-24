import pygame
import random


# TODO dodelat:)
class Minigame:
    def __init__(self, screen, vlk, sound):
        self.screen = screen
        self.vlk = vlk
        self.w, self.h = pygame.display.get_surface().get_size()
        self.background_image_hra = pygame.image.load('images/game_pozadi.png').convert()
        self.font = pygame.font.Font(None, 36)
        self.back_image = pygame.image.load('icons/left-arrow.png').convert_alpha()
        self.back_image_rect = self.back_image.get_rect(topleft=(0, 0))
        self.hlava = pygame.image.load('icons/hlava.png').convert_alpha()
        self.hlava_rect = self.hlava.get_rect(center=(40, self.h//2))
        self.sleep_image = pygame.image.load('icons/sleep.png').convert_alpha()
        self.sleep_image_rect = self.sleep_image.get_rect(topleft=(100, 0))
        self.happy_image = pygame.image.load('icons/game.png').convert_alpha()
        self.happy_image_rect = self.happy_image.get_rect(topleft=(300, 0))
        self.ball_image = pygame.image.load('images/ball.png').convert_alpha()
        self.ball_rect = (self.happy_image.get_rect
                          (center=(self.w, random.randint(40,self.h-(self.happy_image_rect.height//2)))))

    def play(self):
        clock = pygame.time.Clock()
        pokracovat = True

        while pokracovat:
            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            tired_percent = self.font.render(str(self.vlk.sleepy), True, "orange")
            happy_percent = self.font.render(str(self.vlk.happy), True, "orange")

            self.screen.blit(self.background_image_hra, (0, 0))
            self.screen.blit(self.back_image, self.back_image_rect)
            self.screen.blit(self.hlava, self.hlava_rect)
            self.screen.blit(self.sleep_image, self.sleep_image_rect)
            self.screen.blit(self.happy_image, self.happy_image_rect)
            self.screen.blit(self.ball_image, self.ball_rect)
            self.screen.blit(tired_percent, (140, 0))
            self.screen.blit(happy_percent, (340, 0))

            if self.back_image_rect.collidepoint(mouse):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            for event in pygame.event.get():
                if ((event.type == pygame.QUIT or
                        (event.type == pygame.MOUSEBUTTONDOWN and self.back_image_rect.collidepoint(mouse)))):
                    pokracovat = False

            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.hlava_rect.top >= 40:
                self.hlava_rect.y -= 5
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.hlava_rect.bottom <= self.h:
                self.hlava_rect.y += 5

            clock.tick(60)
            pygame.display.flip()

        if event.type == pygame.QUIT:
            return False
        else:
            return True