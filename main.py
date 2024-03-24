import pygame
import datetime
from vlk import Vlk
from ikony import Clean, Game, Sleep, Food
from minigame_food import MinigameFood
from cleaning import Cleaning
from minigame import Minigame

# Inicializace Pygame knihovny
pygame.init()
height = 512
width = 512

# Nastavení displeje pro hru
screen = pygame.display.set_mode((width, height))

# Příprava fontu pro zobrazení času a dalších textových elementů
font = pygame.font.Font(None, 36)

# Načtení a příprava grafiky pro hru
background_image = pygame.image.load('images/pozadi.png').convert()
wolf_image = pygame.image.load('images/wolf.png').convert_alpha()
wolf_sleep = pygame.image.load('images/wolf_sleep.png').convert_alpha()
# Ikony pro různé akce ve hře
clean_image = pygame.image.load('icons/clean.png').convert_alpha()
game_image = pygame.image.load('icons/game.png').convert_alpha()
sleep_image = pygame.image.load('icons/sleep.png').convert_alpha()
food_image = pygame.image.load('icons/food.png').convert_alpha()

# Načtení zvukového efektu pro kliknutí
sound_klik = pygame.mixer.Sound("sounds/click.mp3")

# Nastavení titulku hry
pygame.display.set_caption("Wlck's tamagochi")

# Vytvoření herních objektů
vlk = Vlk(wolf_image, wolf_sleep, (250, 370))
food = Food(food_image, (0, 0), sound_klik)
sleep = Sleep(sleep_image, (100, 0), sound_klik)
clean = Clean(clean_image, (200, 0), sound_klik)
game = Game(game_image, (300, 0), sound_klik)
minigame_food = MinigameFood(screen, vlk, sound_klik)
minigame = Minigame(screen, vlk, sound_klik)
cleaning = Cleaning(screen, vlk, sound_klik)

# Hlavní smyčka hry
pokracovat = True
while pokracovat:
    mouse = pygame.mouse.get_pos()
    current_time = datetime.datetime.now()

    # Zpracování událostí (vstup od uživatele)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovat = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Interakce s ikonami na základě pozice kliknutí
            if food.rect.collidepoint(mouse) and not vlk.sleep:
                pokracovat = food.klik(minigame_food)
            elif sleep.rect.collidepoint(mouse) and not vlk.sleep:
                sleep.klik(vlk)
            elif clean.rect.collidepoint(mouse) and not vlk.sleep:
                pokracovat = clean.klik(cleaning)
            elif game.rect.collidepoint(mouse) and not vlk.sleep:
                pokracovat = game.klik(minigame)
            elif vlk.rect.collidepoint(mouse) and vlk.sleep:
                vlk.sleep = False
                sound_klik.play()

    # Změna kurzoru myši na "hand" pokud je nad interaktivním objektem
    if (food.rect.collidepoint(mouse) or sleep.rect.collidepoint(mouse) or
            clean.rect.collidepoint(mouse) or game.rect.collidepoint(mouse) or
            vlk.rect.collidepoint(mouse)):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Vykreslení grafických prvků hry
    screen.blit(background_image, (0, 0))
    # Ikony a čas
    screen.blit(food.image, food.rect)
    screen.blit(sleep.image, sleep.rect)
    screen.blit(clean.image, clean.rect)
    screen.blit(game.image, game.rect)
    time_surface = font.render(current_time.strftime('%H:%M'), True, "orange")
    screen.blit(time_surface, (width - time_surface.get_width(), 0))

    # Logika pro aktualizaci stavu spánku vlka
    vlk.update_sleep(current_time)

    # Vykreslení vlka a jeho statistik
    vlk.draw(screen)
    vlk.draw_stats(screen)

    # Zpoždění pro snížení zátěže procesoru a aktualizace obrazovky
    pygame.time.delay(100)
    pygame.display.flip()

# Ukončení hry
pygame.quit()