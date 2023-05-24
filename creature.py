import time
import random


class Creature:
    def __init__(self, age, colour, speed, need_food, strength, x, y, move):
        self.age = age
        self.colour = colour
        self.speed = speed
        self.need_food = need_food
        self.strength = strength
        self.x = x
        self.y = y
        self.move = move
        self.alive = True
        self.deathAge = random.uniform(1, 2) * 60

    def live(self, dt):
        self.age += 1 / dt
        self.x += self.move[0] * self.speed
        self.y += self.move[1] * self.speed
        self.need_food += 1 / dt

        if self.need_food > 30 or self.age > self.deathAge:
            self.alive = False

