import pygame
from src.Button import Button
import json

class Controller():

    def __init__(self):

        # for later for full screen
        # dimensions = pygame.display.get_desktop_sizes()
        # self.screen_width = dimensions[0][0]
        # self.screen_height = dimensions[0][1]

        #screen dimensiosn for now
        self.screen_width = 800
        self.screen_height = 450

        #creates screen surface and loads background
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.width, self.height = pygame.display.get_window_size()
        self.background = pygame.image.load("assets/fp_images/background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.screen.blit(self.background, (0,0))

        
        #opens json file, dictionary of data is stored in self.data
        self.data_json = open("src/data.json", "r")
        self.data = json.loads(self.data_json.read())
        self.data_json.close()
        #list of ingredients and objects
        self.objects = self.data["objects"]
        #ill clean this up later
        for object in self.objects:
            self.data[object]["size"]["width"] = self.data[object]["size"]["scale"] * self.screen_width
            self.data[object]["size"]["height"] = self.data[object]["size"]["scale"] * self.screen_height
            self.data[object]["act_pos"].append(self.data[object]["rel_pos"][0] * self.screen_width)
            self.data[object]["act_pos"].append(self.data[object]["rel_pos"][1] * self.screen_height)

        #creates separate surface where ingredient copies and products are shown
        # self.surfaces = {}
        # for app in (self.data["appliances"]):
        #     for _ in ["ingredients", "products"]:
        #         surface = pygame.Surface((self.screen_width, self.screen_height))
        #         surface.fill((0,0,0,0))
        #         self.surfaces[f"{app}_" + _] = surface

        #state is kitchen
        self.state = "KITCHEN"

    def mainloop(self):
       
        #goes to kitchen loop
        if self.state == "KITCHEN":
            self.kitchenloop()
        #idea is to go to pause menu where recipes are shown
        elif self.state == "MENU":
            self.menuloop()

    def kitchenloop(self):

        #creates a button for all of the ingredients and appliances and stores attributes in json file
        for object in self.objects:
            model = Button(self.data, object, self.screen)
            self.objects[f"{object}"] = model


        while self.state == "KITCHEN":
            
            #tests if any of the pan ingredients are clicked then puts them on the pan
            for app in self.data["appliances"]:
                for food in self.data[f"{app}_food"][0:-2]:
                    if self.objects[food].click():
                        surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                        surface.fill((0,0,0,0))
                        self.objects[food].cook(self.data, self.objects[food].type, app, surface)
                        self.screen.blit(surface, (0,0))
                        self.data[app]["recipes"][self.data[food]["recipe"]]["ing"][food] = 1
                        print(f"{food} clicked")
                        print(self.data["objects"][app].available)

            #test if any of the appliances are clicked and have the required amount of ingredients
            for app in self.data["appliances"]:
                recipe = ""
                if self.data["objects"][app].click() and len(self.data["objects"][app].rect.collidelistall([self.data["clone_image"][f"{app}food1"], self.data["clone_image"][f"{app}food2"]])) == self.data[app]["ing_num"]:
                    #if recipe has 2 ingredients
                    if self.data[app]["ing_num"] == 2:
                        if self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][0]] and self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][1]]:
                            recipe = f"{self.data[f"{app}_food"][-2]}"
                            self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][1]] = 0
                            self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][2]] = 0
                        elif self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][2]] and self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][3]]:
                            recipe = f"{self.data[f"{app}_food"][-1]}"
                            self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][1]] = 0
                            self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][2]] = 0
                    #if recipe has 1 ingredient
                    elif self.data[app]["ing_num"] == 1:
                        if self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][0]]:
                            recipe = f"{self.data[f"{app}_food"][-2]}"
                        elif self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][1]]:
                            recipe = f"{self.data[f"{app}_food"][-1]}"
                
                    #hides ingredients by putting background back on but it doesnt remove the rectangles or surfaces
                    if recipe:
                        surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                        surface.fill((0,0,0,0))
                        self.screen.blit(self.background, (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1]), (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1], self.data[app]["size"]["width"], self.data[app]["size"]["height"]))
                        self.data["objects"][f"{app}"].new_image(self.data[app]["size"]["width"], self.data[app]["size"]["height"], f"assets/fp_images/cooked_{recipe}.png", surface)
                        self.screen.blit(surface, (0,0))
                        self.data["objects"][app].available = "Full"

                    elif self.data["objects"][app].available == "Full":
                        self.screen.blit(self.background, (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1]), (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1], self.data[app]["size"]["width"], self.data[app]["size"]["height"]))
                        print(self.data["objects"][app].available)
                        self.data["objects"][app].available = "Empty"

                    

                    print(f"{app} clicked")
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()