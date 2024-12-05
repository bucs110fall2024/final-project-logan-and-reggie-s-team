import pygame

class Button():

    def __init__(self, data, object, surface):
        
        #creates rectangle
        self.rect = pygame.Rect((data[object]["act_pos"][0], data[object]["act_pos"][1]),(data[object]["size"]["width"], data[object]["size"]["height"]))
        #clicked state
        self.clicked = False
        #availability of the object (for if a pan can be used or if the required ingredient is there)
        self.available = "Empty"
        #string for type of object
        self.type = f"{object}"
        #if an ingreident goes first or second
        self.order = data[object]["order"]

    def click(self):
        state = False
        pos = pygame.mouse.get_pos()
        #if mouse touches the rectangle returns true and clicked state is true so it cant be clicked unless mouse is released
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                state = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False
        #returns that the button has been clicked once
        return state
    
    def new_image(self, width, height, image, surface):
        #creates new rectangle and surface for an image then puts it on screen
        self.clone_rect = self.rect
        self.clone_image = pygame.image.load(image)
        self.clone_image = pygame.transform.scale(self.clone_image, (width, height))
        surface.blit(self.clone_image, (self.clone_rect.x, self.clone_rect.y))
        #returns rectangle of the clone
        return self.clone_rect
                
    def cook(self, data, food, app, surface):
        #the food will only create a copy if the required appliance is free or if it the required ingredient is already there
        if data["required"][food] == data["objects"][app].available:
            clone = data["objects"][app].new_image(data[app]["size"]["width"], data[app]["size"]["height"], data[food]["image"], surface)
            data["objects"][app].available = food
            #stores rectangle of the clone in json file
            data["clone_image"][f"{app}food{data[food]["order"]}"] = clone
        

        


