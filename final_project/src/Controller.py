import pygame
from src.Button import Button
import json


class Controller():

    def __init__(self):

        # dimensions = pygame.display.get_desktop_sizes()
        # self.screen_width = dimensions[0][0]
        # self.screen_height = dimensions[0][1]

        self.screen_width = 800
        self.screen_height = 450

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.width, self.height = pygame.display.get_window_size()
        
        self.screen2 = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)

        self.data_json = open("src/data.json", "r")
        self.data = json.loads(self.data_json.read())
        self.data_json.close()
        self.object_type = self.data["object_type"]
        self.indv_object = self.data["indv_object"]
        for object in self.object_type:
            self.data[object]["size"]["width"] = self.data[object]["size"]["scale"] * self.screen_width
            self.data[object]["size"]["height"] = self.data[object]["size"]["scale"] * self.screen_height

        self.state = "KITCHEN"

    def mainloop(self):
       
        if self.state == "KITCHEN":
            self.kitchenloop()
        elif self.state == "MENU":
            self.menuloop()

    def kitchenloop(self):
    
        background = pygame.image.load("assets/fp_images/background.png")
        background = pygame.transform.scale(background, (self.screen_width, self.screen_height))
        self.screen.blit(background, (0,0))

        for object in self.object_type:
            for i in range(self.data[object]["amount"]):
                name = f"{object}{i+1}"
                model = Button(self.data, object, i, self.screen)

                self.indv_object[name] = model


        while self.state == "KITCHEN":
            
            for food in self.data["pan_food"]:
                if self.indv_object[food].click():
                    self.indv_object[food].cook(self.data, self.indv_object, self.indv_object[food].type, "pan", self.screen2)
                    self.screen.blit(self.screen2, (0,0))
                    
                    print(f"{food} clicked")

            for pan in self.data["pans"]:
                if self.indv_object[pan].click() and len(self.indv_object[pan].rect.collidelistall([self.data["clone_image"][f"{pan}food1"]["rect"], self.data["clone_image"][f"{pan}food2"]["rect"]])) == 2:
                    # print(self.data["clone_image"]["pan1food1"]["image"], self.data["clone_image"]["pan1food2"]["image"])
                    #self.indv_object[pan].plate(self.data, pan, self.screen2)
                    self.screen2.set_alpha(0)
                    print(f"{pan} clicked")
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()
        