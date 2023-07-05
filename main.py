import pygame
from fighter import Character

# Initialization
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fight!")

background = pygame.image.load("assets\stages\stage ctown.png").convert_alpha()

# Functions
def drawBackground():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))

player1 = Character(200, 310)
player2 = Character(700, 310)

# Loop
run = True
while run:

    # Make Background
    drawBackground()

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update Display
    pygame.display.update()


pygame.quit()