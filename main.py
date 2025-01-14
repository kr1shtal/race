import random

import enemy
import player
import pygame

width, height = 800, 700

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing")

is_game_over = False


def game_over():
    global is_game_over

    is_game_over = True

    game_over_shadow = game_over_font.render("Game Over!", True, "black")
    game_over_text = game_over_font.render("Game Over!", True, "crimson")

    restart_shadow = font.render("SPACE to restart", True, "black")
    restart_text = font.render("SPACE to restart", True, "white")

    window.blit(game_over_shadow, (110, 250))
    window.blit(game_over_text, (105, 245))

    window.blit(restart_shadow, (105, 350))
    window.blit(restart_text, (100, 345))


def restart():
    global is_game_over

    is_game_over = False

    player_car.rect.x = 400 - 64
    player_car.rect.y = 700 - 128
    player_car.score = 0
    player_car.life = 3

    enemy_car.rect.x = random.randint(130, 610)
    enemy_car.rect.y = -128


def render_text():
    score_shadow = font.render("Score:" + str(enemy_car.score), True, "black")
    score_text = font.render("Score:" + str(enemy_car.score), True, "white")

    life_shadow = font.render("Life:" + str(player_car.life), True, "black")
    life_text = font.render("Life:" + str(player_car.life), True, "white")

    window.blit(score_shadow, (20, 20))
    window.blit(score_text, (15, 15))

    window.blit(life_shadow, (500, 20))
    window.blit(life_text, (495, 15))


def run():
    global is_game_over

    pygame.init()

    background = pygame.transform.scale(
        pygame.image.load("img/background.png"), (width, height)
    )

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        if keys[pygame.K_SPACE] and is_game_over:
            restart()

        if not is_game_over:
            window.blit(background, (0, 0))

            player_car.update(window)
            enemy_car.update(window)

            if player_car.rect.colliderect(enemy_car.rect):
                enemy_car.rect.y = -128
                enemy_car.rect.x = random.randint(130, 610)
                player_car.life -= 1
                player_car.rect.y = height - 128

                if player_car.life == 0:
                    game_over()

            render_text()

            pygame.display.flip()
            pygame.time.Clock().tick(60)


if __name__ == "__main__":
    pygame.font.init()

    font = pygame.font.Font("font/PressStart2P-Regular.ttf", 40)
    game_over_font = pygame.font.Font("font/PressStart2P-Regular.ttf", 64)

    player_car = player.Player()
    enemy_car = enemy.Enemy()

    run()
    pygame.quit()
