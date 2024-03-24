import pygame, datetime

#TODO vlk sleep predelat na stav
class Vlk(pygame.sprite.Sprite):

    def __init__(self, image, sleep, position):
        super().__init__()
        self.image = image
        self.image_sleep = sleep
        self.rect = self.image.get_rect(center=position)
        self.rect_sleep = self.image_sleep.get_rect(center=(position[0],position[1]+self.rect.x//2))
        self.font = pygame.font.Font(None, 36)
        self.food = 80
        self.happy = 100
        self.sleepy = 100
        self.clean = 50
        self.sleep = False
        self.last_check_sleep = datetime.datetime.now()
        self.sleep_time = datetime.datetime.now()

    def draw(self, screen):
        if self.sleep:
            screen.blit(self.image_sleep, self.rect_sleep)
        else:
            screen.blit(self.image, self.rect)

    def draw_stats(self,screen):
        food_percent = self.font.render(str(self.food), True, "orange")
        happy_percent = self.font.render(str(self.happy), True, "orange")
        tired_percent = self.font.render(str(self.sleepy), True, "orange")
        clean_percent = self.font.render(str(self.clean), True, "orange")
        screen.blit(food_percent, (40, 0))
        screen.blit(tired_percent, (140, 0))
        screen.blit(clean_percent, (240, 0))
        screen.blit(happy_percent, (340, 0))

    def update_sleep(self,current_time):
        if (current_time - self.last_check_sleep) >= datetime.timedelta(seconds=5) and not self.sleep:
            self.sleepy -= 5
            self.last_check_sleep = current_time
        elif (current_time - self.sleep_time) >= datetime.timedelta(seconds=10) and self.sleep:
            self.sleepy += 5
            if self.sleepy < 0:
                self.sleepy = 0
            self.sleep_time = current_time
            if self.sleepy == 100:
                self.sleep = False
                self.last_check_sleep = current_time
