import pygame

width, height = 800, 700

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing")


def run():
    pygame.init()

    background = pygame.transform.scale(
        pygame.image.load("img/background.png"), (width, height)
    )

    pygame.font.init()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        window.blit(background, (0, 0))

        pygame.display.update()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    run()
    pygame.quit()
