import pygame
from src.Button import Button
import json

screen_width = 800
screen_height = 450
# scale = {
#     "pan" : [screen_width * 0.1, screen_height * 0.1],
#     "beef" : [screen_width * 0.1, screen_height * 0.1],

#     }
data_json = open("data.json", "r")
dict_data = json.loads(data_json.read())
data_json.close()
print(dict_data)

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

    def kitchenloop(self):
    
        # beef = Button(400, 200, scale["beef"], "beef", "assets/fp_images/beef.png", self.screen)
        # pan1 = Button(100, 200, scale["pan"], "pan", "assets/fp_images/pan.png", self.screen)
        # pan2 = Button(200, 200, scale["pan"], "pan", "assets/fp_images/pan.png", self.screen)
        # pan3 = Button(100, 100, scale["pan"], "pan", "assets/fp_images/pan.png", self.screen)
        # pan4 = Button(200, 100, scale["pan"], "pan", "assets/fp_images/pan.png", self.screen)

        while self.state == "KITCHEN":
   
            #if beef.draw(self.screen):
                # if pan1.available:
                #     beef.cook(pan1.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                #     pan1.available = False
                # elif pan2.available:
                #     beef.cook(pan2.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                #     pan2.available = False           
                # elif pan3.available:
                #     beef.cook(pan3.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                #     pan3.available = False               
                # elif pan4.available:
                #     beef.cook(pan4.rect.topleft, scale["pan"], "assets/fp_images/beef.png", self.screen)
                #     pan4.available = False
                # print("clicked")

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()
        