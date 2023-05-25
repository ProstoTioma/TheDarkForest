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

    def generate_civilisations(self, n, pop):
        for i in range(n):
            power = random.uniform(0, 5)
            vsb = random.uniform(power, 10)
            agr = random.uniform(0, 10)
            speed = random.uniform(0.1, 0.999)
            civ = Civilisation(random.randint(0, self.screen_width), random.randint(0, self.screen_height),
                               agr, vsb, power,
                               speed, random.uniform(0, 0.01), random.uniform(0, 0.05),
                               random.uniform(0, 0.01))

            pop.append(civ)

    def simulate(self):
        age_of_universe = 0
        n = 300
        self.generate_civilisations(n, self.population)
        while True:
            if len(self.population) > 0:
                print('Length of population: ', len(self.population), ' Average age: ',
                      round(sum(civ.age for civ in self.population) / len(self.population)), " Average power: ",
                      round(sum(civ.power for civ in self.population)) / len(self.population), " Dead count: ",
                      self.dead_count, " Time: ", age_of_universe)
                dt = self.clock.tick(60)
                age_of_universe += 1 / dt

                for civ in self.population:
                    if not civ.alive:
                        self.dead_count += 1
                        self.population.remove(civ)

                    else:
                        if len(civ.visible_civilisations) > 0:
                            target = random.choice(civ.visible_civilisations)
                            if random.randint(0, 20) == 15:
                                civ.coexist(target)
                            elif random.randint(0, 20) == 15:
                                civ.attack(target)
                            else:
                                civ.ignore()

                    for j in range(len(self.population)):
                        distance = math.sqrt(
                            (self.population[j].x - civ.x) ** 2 + (self.population[j].y - civ.y) ** 2)
                        if distance > 0:

                            if distance < civ.vsb:
                                civ.visible_civilisations.append(self.population[j])

                self.screen.draw(self.population, dt)

                if random.randint(0, 1000) == 10:
                    self.generate_civilisations(1, self.population)


evo = Forest()
evo.simulate()
