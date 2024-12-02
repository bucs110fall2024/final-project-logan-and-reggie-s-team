import pygame

class Appliance():

    def __init__(self, x, y, width, height, img_file):
        self.rectangle = pygame.Rect(x, y, width, height)
        self.surface = pygame.Surface((width, height))
        self.image = pygame.image.load(img_file)
        self.image.blit(self.image, (0,0))