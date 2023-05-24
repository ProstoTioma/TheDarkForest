import pygame


class Screen:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('Evolution')
        self.screen = pygame.display.set_mode((width, height))




