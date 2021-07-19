import random

import pygame

from .settings import HEIGHT, WIDTH


class Ball:
    """The ball sprite, all stuff related to the ball is included there."""

    def __init__(self, game) -> None:
        self.game = game
        self.rect = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 - 15, 30, 30)
        self.speed_x = 7 * random.choice((1, -1))
        self.speed_y = 7 * random.choice((1, -1))

    def animation(self) -> None:
        player = self.game.player
        opponent = self.game.opponent

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.reset()

        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent):
            self.speed_x *= -1

    def reset(self) -> None:
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))


class Player:
    def __init__(self, game) -> None:
        self.rect = pygame.Rect(WIDTH - 20, HEIGHT / 2 - 70, 10, 140)
        self.speed = 0

    def animation(self) -> None:
        self.rect.y += self.speed
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


class Opponent:
    def __init__(self, game) -> None:
        self.game = game
        self.rect = pygame.Rect(10, HEIGHT / 2 - 70, 10, 140)
        self.speed = 7

    def animation(self) -> None:
        ball = self.game.ball
        player = self.game.player

        if self.rect.top < ball.rect.y:
            self.rect.top += self.speed

        if self.rect.bottom > ball.rect.y:
            self.rect.bottom -= self.speed

        if player.rect.top <= 0:
            player.rect.top = 0

        if player.rect.bottom >= HEIGHT:
            player.rect.bottom = HEIGHT
