import pygame

class Button():

    def __init__(self, data, object, surface):
        
        self.rect = pygame.Rect((data[object]["act_pos"][0], data[object]["act_pos"][1]),(data[object]["size"]["width"], data[object]["size"]["height"]))
        self.clicked = False
        self.available = "None"
        self.type = f"{object}"
        self.order = data[object]["order"]
  
    def click(self):
        state = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                state = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False
        return state
    
    
    def new_image(self, width, height, image, surface):
        self.clone_rect = self.rect
        self.clone_image = pygame.image.load(image).convert_alpha()
        self.clone_image = pygame.transform.scale(self.clone_image, (width, height))
        surface.blit(self.clone_image, (self.clone_rect.x, self.clone_rect.y))

        return self.clone_rect
                
    def cook(self, data, food, app, surface):

        if data["objects"][app].available == data["required"][food]:
            clone = data["objects"][app].new_image(data[app]["size"]["width"], data[app]["size"]["height"], data[food]["image"], surface)
            data["objects"][app].available = food
            data["clone_image"][f"{app}food{data[food]["order"]}"] = clone

    def plate(self, data, app, surface):
        surface.set_alpha(0)
        

        


