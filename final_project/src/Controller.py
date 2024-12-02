import pygame
from src import Appliance

class Controller():

    def __init__(self):

        self.screen = pygame.display.set_mode((800,450))
        self.width, self.height = pygame.display.get_window_size()
        self.state = "KITCHEN"

    def mainloop(self):
       
        if self.state == "KITCHEN":
            self.kitchenloop()
        elif self.state == "HUB":
            self.hubloop()
        elif self.state == "START":
            self.tutorial()

    def kitchenloop(self):
    
        while self.state == "KITCHEN":

            #stove = Appliance.Appliance(0, 0, 50, 50, "assets/stovetop.jpg")
            stove = pygame.image.load("assets/stovetop.jpg")
            stove.blit(stove, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.display.flip()
        