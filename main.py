import pygame

# Initialization
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fight!")

background = pygame.image.load(filename)


run = True
while run:

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()