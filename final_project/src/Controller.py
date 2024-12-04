import pygame
from src.Button import Button
import json

screen_width = 800
screen_height = 450

class Controller():

    def __init__(self):

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill((255, 255, 255))
        self.width, self.height = pygame.display.get_window_size()
        self.state = "KITCHEN"

        self.data_json = open("src/data.json", "r")
        self.data = json.loads(self.data_json.read())
        self.data_json.close()
        self.object_type = self.data["object_type"]
        self.indv_object = self.data["indv_object"]
        for object in self.object_type:
            self.data[object]["size"]["width"] = self.data[object]["size"]["scale"] * screen_width
            self.data[object]["size"]["height"] = self.data[object]["size"]["scale"] * screen_height
        self.clone = []

    def mainloop(self):
       
        if self.state == "KITCHEN":
            self.kitchenloop()
        elif self.state == "MENU":
            self.menuloop()

    def kitchenloop(self):
    
        background = pygame.image.load("assets/fp_images/background.png")
        background = pygame.transform.scale(background, (screen_width, screen_height))
        self.screen.blit(background, (0,0))

        for object in self.object_type:
            for i in range(self.data[object]["amount"]):
                name = f"{object}{i+1}"
                model = Button(self.data, object, i, self.screen)

                self.indv_object[name] = model


        while self.state == "KITCHEN":
            
            for food in self.data["pan_food"]:
                if self.indv_object[food].click():
                    self.indv_object[food].cook(self.data, self.indv_object, self.indv_object[food].type, "pan", self.screen)
                    print(f"{food} clicked")

            for pan in self.data["pans"]:
                if self.indv_object[pan].click() and len(self.indv_object[pan].rect.collidelistall([self.data["clone_image"][f"{pan}food1"],self.data["clone_image"][f"{pan}food2"]])) == 2:
                    self.indv_object[pan].plate()
                    print(f"{pan} clicked")
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()
        