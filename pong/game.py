import sys
from collections import Counter

import pygame

from .settings import (BG_COLOR, GREY, HEIGHT, MAX_SCORES_PER_MATCH, TITLE,
                       WIDTH)
from .units import Ball, Opponent, Player


class Game:
    def __init__(self) -> None:
        # Setup.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.Font('font/8bit.ttf', 30)

        # Units initialization.
        self.ball = Ball(self)
        self.player = Player(self)
        self.opponent = Opponent(self)

        self.counter = Counter()

    def display_score(self, *, opponent: bool = False) -> None:
        count = self.counter['opponent'] if opponent else self.counter['player']
        message = self.font.render(str(count), False, GREY)
        rect = message.get_rect(center=(WIDTH / 4 if opponent else WIDTH - WIDTH / 4, 30))
        self.screen.blit(message, rect)

    def loop(self) -> None:
        while True:
            # Checking up events.
            self.events()

            # Animating.
            self.ball.animation()
            self.player.animation()
            self.opponent.animation()

            # Visuals.
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
            self.display_score()
            self.display_score(opponent=True)

            pygame.display.flip()
            self.clock.tick(60)

    @staticmethod
    def kill(exit_code: int = 0):
        pygame.quit()
        sys.exit(exit_code)

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (self.counter['player'] >= MAX_SCORES_PER_MATCH or self.counter['opponent'] >= MAX_SCORES_PER_MATCH):
                # TODO: display the ending menu when the score limit reaches.
                self.kill()

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
