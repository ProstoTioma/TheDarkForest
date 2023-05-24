import random
import time

import screen
import pygame
import creature
import food
import random


class Evo:
    def __init__(self):
        self.screenSize = 600
        self.screen = screen.Screen(self.screenSize, self.screenSize)
        self.population = []
        self.colours = ['blue', 'yellow', 'green']
        self.clock = pygame.time.Clock()
        self.fd = []
        self.kill_count = 0
        self.dead_count = 0

    def spawn_food(self, n):
        for i in range(n):
            f = food.Food(random.randrange(1, 10), random.randrange(1, self.screenSize),
                          random.randrange(1, self.screenSize))
            self.fd.append(f)

    def eat(self, pop):
        for i in range(len(pop)):
            for f in self.fd:
                if round(pop[i].x) == round(f.x) and round(pop[i].y) == round(f.y):
                    f.alive = False
                    pop[i].need_food -= f.value
                    self.generate_creatures(1, pop, pop[i])

            for j in range(len(pop)):
                if pop[i] != pop[j] and pop[i].alive and pop[j].alive and round(pop[i].x) == round(pop[j].x) and round(
                        pop[i].y) == \
                        round(pop[j].y):
                    self.kill_count += 1
                    if pop[i].strength >= pop[j].strength:
                        pop[j].alive = False
                        pop[j].x = -100
                        pop[j].y = -100
                        pop[i].need_food -= 10
                        pop[i].colour = (255, 0, 0)
                        # print(i, ' ate ', j)
                        self.generate_creatures(1, pop, pop[i])

                    else:
                        pop[i].x = -100
                        pop[i].y = -100
                        pop[i].alive = False
                        pop[j].need_food -= 10
                        pop[j].colour = (255, 0, 0)
                        # print(j, ' ate ', i)
                        self.generate_creatures(1, pop, pop[j])

    def border(self, population):
        for cr in population:
            if cr.x > self.screenSize or cr.x < 0 or cr.y > self.screenSize or cr.y < 0:
                cr.x = random.randrange(0, self.screenSize)
                cr.y = random.randrange(0, self.screenSize)
                cr.move = [random.randint(-1, 1), random.randint(-1, 1)]

    def generate_creatures(self, n, pop, clone):
        if clone is not None:
            cr = creature.Creature(0, clone.colour, clone.speed, 0, clone.strength,
                                   clone.x + 5, clone.y + 5,
                                   [random.randint(-1, 1), random.randint(-1, 1)])
            pop.append(cr)
        else:
            for i in range(n):
                cr = creature.Creature(0, random.choice(self.colours), random.randint(1, 3), 0, random.randrange(1, 11),
                                       random.randint(0, 800), random.randint(0, 800),
                                       [random.randint(-1, 1), random.randint(-1, 1)])
                pop.append(cr)

    def simulate(self):
        age_of_universe = 0
        n = 50
        self.generate_creatures(n, self.population, None)
        # print('Average death age is: ', sum(cr.deathAge for cr in population) / n)
        while True:
            if len(self.population) < 100:
                self.spawn_food(10)
            elif len(self.population) > 300:
                del self.fd[:]
            del self.fd[1000:]
            dead = list()
            for cr in self.population:
                if not cr.alive:
                    dead.append(cr)
            for cr in dead:
                if cr in self.population:
                    self.population.remove(cr)
            self.dead_count += len(dead)
            print('Length of population: ', len(self.population), ' Average age: ',
                  round(sum(cr.age for cr in self.population) / len(self.population)), " Average strength: ",
                  round(sum(cr.strength for cr in self.population)) / len(self.population), " Kill count: ",
                  self.kill_count, " Dead count: ", self.dead_count, " Time: ", age_of_universe)
            dt = self.clock.tick(60)
            age_of_universe += 1 / dt
            pygame.display.update()
            self.screen.screen.fill((100, 100, 100))
            for i in range(len(self.population)):
                if self.population[i].alive:
                    pygame.draw.circle(self.screen.screen, self.population[i].colour,
                                       (self.population[i].x, self.population[i].y), 1)
                    self.population[i].live(dt)
                # if not population[i].alive:
                # print("O no! ", i, ' died at age of ', population[i].age)
            self.eat(self.population)
            self.border(self.population)
            for i in range(len(self.fd)):
                if self.fd[i].alive:
                    pygame.draw.circle(self.screen.screen, (50, 50, 50), (self.fd[i].x, self.fd[i].y), 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break


evo = Evo()
evo.simulate()
