import pygame, datetime


# TODO: Předělat vlkův spánek na systém stavů (například FSM - Finite State Machine)
class Vlk(pygame.sprite.Sprite):
    # Konstruktor třídy Vlk
    def __init__(self, image, sleep, position):
        super().__init__()
        self.image = image  # Obrázek vlka, když je vzhůru
        self.image_sleep = sleep  # Obrázek vlka, když spí
        self.rect = self.image.get_rect(center=position)  # Pozice obrázku vlka
        self.rect_sleep = self.image_sleep.get_rect(center=(position[0], position[1]+self.rect.x//2))  # Pozice obrázku vlka při spánku
        self.font = pygame.font.Font(None, 36)  # Font pro zobrazování stavů vlka
        # Inicializace stavů vlka
        self.food = 80  # Stav jídla
        self.happy = 100  # Stav štěstí
        self.sleepy = 100  # Stav únavy
        self.clean = 50  # Stav čistoty
        self.sleep = False  # Určuje, zda vlk spí
        self.last_check_sleep = datetime.datetime.now()  # Čas poslední kontroly spánku
        self.sleep_time = datetime.datetime.now()  # Čas na kontrolu délky spánku

    # Metoda pro vykreslení vlka na obrazovku
    def draw(self, screen):
        # Pokud vlk spí, vykreslí obrázek spícího vlka, jinak vykreslí obrázek vlka vzhůru
        if self.sleep:
            screen.blit(self.image_sleep, self.rect_sleep)
        else:
            screen.blit(self.image, self.rect)

    # Metoda pro vykreslení stavových indikátorů vlka (jídlo, štěstí, únava, čistota)
    def draw_stats(self, screen):
        food_percent = self.font.render(str(self.food), True, "orange")
        happy_percent = self.font.render(str(self.happy), True, "orange")
        tired_percent = self.font.render(str(self.sleepy), True, "orange")
        clean_percent = self.font.render(str(self.clean), True, "orange")
        # Pozicionování stavových indikátorů na obrazovce
        screen.blit(food_percent, (40, 0))
        screen.blit(tired_percent, (140, 0))
        screen.blit(clean_percent, (240, 0))
        screen.blit(happy_percent, (340, 0))

    # Metoda pro aktualizaci stavu spánku vlka
    def update_sleep(self, current_time):
        # Snížení únavy pokud vlk nespí, zvyšení pokud spí
        if (current_time - self.last_check_sleep) >= datetime.timedelta(seconds=5) and not self.sleep:
            self.sleepy -= 5
            self.last_check_sleep = current_time
        elif (current_time - self.sleep_time) >= datetime.timedelta(seconds=10) and self.sleep:
            self.sleepy += 5
            if self.sleepy < 0:
                self.sleepy = 0
            self.sleep_time = current_time
            # Pokud dosáhne úplného odpočinku, vlk se probudí
            if self.sleepy == 100:
                self.sleep = False
                self.last_check_sleep = current_time
