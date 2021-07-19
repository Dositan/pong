import sys

import pygame

from .settings import BG_COLOR, GREY, HEIGHT, TITLE, WIDTH
from .units import Ball, Opponent, Player


class Game:
    def __init__(self) -> None:
        # Setup.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        # Units initialization.
        self.ball = Ball(self)
        self.player = Player(self)
        self.opponent = Opponent(self)

    def loop(self) -> None:
        while True:
            # Checking up events.
            self.events()

            # Animating.
            self.ball.animation()
            self.player.animation()
            self.opponent.animation()

            # Visuals
            self.screen.fill(BG_COLOR)
            pygame.draw.rect(self.screen, GREY, self.player)
            pygame.draw.rect(self.screen, GREY, self.opponent)
            pygame.draw.ellipse(self.screen, GREY, self.ball)
            pygame.draw.aaline(
                self.screen,
                GREY,
                (WIDTH / 2, 0),
                (WIDTH / 2, HEIGHT)
            )

            pygame.display.flip()
            self.clock.tick(60)

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.player.speed += 7

                if event.key == pygame.K_UP:
                    self.player.speed -= 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player.speed -= 7

                if event.key == pygame.K_UP:
                    self.player.speed += 7
