# Wlck's Tamagotchi

## Overview
This is an example game demonstrating a virtual pet (Tamagotchi) written in Python using the Pygame library. The player can interact with the pet wolf (`Vlk`) by feeding it, playing with it, cleaning it, and putting it to sleep. The game is designed to show basic game mechanics and handling of different game states.

## Getting Started

### Prerequisites
- Python 3.x
- Pygame library



## Game Controls

    Feed the Wolf: Click on the food icon.
    Put the Wolf to Sleep: Click on the sleep icon.
    Clean the Wolf: Click on the cleaning icon.
    Play with the Wolf: Click on the game icon.
    Wake up the Wolf: Click on the wolf if it is sleeping.

## Customization

For better playability, you may want to change some game constants such as the wolf's initial stats or the speed of the minigames. These constants can be found and modified in the respective Python scripts:

- Vlk class in vlk.py for initial stats (food, happy, sleepy, clean).
- Minigame and MinigameFood classes for adjusting game mechanics and difficulty.

## File Structure

- main.py: The main game loop and initialization of game objects.
- vlk.py: Contains the Vlk class, representing the pet wolf and its behaviors.
- ikony.py: Contains button classes for different actions (feed, sleep, clean, play).
- cleaning.py: Contains the cleaning minigame logic.
- minigame.py: Contains the game minigame logic.
- minigame_food.py: Contains the feeding minigame logic.

## Example Code Snippet

Here's a snippet from main.py showing how the game initializes:
```
# Initialize Pygame
pygame.init()
height = 512
width = 512

# Set up the game screen
screen = pygame.display.set_mode((width, height))

# Create game objects
vlk = Vlk(wolf_image, wolf_sleep, wolf_tired, (250, 370))
food = Food(food_image, (0, 0), sound_klik)
sleep = Sleep(sleep_image, (100, 0), sound_klik)
clean = Clean(clean_image, (200, 0), sound_klik)
game = Game(game_image, (300, 0), sound_klik)
minigame_food = MinigameFood(screen, vlk, sound_klik, sound_success)
minigame = Minigame(screen, vlk, sound_klik, sound_success)
cleaning = Cleaning(screen, vlk, sound_klik)
```

## Contributing

Feel free to fork this project and submit pull requests. Any improvements or suggestions are welcome!
## License

This project is licensed under the MIT License.