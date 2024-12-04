import pygame

class Button():

    def __init__(self, data, object, num, screen):
        
        self.image = pygame.image.load(data[object]["image"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (data[object]["size"]["width"], data[object]["size"]["height"]))
        self.rect = self.image.get_rect()
        self.rect.topleft = (data[object]["pos"][f"{num+1}"][0], data[object]["pos"][f"{num+1}"][1])
        self.clicked = False
        self.available = "None"
        self.type = f"{object}"
        self.order = data[object]["order"]
        screen.blit(self.image, (self.rect.x, self.rect.y))

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
    
    def new_image(self, topleft, width, height, image, surface):
        self.clone_rect = self.image.get_rect()
        self.clone_rect.topleft = topleft
        self.clone_image = pygame.image.load(image)
        self.clone_image = pygame.transform.scale(self.clone_image, (width, height))
        surface.blit(self.clone_image, (self.clone_rect.x, self.clone_rect.y))

        return {"rect" : self.clone_rect}
                

    def cook(self, data, objects, food, app, surface):
        if objects[f"{app}1"].available == data["required"][food]:
            clone = objects[f"{app}1"].new_image(objects[f"{app}1"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], surface)
            objects[f"{app}1"].available = f"{food}"
            data["clone_image"][f"{app}1food{data[food]["order"]}"] = clone

        elif objects[f"{app}2"].available == data["required"][food]:
            clone = objects[f"{app}2"].new_image(objects[f"{app}2"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], surface)
            objects[f"{app}2"].available = f"{food}"
            data["clone_image"][f"{app}2food{data[food]["order"]}"] = clone

        elif objects[f"{app}3"].available == data["required"][food]:
            clone = objects[f"{app}3"].new_image(objects[f"{app}3"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], surface)
            objects[f"{app}3"].available = f"{food}"
            data["clone_image"][f"{app}3food{data[food]["order"]}"] = clone

        elif objects[f"{app}4"].available == data["required"][food]:
            clone = objects[f"{app}4"].new_image(objects[f"{app}4"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], surface)
            objects[f"{app}4"].available = f"{food}"
            data["clone_image"][f"{app}4food{data[food]["order"]}"] = clone
        
    def plate(self, data, app, surface):
        surface.set_alpha(0)
        

        


