import math
import random
import time

import pygame

from civilisation import Civilisation
from screen import Screen


class Forest:
    random.seed(time.time())

    def __init__(self):
        self.screen_width = 1300
        self.screen_height = 850
        self.screen = Screen(self.screen_width, self.screen_height)
        self.population = []
        self.clock = pygame.time.Clock()
        self.fd = []
        self.dead_count = 0

    def generate_civilisations(self, n):
        pop = []
        for i in range(n):
            power = random.uniform(0, 5)
            vsb = random.uniform(power, 10)
            agr = random.uniform(0, 10)
            speed = random.uniform(0.1, 9.999)
            civ = Civilisation(random.randint(0, self.screen_width), random.randint(0, self.screen_height),
                               agr, vsb, power,
                               speed, random.uniform(0, 0.5),
                               random.uniform(0, 0.1))

            pop.append(civ)
        return pop

    def simulate(self):
        age_of_universe = 0
        n = 150
        self.population = self.generate_civilisations(n)
        while True:
            if len(self.population) > 0:
                if round(age_of_universe) % 10 == 0:
                    print('Length of population: ', len(self.population) - self.dead_count, " Average power: ",
                          round(sum(civ.power for civ in self.population if civ.alive)) / len(self.population),
                          " Dead count: ",
                          self.dead_count, " Time: ", round(age_of_universe), " Visible Civs: ",
                          round(sum(len(civ.visible_civilisations) for civ in self.population)),
                          " Average aggressive: ",
                          round(sum(civ.agr for civ in self.population if civ.alive)) / len(self.population))
                dt = self.clock.tick(60)
                age_of_universe += 1 / dt

                self.dead_count = sum(not civ.alive for civ in self.population)

                self.screen.draw()
                for civ in self.population:
                    if civ.alive:
                        civ.live(dt)
                        self.screen.draw_civ(civ)
                        if len(civ.visible_civilisations) > 0:
                            target = random.choice(civ.visible_civilisations)
                            if civ.agr < 5:
                                if target not in civ.alliances:
                                    if random.randint(0, 100) == 1:
                                        civ.coexist(target)
                            elif civ.agr > 9:
                                if random.randint(0, 100) == 1:
                                    civ.attack(target)
                            else:
                                civ.ignore()

                        for j in range(len(self.population)):
                            if not self.population[j].alive:
                                if self.population[j] in civ.visible_civilisations:
                                    civ.visible_civilisations.remove(self.population[j])
                            else:
                                if self.population[j] in civ.alliances:
                                    self.screen.draw_alliance(civ, self.population[j])
                            distance = math.sqrt(
                                (self.population[j].x - civ.x) ** 2 + (self.population[j].y - civ.y) ** 2)
                            if distance > 0:
                                if distance < civ.vsb and self.population[j].alive:
                                    ids = [civ.id for civ in civ.visible_civilisations]
                                    if self.population[j].id not in ids:
                                        civ.visible_civilisations.append(self.population[j])

                # if random.randint(0, 1000) == 10: TODO spawn new civs
                #    self.population = self.generate_civilisations(1)


evo = Forest()
evo.simulate()
