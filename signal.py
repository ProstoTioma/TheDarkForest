class Signal:
    def __init__(self, x, y, goal_civ, aggressive):
        self.x = x
        self.y = y
        self.goal_x = goal_civ.x
        self.goal_y = goal_civ.y

        self.goal_civ = goal_civ

        self.direct_x = 0
        self.direct_y = 0

        self.aggressive = aggressive

        self.reached = False

    def move(self, speed):
        self.direct_x = self.goal_x - self.x
        self.direct_y = self.goal_y - self.y
        if self.direct_x > 0:
            self.direct_x = 1
        elif self.direct_x < 0:
            self.direct_x = -1
        if self.direct_y > 0:
            self.direct_y = 1
        elif self.direct_y < 0:
            self.direct_y = -1

        self.x += self.direct_x * speed
        self.y += self.direct_y * speed

        if round(self.goal_x) == round(self.x) and round(self.goal_y) == round(self.y):
            self.reached = True
