import pygame
from src.Building import Building
from src.Button import Button

class Controller():

    def __init__(self):
        """
        docstring
        """

    def mainloop(self):
        """
        docstring
        """

        run = True
        while(run): #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #2. detect collisions and update models

            #3. Redraw next frame

            #4. Display next frame
            pygame.display.flip()