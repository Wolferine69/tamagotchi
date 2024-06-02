import pygame, datetime


class Vlk(pygame.sprite.Sprite):
    # Constructor for the Vlk (wolf) class
    def __init__(self, image, sleep, tired, position):
        super().__init__()
        self.image = image  # Image of the wolf when awake
        self.image_sleep = sleep  # Image of the wolf when sleeping
        self.image_tired = tired  # Image of the wolf when tired
        self.rect = self.image.get_rect(center=position)  # Position of the wolf image
        self.rect_sleep = self.image_sleep.get_rect(
            center=(position[0], position[1] + self.rect.x // 2))  # Position of the wolf image when sleeping
        self.font = pygame.font.Font(None, 36)  # Font for displaying wolf's status
        # Initialize wolf's status
        self.food = 80  # Food status
        self.happy = 100  # Happiness status
        self.sleepy = 100  # Sleepiness status
        self.clean = 50  # Cleanliness status
        self.sleep = False  # Whether the wolf is sleeping
        self.tired = False  # Whether the wolf is tired
        self.last_check_sleep = datetime.datetime.now()  # Last check time for sleep
        self.sleep_time = datetime.datetime.now()  # Time to check sleep duration

    # Method to draw the wolf on the screen
    def draw(self, screen):
        if self.sleep:
            screen.blit(self.image_sleep, self.rect_sleep)
        elif self.tired:
            screen.blit(self.image_tired, self.rect)
        else:
            screen.blit(self.image, self.rect)

    # Method to draw the wolf's status indicators (food, happiness, sleepiness, cleanliness)
    def draw_stats(self, screen):
        food_percent = self.font.render(str(self.food), True, "orange")
        happy_percent = self.font.render(str(self.happy), True, "orange")
        tired_percent = self.font.render(str(self.sleepy), True, "orange")
        clean_percent = self.font.render(str(self.clean), True, "orange")
        # Position the status indicators on the screen
        screen.blit(food_percent, (40, 0))
        screen.blit(tired_percent, (140, 0))
        screen.blit(clean_percent, (240, 0))
        screen.blit(happy_percent, (340, 0))

    # Method to update the wolf's sleep status
    def update_sleep(self, current_time):
        if (current_time - self.last_check_sleep) >= datetime.timedelta(seconds=5) and not self.sleep:
            self.sleepy -= 5
            if self.sleepy <= 0:
                self.sleepy = 0
                self.tired = True
            self.last_check_sleep = current_time
        elif (current_time - self.sleep_time) >= datetime.timedelta(seconds=10) and self.sleep:
            self.sleepy += 5
            self.tired = False
            self.sleep_time = current_time
            if self.sleepy == 100:
                self.sleep = False
                self.last_check_sleep = current_time

    def update_game(self, current_time):
        if (current_time - self.last_check_sleep) >= datetime.timedelta(seconds=10) and not self.sleep:
            self.sleepy -= 3
            self.last_check_sleep = current_time
