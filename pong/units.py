from __future__ import annotations

import random
from typing import TYPE_CHECKING

import pygame

from .settings import HEIGHT, WIDTH

if TYPE_CHECKING:
    from .game import Game


class BaseUnit:
    """The base class for all appearing units in the game."""

    def __init__(self) -> None:
        self.game: Game
        self.rect: pygame.Rect

    def animation(self) -> None:
        """The animation method that must be overridden by child classes."""
        raise NotImplementedError


class Ball(BaseUnit):
    """The ball unit, all stuff related to the ball is included there.

    This class inherits from `pong.units.BaseUnit`.
    """

    def __init__(self, game: Game) -> None:
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

        if self.rect.left <= 0:
            self.game.counter['player'] += 1
            self.reset()
        if self.rect.right >= WIDTH:
            self.game.counter['opponent'] += 1
            self.reset()

        if self.rect.colliderect(player.rect) or self.rect.colliderect(opponent.rect):
            self.speed_x *= -1

    def reset(self) -> None:
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))


class Player(BaseUnit):
    """The player, all stuff related to the player is included there.

    This class inherits from `pong.units.BaseUnit`.
    """

    def __init__(self, game: Game) -> None:
        self.rect = pygame.Rect(WIDTH - 20, HEIGHT / 2 - 70, 10, 140)
        self.speed = 0

    def animation(self) -> None:
        self.rect.y += self.speed
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


class Opponent(BaseUnit):
    """The opponent, all stuff related to the opponent is included there.

    This class inherits from `pong.units.BaseUnit`.
    """

    def __init__(self, game: Game) -> None:
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
