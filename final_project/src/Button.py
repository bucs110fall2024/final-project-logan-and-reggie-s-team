import pygame

class Button():

    def __init__(self, x, y, width, height, image, screen):
        
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.available = "None"
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def draw(self, screen):
        state = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                state = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False
        return state
    
    def new_image(self, topleft, width, height, image, screen):
        self.clone_rect = self.image.get_rect()
        self.clone_rect.topleft = topleft
        self.clone_image = pygame.image.load(image)
        self.clone_image = pygame.transform.scale(self.clone_image, (width, height))
        screen.blit(self.clone_image, (self.clone_rect.x, self.clone_rect.y))

    def cook(self, data, objects, food, app, screen):
        if objects[f"{app}1"].available == data["required"][food]:
            objects[f"{app}1"].new_image(objects[f"{app}1"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], screen)
            objects[f"{app}1"].available = f"{food}"
        elif objects[f"{app}2"].available == data["required"][food]:
            objects[f"{app}2"].new_image(objects[f"{app}2"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], screen)
            objects[f"{app}2"].available = f"{food}"
        elif objects[f"{app}3"].available == data["required"][food]:
            objects[f"{app}3"].new_image(objects[f"{app}3"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], screen)
            objects[f"{app}3"].available = f"{food}"
        elif objects[f"{app}4"].available == data["required"][food]:
            objects[f"{app}4"].new_image(objects[f"{app}4"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data[food]["image"], screen)
            objects[f"{app}4"].available = f"{food}"
        
    def plate(self, data, objects, screen):
        pass