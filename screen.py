import math

import pygame


class Screen:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Dark Forest')
        self.screen = pygame.display.set_mode((width, height))

    def draw(self, population, dt):
        pygame.display.update()
        self.screen.fill((0, 0, 0))

        for i in range(len(population)):
            if population[i].alive:
                if population[i].power < 10:
                    size = 2
                elif population[i].power < 50:
                    size = 5
                else:
                    size = 10

                pygame.draw.circle(self.screen, population[i].colour,
                                   (population[i].x, population[i].y), size)

                vsb_arc = pygame.Rect(population[i].x, population[i].y, population[i].vsb, population[i].vsb)
                vsb_arc.center = population[i].x, population[i].y

                for j in range(len(population)):
                    distance = math.sqrt(
                        (population[j].x - population[i].x) ** 2 + (population[j].y - population[i].y) ** 2)
                    if distance > 0:

                        if distance < population[i].vsb:
                            population[i].visible_civilisations.append(population[j])

                pygame.draw.arc(self.screen, (255, 255, 255),
                                vsb_arc, 0, math.pi * 2)

                population[i].live(dt)

                for signal in population[i].signals:
                    signal_colour = (0, 200, 0) if not signal.aggressive else (200, 0, 0)
                    pygame.draw.line(self.screen, signal_colour,
                                     (signal.x, signal.y), (signal.x + signal.direct_x, signal.y + signal.direct_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
