import pygame

class Button():

    def __init__(self, x, y, width, height, image, screen):
        
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.available = True
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
    
    def clone(self, topleft, width, height, image, screen):
        self.clone_rect = self.image.get_rect()
        self.clone_rect.topleft = topleft
        self.clone_image = pygame.image.load(image)
        self.clone_image = pygame.transform.scale(self.clone_image, (width, height))
        screen.blit(self.clone_image, (self.clone_rect.x, self.clone_rect.y))

    def cook(self, data, objects, app, screen):
        if objects[f"{app}1"].available:
            objects[f"{app}1"].clone(objects[f"{app}1"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data["beef"]["image"], screen)
            objects[f"{app}1"].available = False
        elif objects[f"{app}2"].available:
            objects[f"{app}2"].clone(objects[f"{app}2"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data["beef"]["image"], screen)
            objects[f"{app}2"].available = False
        elif objects[f"{app}3"].available:
            objects[f"{app}3"].clone(objects[f"{app}3"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data["beef"]["image"], screen)
            objects[f"{app}3"].available = False
        elif objects[f"{app}4"].available:
            objects[f"{app}4"].clone(objects[f"{app}4"].rect.topleft, data[f"{app}"]["size"]["width"], data[f"{app}"]["size"]["height"], data["beef"]["image"], screen)
            objects[f"{app}4"].available = False