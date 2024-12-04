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

    def mainloop(self):
       
        if self.state == "KITCHEN":
            self.kitchenloop()
        elif self.state == "MENU":
            self.menuloop()

    def kitchenloop(self):
    
        for object in self.object_type:
            for i in range(self.data[object]["amount"]):
                name = f"{object}{i+1}"
                model = Button(self.data[object]["pos"][f"{i+1}"][0],self.data[object]["pos"][f"{i+1}"][1],self.data[object]["size"]["width"],self.data[object]["size"]["height"],self.data[object]["image"],self.screen)
                self.indv_object[name] = model

        while self.state == "KITCHEN":
   
            if self.indv_object["beef1"].draw(self.screen):
                self.indv_object["beef1"].cook(self.data, self.indv_object, "pan", self.screen)
                print("clicked")

            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()
        