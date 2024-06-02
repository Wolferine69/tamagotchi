import pygame
import random


class Minigame:
    def __init__(self, screen, vlk, sound, sound_success):
        # Initialize the minigame with screen, vlk (wolf), and sounds
        self.screen = screen
        self.vlk = vlk
        self.sound_klik = sound
        self.sound_success = sound_success
        self.w, self.h = pygame.display.get_surface().get_size()
        self.background_image_hra = pygame.image.load('images/game_pozadi.png').convert()
        self.font = pygame.font.Font(None, 36)
        self.back_image = pygame.image.load('icons/left-arrow.png').convert_alpha()
        self.back_image_rect = self.back_image.get_rect(topleft=(0, 0))
        self.hlava = pygame.image.load('icons/hlava.png').convert_alpha()
        self.hlava_rect = self.hlava.get_rect(center=(40, self.h // 2))
        self.sleep_image = pygame.image.load('icons/sleep.png').convert_alpha()
        self.sleep_image_rect = self.sleep_image.get_rect(topleft=(100, 0))
        self.happy_image = pygame.image.load('icons/game.png').convert_alpha()
        self.happy_image_rect = self.happy_image.get_rect(topleft=(300, 0))
        self.ball_image = pygame.image.load('images/ball.png').convert_alpha()
        self.ball_rect = self.happy_image.get_rect()
        self.place_ball()
        self.ball_speed = 5

    def play(self):
        # Main minigame loop
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

            # Change cursor on hover over back button
            if self.back_image_rect.collidepoint(mouse):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # Handle events
            for event in pygame.event.get():
                if (((event.type == pygame.QUIT or
                      (event.type == pygame.MOUSEBUTTONDOWN and self.back_image_rect.collidepoint(mouse)))) or
                        self.vlk.happy == 100 or self.vlk.sleepy == 0):
                    self.sound_klik.play()
                    pokracovat = False

            # Move head with keys
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.hlava_rect.top >= 40:
                self.hlava_rect.y -= 5
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.hlava_rect.bottom <= self.h:
                self.hlava_rect.y += 5

            # Move the ball and check for collisions
            if self.ball_rect.x < 0:
                self.place_ball()
                self.ball_speed += 0.5
                self.vlk.sleepy -= 1
                if self.vlk.sleepy < 0:
                    self.vlk.sleepy = 0
            else:
                self.ball_rect.x -= self.ball_speed

            if self.hlava_rect.colliderect(self.ball_rect):
                if self.vlk.happy < 96:
                    self.vlk.happy += 5
                else:
                    self.vlk.happy = 100
                self.sound_success.play()
                self.place_ball()
                self.ball_speed += 2

            clock.tick(60)
            pygame.display.flip()

        if event.type == pygame.QUIT:
            return False
        else:
            return True

    def place_ball(self):
        # Place the ball at a random position
        self.ball_rect.center = (self.w, random.randint(40 + (self.ball_rect.height // 2),
                                                        self.h - (self.ball_rect.height // 2)))
