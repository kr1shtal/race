import random

import pygame


class Enemy:
    def __init__(self):
        self.image = pygame.transform.scale(
            pygame.image.load("img/green.png"), (64, 128)
        )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(130, 610)
        self.rect.y = -128
        self.speed = random.randint(1, 5)
        self.score = 0

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.y += self.speed

        if self.rect.y > 700:
            self.rect.y = -128
            self.rect.x = random.randint(130, 610)
            self.score += 1
            self.speed += 1

    def update(self, screen):
        self.render(screen)
        self.move()
