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
        self.background = pygame.image.load("assets/fp_images/background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.screen.blit(self.background, (0,0))
        self.surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
        
        self.data_json = open("src/data.json", "r")
        self.data = json.loads(self.data_json.read())
        self.data_json.close()
        self.objects = self.data["objects"]
        for object in self.objects:
            
            self.data[object]["size"]["width"] = self.data[object]["size"]["scale"] * self.screen_width
            self.data[object]["size"]["height"] = self.data[object]["size"]["scale"] * self.screen_height
            self.data[object]["act_pos"].append(self.data[object]["rel_pos"][0] * self.screen_width)
            self.data[object]["act_pos"].append(self.data[object]["rel_pos"][1] * self.screen_height)

        self.state = "KITCHEN"

    def mainloop(self):
       
        if self.state == "KITCHEN":
            self.kitchenloop()
        elif self.state == "MENU":
            self.menuloop()

    def kitchenloop(self):

        for object in self.objects:
            model = Button(self.data, object, self.screen)
            self.objects[f"{object}"] = model

        while self.state == "KITCHEN":
            
            for food in self.data["pan_food"]:
                if self.objects[food].click():
                    self.objects[food].cook(self.data, self.objects[food].type, "pan", self.surface)
                    self.screen.blit(self.surface, (0,0))
                    print(f"{food} clicked")

            if self.data["objects"]["pan"].click() and len(self.data["objects"]["pan"].rect.collidelistall([self.data["clone_image"]["panfood1"], self.data["clone_image"]["panfood2"]])) == 2:
                self.screen.blit(self.background, (0,0))
                self.data["objects"]["pan"].new_image(self.data["pan"]["size"]["width"], self.data["pan"]["size"]["height"], "assets/fp_images/cooked_noodles.png", self.surface)
                self.screen.blit(self.surface, (0,0))
                print("pan clicked")
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()