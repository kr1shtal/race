import enemy
import player
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

    shadow = pygame.font.Font("font/PressStart2P-Regular.ttf", 40)
    font = pygame.font.Font("font/PressStart2P-Regular.ttf", 40)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        window.blit(background, (0, 0))

        score_shadow = shadow.render("Score: " + str(enemy_car.score), True, "black")
        score_text = font.render("Score: " + str(enemy_car.score), True, "white")

        window.blit(score_shadow, (20, 20))
        window.blit(score_text, (15, 15))

        player_car.update(window)
        enemy_car.update(window)

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == "__main__":
    player_car = player.Player()
    enemy_car = enemy.Enemy()

    run()
    pygame.quit()
