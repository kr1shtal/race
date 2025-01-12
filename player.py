import pygame


class Player:
    def __init__(self):
        self.image = pygame.transform.scale(
            pygame.image.load("img/black.png"), (64, 128)
        )
        self.rect = self.image.get_rect()
        self.rect.x = 400 - 64
        self.rect.y = 700 - 128
        self.speed = 10

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 570:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.x > 130:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < 610:
            self.rect.x += self.speed

    def update(self, screen):
        self.render(screen)
        self.move()
