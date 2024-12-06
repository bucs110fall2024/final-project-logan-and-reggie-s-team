import pygame
import json
from src.Button import Button
from src.Customer import Customer
from src.Timer import Timer


class Controller():


    def __init__(self):

        dimensions = pygame.display.get_desktop_sizes()
        self.screen_width = dimensions[0][0]
        self.screen_height = dimensions[0][1] - 50
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        #opens json file, dictionary of data is stored in self.data
        self.data_json = open("src/data.json", "r")
        self.data = json.loads(self.data_json.read())
        self.data_json.close()

        #list for objects
        self.objects = self.data["objects"]
        self.customers = []
        self.timers = []

        #uses objects scale to give them size and position relative to the screen
        for object in self.objects:
            object_data = self.data[object]
            object_data["size"]["width"] = object_data["size"]["scale"] * self.screen_width
            object_data["size"]["height"] = object_data["size"]["scale"] * self.screen_height
            object_data["act_pos"].extend([object_data["rel_pos"][0] * self.screen_width, object_data["rel_pos"][1] * self.screen_height])

        for i in range(1,4):
            customer_data = self.data["customer"]
            customer_data["size"]["width"] = customer_data["size"]["scale"][0] * self.screen_width
            customer_data["size"]["height"] = customer_data["size"]["scale"][1] * self.screen_height
            customer_data["act_pos"][str(i)].extend([customer_data["rel_pos"][str(i)][0] * self.screen_width, customer_data["rel_pos"][str(i)][1] * self.screen_height]), 
    
        self.state = "START"

    def mainloop(self):
        
        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "GAME":
                self.gameloop()
        
    def startloop(self):

        bgm = pygame.mixer.Sound("assets/chefmusic.mp3")
        bgm.play(-1)
        bgm.set_volume(0.5)
        self.start_screen = pygame.image.load("assets/fp_images/start_screen.png")
        self.start_screen = pygame.transform.scale(self.start_screen, (self.screen_width, self.screen_height))
        self.screen.blit(self.start_screen, (0,0))
        pygame.display.flip()

        while self.state == "START":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "GAME"
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def gameloop(self):
        
        self.background = pygame.image.load("assets/fp_images/background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.screen.blit(self.background, (0,0))

        #creates a button for all of the ingredients and appliances and stores attributes in json file
        for object in self.objects:
            model = Button(self.data, object, self.screen)
            self.objects[f"{object}"] = model
        #creates models for customers
        for i in range(1, 4):
            customer = Customer(self.data, i)
            self.customers.append(customer)
            timer = Timer()
            self.timers.append(timer)

        #current recipe being made and orders being taken
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


            #test if any of the appliances are clicked and have the required amount of ingredients
            for app in self.data["appliances"]:
                if self.data["objects"][app].click() and len(self.data["objects"][app].rect.collidelistall([self.data["clone_image"][f"{app}food1"], self.data["clone_image"][f"{app}food2"]])) == self.data[app]["ing_num"]:
                    
                    recipe_data = self.data[app]["recipes"]
                    food_key = self.data[f"{app}_food"]
                    ing_num = self.data[app]["ing_num"]
                    #if recipe has 2 ingredients
                    if ing_num == 2:
                        #if recipe 1 is made
                        if recipe_data[food_key[-2]]["ing"][food_key[0]] and recipe_data[food_key[-2]]["ing"][food_key[1]]:
                            recipe = f"{food_key[-2]}"
                            recipe_data[food_key[-2]]["ing"][self.data[f"{app}_food"][1]] = 0
                        #if recipe 2 is made
                        elif recipe_data[self.data[f"{app}_food"][-1]]["ing"][food_key[2]] and recipe_data[food_key[-1]]["ing"][food_key[3]]:
                            recipe = f"{food_key[-1]}"
                            recipe_data[food_key[-1]]["ing"][food_key[2]] = 0
                            recipe_data[food_key[-1]]["ing"][food_key[3]] = 0
                    #if recipe has 1 ingredient
                    if ing_num == 1:
                        #if recipe 1 is made
                        if recipe_data[food_key[-2]]["ing"][food_key[0]]:
                            recipe = f"{food_key[-2]}"
                            recipe_data[food_key[-2]]["ing"][food_key[0]] = 0
                        #if recipe 2 is made
                        elif recipe_data[food_key[-1]]["ing"][food_key[1]]:
                            recipe = f"{food_key[-1]}"
                            recipe_data[food_key[-1]]["ing"][food_key[1]] = 0

                    #serves product
                    if self.data["objects"][app].available == "Full":
                        self.screen.blit(self.background, (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1]), (self.data[app]["act_pos"][0], self.data[app]["act_pos"][1], self.data[app]["size"]["width"], self.data[app]["size"]["height"]))
                        self.data["objects"][app].available = "Empty"
                        for i in range(1, 4):
                            if f"cooked_{recipe}{i}" in orders:
                                orders.remove(f"cooked_{recipe}{i}")
                                break
                        recipe = ""

                    #turns ingredients into product
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
                    cus.new_time()
                    cus.new_order()
                    cus.new_cus(surface)
                    self.screen.blit(surface, (0,0))
                    orders.append(f"{cus.order}{cus.num}")


                #after customer is served
                elif not(f"{cus.order}{cus.num}" in orders):
                    surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
                    surface.fill((0,0,0,0))
                    self.screen.blit(self.background, (cus.order_x, cus.y), (cus.order_x, cus.y, cus.order_w + self.data["customer"]["size"]["width"], self.data["customer"]["size"]["height"]))
                    self.timers[int(cus.num)-1].duration = cus.time_btwn_cus


                    if not(self.timers[int(cus.num)-1].active) and not(self.timers[int(cus.num)-1].activated):
                        self.timers[int(cus.num)-1].activate()


                    elif not(self.timers[int(cus.num)-1].active) and self.timers[int(cus.num)-1].activated:
                        print("works")
                        self.timers[int(cus.num)-1].activated = False
                        cus.served()
                    else:
                        self.timers[int(cus.num)-1].update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            pygame.display.flip()