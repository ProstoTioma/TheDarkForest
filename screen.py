import math

import pygame


class Screen:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Dark Forest')
        self.screen = pygame.display.set_mode((width, height))

    def draw(self, civilisations, dt):
        pygame.display.update()
        self.screen.fill((0, 0, 0))

        for i in range(len(civilisations)):
            civ = civilisations[i]
            civ.live(dt)
            civ.draw(self.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
