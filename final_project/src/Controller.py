import pygame
from src import Button

screen_width = 800
screen_height = 450
scale = {
    "pan" : [screen_width * 0.1, screen_height * 0.1],
    "beef" : [screen_width * 0.1, screen_height * 0.1],

    }

class Controller():

    def __init__(self):

        
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill((255, 255, 255))
        self.width, self.height = pygame.display.get_window_size()
        self.state = "KITCHEN"

    def mainloop(self):
       
        if self.state == "KITCHEN":
            self.kitchenloop()
        elif self.state == "MENU":
            self.menuloop()
        elif self.state == "TUTORIAL":
            self.tutorial()

    def kitchenloop(self):
    
        beef = Button.Button(400, 200, scale["beef"], "beef", "assets/fp_images/beef.png")
        pan1 = Button.Button(100, 200, scale["pan"], "pan", "assets/fp_images/pan.png")
        pan2 = Button.Button(200, 200, scale["pan"], "pan", "assets/fp_images/pan.png")
        pan3 = Button.Button(100, 100, scale["pan"], "pan", "assets/fp_images/pan.png")
        pan4 = Button.Button(200, 100, scale["pan"], "pan", "assets/fp_images/pan.png")
        print(pan1.available, pan2.available, pan3.available, pan4.available)

        while self.state == "KITCHEN":
            
            pan1.draw(self.screen)
            pan2.draw(self.screen)
            pan3.draw(self.screen)
            pan4.draw(self.screen)

            if beef.draw(self.screen):
                if pan1.available:
                    beef.cook(pan1.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                    pan1.available = False
                elif pan2.available:
                    beef.cook(pan2.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                    pan2.available = False           
                elif pan3.available:
                    beef.cook(pan3.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                    pan3.available = False               
                elif pan4.available:
                    beef.cook(pan4.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                    pan4.available = False


                print("clicked")

            
            
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            
            pygame.display.flip()
        