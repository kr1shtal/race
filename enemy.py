import random

import pygame

score = 0
cars = [
    "img/red.png",
    "img/green.png",
    "img/blue.png",
]


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(random.choice(cars)), (64, 128)
        )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(130, 610)
        self.rect.y = -128
        self.speed = random.randint(5, 10)

    def spawn_car(self):
        self.rect.y = -128
        self.rect.x = random.randint(130, 610)
        if self.speed < 50:
            self.speed += 1

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        global score
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.spawn_car()
            score += 1

    def update(self, screen):
        self.render(screen)
        self.move()
