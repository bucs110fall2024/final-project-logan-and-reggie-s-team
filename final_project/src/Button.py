import pygame

class Button():

    def __init__(self, x, y, scale, type, image, screen):
        
        self.image = pygame.image.load(image).convert_alpha()
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (scale[0], scale[1]))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = type
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
    
    def cook(self, topleft, scale, image, screen):
        self.clone_rect = self.image.get_rect()
        self.clone_rect.topleft = topleft
        self.clone_image = pygame.image.load(image)
        self.clone_image = pygame.transform.scale(self.clone_image, (scale[0], scale[1]))
        screen.blit(self.clone_image, (self.clone_rect.x, self.clone_rect.y))
