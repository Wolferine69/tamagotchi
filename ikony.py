import pygame, datetime


# Base Button class
class Button(pygame.sprite.Sprite):
    def __init__(self, image, position, sound):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.sound = sound


# Clean button class
class Clean(Button):
    def __init__(self, image, position, sound):
        super().__init__(image, position, sound)

    def klik(self, cleaning):
        self.sound.play()
        pokracovat = cleaning.clean()
        return pokracovat


# Game button class
class Game(Button):
    def __init__(self, image, position, sound):
        super().__init__(image, position, sound)

    def klik(self, minigame):
        self.sound.play()
        pokracovat = minigame.play()
        return pokracovat


# Sleep button class
class Sleep(Button):
    def __init__(self, image, position, sound):
        super().__init__(image, position, sound)

    def klik(self, vlk):
        self.sound.play()
        if vlk.sleepy < 100:
            vlk.sleep = True
            vlk.sleep_time = datetime.datetime.now()


# Food button class
class Food(Button):
    def __init__(self, image, position, sound):
        super().__init__(image, position, sound)

    def klik(self, minigame):
        self.sound.play()
        pokracovat = minigame.play()
        return pokracovat
