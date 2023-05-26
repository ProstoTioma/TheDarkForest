import random
import time
import math
import pygame

from signal import Signal

random.seed(time.time())


class Civilisation:
    def __init__(self, x, y, agr, vsb, power, speed, d_agr, d_vsb, d_power):
        self.power = power
        self.x = x
        self.y = y
        self.alive = True
        self.age = 0
        self.agr = agr
        self.vsb = vsb
        self.speed = speed

        self.d_agr = d_agr
        self.d_vsb = d_vsb
        self.d_power = d_power

        self.visible_civilisations = []

        self.signals = []

        self.alive = True

        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def send_signal(self, civ, aggressive):
        signal = Signal(self.x, self.y, civ, aggressive)

        self.signals.append(signal)

    def coexist(self, civ):
        self.send_signal(civ, False)

    def ignore(self):
        pass

    def attack(self, civ):
        self.send_signal(civ, True)

    def live(self, dt):
        if self.alive:
            self.power += self.d_power / dt
            self.vsb += self.d_vsb / dt
            self.agr += self.d_agr / dt
            self.age += 1 / dt

            if self.speed < 0.999:
                self.speed += self.d_power

            for sig in self.signals:
                if len(self.signals) > 0:
                    if sig.reached:
                        if sig.aggressive:
                            sig.goal_civ.alive = False
                            self.visible_civilisations.remove(sig.goal_civ)
                            self.power += sig.goal_civ.power * 0.5
                            self.vsb += sig.goal_civ.vsb * 0.5

                        else:
                            self.power += sig.goal_civ.power * 0.2
                            self.vsb += sig.goal_civ.vsb * 0.2

                        self.signals.remove(sig)

                    else:
                        sig.move(self.speed / dt)
