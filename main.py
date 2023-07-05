import pygame
from fighter import Character

# Initialization
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fight!")

background = pygame.image.load("assets\stages\stage ctown.png").convert_alpha()

# Set FPS
clock = pygame.time.Clock()
FPS = 60

# Functions
def drawBackground():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))

def drawHealth(health, x, y):
    hpRatio = health / 100
    pygame.draw.rect(screen, '#000000', (x - 3, y - 3, 406, 36))
    pygame.draw.rect(screen, '#ffff00', (x, y, hpRatio * 400, 30))  



player1 = Character(200, 370)
player2 = Character(800, 370)

# Loop
run = True
while run:
    clock.tick(FPS)
    
    # Drawing Stage
    drawBackground()

    # Drawing Stats
    drawHealth(player1.health, 20, 20)
    drawHealth(player2.health, SCREEN_WIDTH - 420, 20)

    # Movement
    player1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player2)

    # Draw Fighers
    player1.draw(screen)
    player2.draw(screen)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update Display
    pygame.display.update()


pygame.quit()