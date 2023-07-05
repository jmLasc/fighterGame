import pygame

class Character():
    def __init__(self, x, y):
        self.leftFacing = False
        self.rect = pygame.Rect(x, y, 80, 180)
        self.health = 100
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        
    def move(self, screen_width, screen_height, surface, target): # TODO
        MOVSPEED = 10
        GRAV = 3 
        dx = 0
        dy = 0

        # Get Input
        key = pygame.key.get_pressed()

        # Moving along x
        if not self.attacking:
            if key[pygame.K_a]:
                dx = -MOVSPEED
            if key[pygame.K_d]:
                dx = MOVSPEED

            # Jump
            if self.jump == False and key[pygame.K_w]:
                self.vel_y = -35
                self.jump = True
            self.vel_y += GRAV
            dy += self.vel_y

        # Check Bounds
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 50:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 50 - self.rect.bottom
            
        # Maintain proper facing
        if target.rect.centerx < self.rect.centerx:
            self.leftFacing = True
        else:
            self.leftFacing = False

        # Update Position
        self.rect.x += dx
        self.rect.y += dy

        # Attacking
        if key[pygame.K_q] or key[pygame.K_e]:
            self.attack(surface, target)
            if key[pygame.K_q]:
                self.attack_type = 1
            if key[pygame.K_e]:
                self.attack_type = 2

    def attack(self, surface, target):
        self.attacking = True
        hitbox = pygame.Rect(self.rect.centerx - (2 * self.leftFacing * self.rect.width), self.rect.y, 2 * self.rect.width, self.rect.height)
        pygame.draw.rect(surface, '#0011ff', hitbox)
        if hitbox.colliderect(target.rect):
            target.health -= 10
        self.attacking = False

    def draw(self, surface):
        pygame.draw.rect(surface, '#ff0000', self.rect)