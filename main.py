import pygame
import datetime
from vlk import Vlk
from ikony import Clean, Game, Sleep, Food
from minigame_food import MinigameFood
from cleaning import Cleaning
from minigame import Minigame

# Initialize Pygame
pygame.init()
height = 512
width = 512

# Set up the game screen
screen = pygame.display.set_mode((width, height))

# Prepare fonts and images
font = pygame.font.Font(None, 36)
background_image = pygame.image.load('images/pozadi.png').convert()
wolf_image = pygame.image.load('images/wolf.png').convert_alpha()
wolf_sleep = pygame.image.load('images/wolf_sleep.png').convert_alpha()
wolf_tired = pygame.image.load('images/wolf_tired.png').convert_alpha()
clean_image = pygame.image.load('icons/clean.png').convert_alpha()
game_image = pygame.image.load('icons/game.png').convert_alpha()
sleep_image = pygame.image.load('icons/sleep.png').convert_alpha()
food_image = pygame.image.load('icons/food.png').convert_alpha()

# Load sound effects
sound_klik = pygame.mixer.Sound("sounds/click.mp3")
sound_success = pygame.mixer.Sound("sounds/success.mp3")

# Set game title
pygame.display.set_caption("Wlck's tamagochi")

# Create game objects
vlk = Vlk(wolf_image, wolf_sleep, wolf_tired, (250, 370))
food = Food(food_image, (0, 0), sound_klik)
sleep = Sleep(sleep_image, (100, 0), sound_klik)
clean = Clean(clean_image, (200, 0), sound_klik)
game = Game(game_image, (300, 0), sound_klik)
minigame_food = MinigameFood(screen, vlk, sound_klik, sound_success)
minigame = Minigame(screen, vlk, sound_klik, sound_success)
cleaning = Cleaning(screen, vlk, sound_klik)

# Main game loop
pokracovat = True
while pokracovat:
    mouse = pygame.mouse.get_pos()
    current_time = datetime.datetime.now()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracovat = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle button clicks
            if food.rect.collidepoint(mouse) and not vlk.sleep and not vlk.tired:
                pokracovat = food.klik(minigame_food)
            elif sleep.rect.collidepoint(mouse) and not vlk.sleep:
                sleep.klik(vlk)
            elif clean.rect.collidepoint(mouse) and not vlk.sleep and not vlk.tired:
                pokracovat = clean.klik(cleaning)
            elif game.rect.collidepoint(mouse) and not vlk.sleep and not vlk.tired:
                pokracovat = game.klik(minigame)
            elif vlk.rect.collidepoint(mouse) and vlk.sleep:
                vlk.sleep = False
                sound_klik.play()

    # Change cursor on hover
    if (food.rect.collidepoint(mouse) or sleep.rect.collidepoint(mouse) or
            clean.rect.collidepoint(mouse) or game.rect.collidepoint(mouse) or
            vlk.rect.collidepoint(mouse)):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Draw the game elements
    screen.blit(background_image, (0, 0))
    screen.blit(food.image, food.rect)
    screen.blit(sleep.image, sleep.rect)
    screen.blit(clean.image, clean.rect)
    screen.blit(game.image, game.rect)
    time_surface = font.render(current_time.strftime('%H:%M'), True, "orange")
    screen.blit(time_surface, (width - time_surface.get_width(), 0))

    # Update the wolf's sleep status
    vlk.update_sleep(current_time)

    # Draw the wolf and its stats
    vlk.draw(screen)
    vlk.draw_stats(screen)

    # Delay for CPU relief and screen update
    pygame.time.delay(100)
    pygame.display.flip()

# Quit the game
pygame.quit()
