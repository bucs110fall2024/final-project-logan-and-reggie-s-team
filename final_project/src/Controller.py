import pygame
import json
from src.Button import Button
from src.Customer import Customer

class Controller():

    def __init__(self):

        # for later for full screen
        dimensions = pygame.display.get_desktop_sizes()
        self.screen_width = dimensions[0][0]
        self.screen_height = dimensions[0][1] - 100

<<<<<<< Updated upstream
        #screen dimensiosn for now
=======
        #screen dimensions for now
>>>>>>> Stashed changes
        # self.screen_width = 800
        # self.screen_height = 450

        #creates screen surface and loads background
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.width, self.height = pygame.display.get_window_size()
        
        #opens json file, dictionary of data is stored in self.data
        self.data_json = open("src/data.json", "r")
        self.data = json.loads(self.data_json.read())
        self.data_json.close()
        #list of ingredients and objects
        self.objects = self.data["objects"]
        #list of customers
        self.customers = []
        #ill clean this up later
        for object in self.objects:
            self.data[object]["size"]["width"] = self.data[object]["size"]["scale"] * self.screen_width
            self.data[object]["size"]["height"] = self.data[object]["size"]["scale"] * self.screen_height
            self.data[object]["act_pos"].append(self.data[object]["rel_pos"][0] * self.screen_width)
            self.data[object]["act_pos"].append(self.data[object]["rel_pos"][1] * self.screen_height)

        for i in range(1,4):
            self.data["customer"]["size"]["width"] = self.data["customer"]["size"]["scale"][0] * self.screen_width
            self.data["customer"]["size"]["height"] = self.data["customer"]["size"]["scale"][1] * self.screen_height
            self.data["customer"]["act_pos"][f"{i}"].append(self.data["customer"]["rel_pos"][f"{i}"][0] * self.screen_width)
            self.data["customer"]["act_pos"][f"{i}"].append(self.data["customer"]["rel_pos"][f"{i}"][1] * self.screen_height)

<<<<<<< Updated upstream
        self.state = "START"
=======
        self.state = "MENU"
>>>>>>> Stashed changes

    def mainloop(self):
       
        while True:
            if self.state == "MENU":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
        
    def menuloop(self):
        print("STATE IS:", self.state)
        while self.state == "MENU":
            menu_background = pygame.image.load("assets/fp_images/start_screen.png")
            menu_background = pygame.transform.scale(menu_background, (self.screen_width, self.screen_height))
            self.screen.blit(menu_background, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "GAME"  
                        print("State changed to:", self.state)

    def gameloop(self):
        
        self.background = pygame.image.load("assets/fp_images/background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.screen.blit(self.background, (0,0))

        #creates a button for all of the ingredients and appliances and stores attributes in json file
        for object in self.objects:
            model = Button(self.data, object, self.screen)
            self.objects[f"{object}"] = model
        #creats models for customers
        for i in range(1, 4):
            customer = Customer(self.data, i)
            self.customers.append(customer)
        
        recipe = ""
        orders = []

        while self.state == "GAME":
            
            #tests if any of the pan ingredients are clicked then puts them on the pan
            for app in self.data["appliances"]:
                for food in self.data[f"{app}_food"][0:-2]:
                    if self.objects[food].click():
                        surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                        surface.fill((0,0,0,0))
                        if self.data["required"][food] == self.data["objects"][app].available:
                            self.data[app]["recipes"][self.data[food]["recipe"]]["ing"][food] = 1
                        self.objects[food].cook(self.data, self.objects[food].type, app, surface)
                        self.screen.blit(surface, (0,0))

                        print(f"{food} clicked")

            #test if any of the appliances are clicked and have the required amount of ingredients
            for app in self.data["appliances"]:
                if self.data["objects"][app].click() and len(self.data["objects"][app].rect.collidelistall([self.data["clone_image"][f"{app}food1"], self.data["clone_image"][f"{app}food2"]])) == self.data[app]["ing_num"]:
                    
                    #if recipe has 2 ingredients
                    if self.data[app]["ing_num"] == 2:
                        if self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][0]] and self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][1]]:
                            recipe = f"{self.data[f"{app}_food"][-2]}"
                            self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][0]] = 0
                            self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][1]] = 0
                        elif self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][2]] and self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][3]]:
                            recipe = f"{self.data[f"{app}_food"][-1]}"
                            self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][2]] = 0
                            self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][3]] = 0
                    #if recipe has 1 ingredient
                    if self.data[app]["ing_num"] == 1:
                        if self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][0]]:
                            recipe = f"{self.data[f"{app}_food"][-2]}"
                            self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][0]] = 0
                        elif self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][1]]:
                            recipe = f"{self.data[f"{app}_food"][-1]}"
                            self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][1]] = 0

                        print(self.data[app]["recipes"][self.data[f"{app}_food"][-2]]["ing"][self.data[f"{app}_food"][0]])
                        print(self.data[app]["recipes"][self.data[f"{app}_food"][-1]]["ing"][self.data[f"{app}_food"][1]])


                    #"serves" product
                    if self.data["objects"][app].available == "Full":
                        self.screen.blit(self.background, (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1]), (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1], self.data[app]["size"]["width"], self.data[app]["size"]["height"]))
                        self.data["objects"][app].available = "Empty"
                        
                        for i in range(1, 4):
                            print(f"cooked_{recipe}{i}")
                            if f"cooked_{recipe}{i}" in orders:
                                orders.remove(f"cooked_{recipe}{i}")
                                break
                        print(orders, recipe)

                        recipe = ""

                    #hides ingredients by putting background back on
                    elif recipe:
                        surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                        surface.fill((0,0,0,0))
                        self.screen.blit(self.background, (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1]), (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1], self.data[app]["size"]["width"], self.data[app]["size"]["height"]))
                        self.data["objects"][f"{app}"].new_image(self.data[app]["size"]["width"], self.data[app]["size"]["height"], f"assets/fp_images/cooked_{recipe}.png", surface)
                        self.screen.blit(surface, (0,0))
                        self.data["objects"][app].available = "Full"
                    

            for cus in self.customers:
                #when no customer
                if cus.waiting:
                    surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                    surface.fill((0,0,0,0))
                    cus.new_order()
                    cus.new_cus(surface)
                    self.screen.blit(surface, (0,0))
                    orders.append(f"{cus.order}{cus.num}")
                    print(cus.order)

                #when customer is served
                if not(f"{cus.order}{cus.num}" in orders) and not(cus.waiting):
                    surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                    surface.fill((0,0,0,0))
                    self.screen.blit(self.background, (cus.order_x, cus.y), (cus.order_x, cus.y, self.data["customer"]["size"]["width"]*2, self.data["customer"]["size"]["height"]))    
                    
                    pygame.time.wait(500)
                    cus.served()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "MENU"
                        print(self.state)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()