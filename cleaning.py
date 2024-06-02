import pygame
import random


class Cleaning:
    def __init__(self, screen, vlk, sound):
        # Initialize the cleaning class with screen, vlk (wolf), and sound
        self.sound_klik = sound
        self.screen = screen
        self.vlk = vlk
        self.w, self.h = pygame.display.get_surface().get_size()
        self.background_image_clean = pygame.image.load('images/cleaning.png').convert()
        self.font = pygame.font.Font(None, 36)
        self.clean_image = pygame.image.load('icons/clean.png').convert_alpha()
        self.clean_image_rect = self.clean_image.get_rect(topleft=(200, 0))
        self.back_image = pygame.image.load('icons/left-arrow.png').convert_alpha()
        self.back_image_rect = self.back_image.get_rect(topleft=(0, 0))
        self.vlk_image = pygame.image.load('images/wolf_shower.png').convert_alpha()
        self.vlk_image_rect = self.vlk_image.get_rect(center=(self.w // 2, self.h - 200))
        self.blato_image = pygame.image.load('icons/blato_mini.png').convert_alpha()
        self.sponge_image = pygame.image.load('icons/sponge.png').convert_alpha()
        self.sponge_image_rect = self.sponge_image.get_rect(topleft=(self.w + 50, self.h + 50))

    # Main method for cleaning action
    def clean(self):
        dirty = (100 - self.vlk.clean) * 4
        cisteni = 0
        blato_rect = []
        pokracovat = True
        clock = pygame.time.Clock()

        # Initialize mud spots
        for i in range(0, dirty):
            blato_rect.append(self.blato_image.get_rect(center=(random.randint(self.vlk_image_rect.left,
                                                                               self.vlk_image_rect.right),
                                                                random.randint(self.vlk_image_rect.top,
                                                                               self.vlk_image_rect.bottom))))

        # Main cleaning loop
        while pokracovat:
            mouse = pygame.mouse.get_pos()
            clean_percent = self.font.render(str(self.vlk.clean), True, "orange")
            self.screen.blit(self.background_image_clean, (0, 0))
            self.screen.blit(self.back_image, self.back_image_rect)
            self.screen.blit(self.clean_image, self.clean_image_rect)
            self.screen.blit(self.vlk_image, self.vlk_image_rect)
            self.screen.blit(clean_percent, (240, 0))

            # Change cursor on hover over back button
            if self.back_image_rect.collidepoint(mouse):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # Draw mud spots and sponge
            for i in range(0, dirty):
                self.screen.blit(self.blato_image, blato_rect[i])
            self.screen.blit(self.sponge_image, self.sponge_image_rect)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and
                                                 self.back_image_rect.collidepoint(mouse)):
                    self.sound_klik.play()
                    pokracovat = False
                elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed() == (1, 0, 0):
                    self.sponge_image_rect.center = event.pos

            # Check for collisions with mud spots
            for blato in blato_rect:
                if self.sponge_image_rect.colliderect(blato):
                    blato.center = (self.w + 100, self.h + 100)
                    cisteni += 0.25
                if cisteni == 1:
                    self.vlk.clean += 1
                    cisteni = 0

            clock.tick(30)
            pygame.display.flip()

        if event.type == pygame.QUIT:
            return False
        else:
            return True
