import pygame
import random


class MinigameFood:
    def __init__(self, screen, vlk, sound):
        self.screen = screen
        self.vlk = vlk
        self.w, self.h = pygame.display.get_surface().get_size()
        self.background_image_hra = pygame.image.load('images/game/pozadi.png').convert()
        self.back_image = pygame.image.load('icons/left-arrow.png').convert_alpha()
        self.back_image_rect = self.back_image.get_rect(topleft=(0, 0))
        self.sleep_image = pygame.image.load('icons/sleep.png').convert_alpha()
        self.sleep_image_rect = self.sleep_image.get_rect(topleft=(100, 0))
        self.clean_image = pygame.image.load('icons/clean.png').convert_alpha()
        self.clean_image_rect = self.clean_image.get_rect(topleft=(200, 0))
        self.food_image = pygame.image.load('icons/food.png').convert_alpha()
        self.food_icon_rect = self.food_image.get_rect(topleft=(400, 0))
        self.food_rect = self.food_image.get_rect()
        self.happy_image = pygame.image.load('icons/game.png').convert_alpha()
        self.happy_image_rect = self.happy_image.get_rect(topleft=(300, 0))
        self.font = pygame.font.Font(None, 36)
        self.hlava = pygame.image.load('icons/hlava.png').convert_alpha()
        self.hlava_rect = self.hlava.get_rect(center=(self.w//2, self.h//2))
        self.krovi_image = pygame.image.load('icons/krovi.png').convert_alpha()
        self.blato_image = pygame.image.load('icons/blato.png').convert_alpha()
        self.krovi_rect = self.krovi_image.get_rect()
        self.krovi2_rect = self.krovi_image.get_rect()
        self.blato_rect = self.blato_image.get_rect()
        self.blato2_rect = self.blato_image.get_rect()
        self.blato3_rect = self.blato_image.get_rect()

    # TODO zvuky
    def play(self):
        self.food_rect.center = (random.randint(0 + self.food_rect.width // 2, self.w - self.food_rect.width // 2),
                                 random.randint(40 + self.food_rect.height // 2, self.h - self.food_rect.height))
        self.krovi_rect.center = (random.randint(0 + self.krovi_rect.width // 2, self.w - self.krovi_rect.width // 2),
                                  random.randint(40 + self.krovi_rect.height // 2, self.h - self.krovi_rect.height))
        self.krovi2_rect.center = (random.randint(0 + self.krovi_rect.width // 2, self.w - self.krovi_rect.width // 2),
                                   random.randint(40 + self.krovi_rect.height // 2, self.h - self.krovi_rect.height))
        self.blato_rect.center = (random.randint(0 + self.blato_rect.width // 2, self.w - self.blato_rect.width // 2),
                                  random.randint(40 + self.blato_rect.height // 2, self.h - self.blato_rect.height))
        self.blato2_rect.center = (random.randint(0 + self.blato_rect.width // 2, self.w - self.blato_rect.width // 2),
                                   random.randint(40 + self.blato_rect.height // 2, self.h - self.blato_rect.height))
        self.blato3_rect.center = (random.randint(0 + self.blato_rect.width // 2, self.w - self.blato_rect.width // 2),
                                   random.randint(40 + self.blato_rect.height // 2, self.h - self.blato_rect.height))
        clock = pygame.time.Clock()
        pokracovat = True
        while pokracovat:
            mouse = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            tired_percent = self.font.render(str(self.vlk.sleepy), True, "orange")
            food_percent = self.font.render(str(self.vlk.food), True, "orange")
            clean_percent = self.font.render(str(self.vlk.clean), True, "orange")
            happy_percent = self.font.render(str(self.vlk.happy), True, "orange")
            self.screen.blit(self.background_image_hra, (0, 0))
            self.screen.blit(self.back_image, self.back_image_rect)
            self.screen.blit(self.sleep_image, self.sleep_image_rect)
            self.screen.blit(self.clean_image, self.clean_image_rect)
            self.screen.blit(self.food_image, self.food_icon_rect)
            self.screen.blit(self.happy_image, self.happy_image_rect)
            self.screen.blit(tired_percent, (140, 0))
            self.screen.blit(clean_percent, (240, 0))
            self.screen.blit(happy_percent,(340,0))
            self.screen.blit(food_percent, (440, 0))
            self.screen.blit(self.krovi_image, self.krovi_rect)
            self.screen.blit(self.krovi_image, self.krovi2_rect)
            self.screen.blit(self.blato_image, self.blato_rect)
            self.screen.blit(self.blato_image, self.blato2_rect)
            self.screen.blit(self.blato_image, self.blato3_rect)
            self.screen.blit(self.food_image, self.food_rect)
            self.screen.blit(self.hlava, self.hlava_rect)

            if self.back_image_rect.collidepoint(mouse):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            for event in pygame.event.get():
                if ((event.type == pygame.QUIT or
                        (event.type == pygame.MOUSEBUTTONDOWN and self.back_image_rect.collidepoint(mouse))) or
                        self.vlk.clean == 0 or self.vlk.happy == 0):
                    pokracovat = False

            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.hlava_rect.top >= 40:
                self.hlava_rect.y -= 10
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.hlava_rect.bottom <= self.h:
                self.hlava_rect.y += 10
            elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.hlava_rect.left >= 0:
                self.hlava_rect.x -= 10
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.hlava_rect.right <= self.w:
                self.hlava_rect.x += 10
                # TODO blato udelat nahodne po case?
                # TODO pridelat unavu
            if self.hlava_rect.colliderect(self.food_rect):
                self.food_rect.center = (random.randint(0 + self.food_rect.width // 2,
                                                        self.w - self.food_rect.width // 2),
                                         random.randint(40 + self.food_rect.height // 2,
                                                        self.h - self.food_rect.height))
                self.blato_rect.center = (
                    random.randint(0 + self.blato_rect.width // 2, self.w - self.blato_rect.width // 2),
                    random.randint(40 + self.blato_rect.height // 2, self.h - self.blato_rect.height))
                self.blato2_rect.center = (
                    random.randint(0 + self.blato_rect.width // 2, self.w - self.blato_rect.width // 2),
                    random.randint(40 + self.blato_rect.height // 2, self.h - self.blato_rect.height))
                self.blato3_rect.center = (
                    random.randint(0 + self.blato_rect.width // 2, self.w - self.blato_rect.width // 2),
                    random.randint(40 + self.blato_rect.height // 2, self.h - self.blato_rect.height))
                if self.vlk.food < 96:
                    self.vlk.food += 5
                else:
                    self.vlk.food = 100

            if (self.hlava_rect.colliderect(self.blato_rect) or
                    self.hlava_rect.colliderect(self.blato2_rect) or
                    self.hlava_rect.colliderect(self.blato3_rect)):
                self.vlk.clean -= 1
                if self.vlk.clean < 0:
                    self.vlk.clean = 0

            if self.hlava_rect.colliderect(self.krovi_rect) or self.hlava_rect.colliderect(self.krovi2_rect):
                self.vlk.happy -= 1
                if self.vlk.happy < 0:
                    self.vlk.happy = 0

            clock.tick(30)
            pygame.display.flip()

        if event.type == pygame.QUIT:
            return False
        else:
            return True
