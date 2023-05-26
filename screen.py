import math

import pygame


class Screen:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Dark Forest')
        self.screen = pygame.display.set_mode((width, height))

    def draw_civ(self, civ):
        if civ.alive:
            if civ.power < 30:
                size = 2
            elif civ.power < 200:
                size = 5
            else:
                size = 10

            pygame.draw.circle(self.screen, civ.colour,
                               (civ.x, civ.y), size)

            vsb_arc_radius = civ.vsb + size
            vsb_arc_rect = pygame.Rect(0, 0, vsb_arc_radius * 2, vsb_arc_radius * 2)
            vsb_arc_rect.center = civ.x, civ.y

            pygame.draw.arc(self.screen, (255, 255, 255), vsb_arc_rect, 0, math.pi * 2)

            # self.live(dt)

            for signal in civ.signals:
                signal_colour = (0, 200, 0) if not signal.aggressive else (200, 0, 0)
                pygame.draw.line(self.screen, signal_colour,
                                 (signal.x, signal.y), (signal.x + signal.direct_x, signal.y + signal.direct_y))

    def draw(self):
        pygame.display.update()
        self.screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



