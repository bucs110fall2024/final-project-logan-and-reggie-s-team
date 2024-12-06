import pygame

class Button():
    def __init__(self, data, object):
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
        
    """
    This method determines whether or not a user left-clicked within a rectangular space.
    args: None
    return: state [bool] This returns a True or False bool that states whether or not a user clicked and released a within a defined rectangular space. (True for Clicked, False if not)
    """
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
    
    """
    This method takes an image, and loads the image to a given width and height that is related to a specific rectangle.
    args: width [int]: Takes the width to scale the image to
    height [int]: Takes the height to scale the image to
    image [str]: The file path of the image that will be loaded in
    surface [obj] Takes the pygame surface the image will be loaded into
    return: self.clone_rect [obj] Returns the rectangle of the cloned image
    """
    def new_image(self, width, height, image, surface):
        #creates new rectangle and surface for an image then puts it on screen
        self.clone_rect = self.rect
        self.clone_image = pygame.image.load(image)
        self.clone_image = pygame.transform.scale(self.clone_image, (width, height))
        surface.blit(self.clone_image, (self.clone_rect.x, self.clone_rect.y))
        #returns rectangle of the clone
        return self.clone_rect
    
    """
    This method creates a copy of food in the correct corresponding appliance.
    args: data [dict]: where data is from
    food [str]: Goes withi type of food it is
    app [str]: which appliance is used
    surface [obj]: which surface the image is being drawn on
    """            
    def cook(self, data, food, app, surface):
        #the food will only create a copy if the required appliance is free or if it the required ingredient is already there
        if data["required"][food] == data["objects"][app].available:
            clone = data["objects"][app].new_image(data[app]["size"]["width"], data[app]["size"]["height"], data[food]["image"], surface)
            data["objects"][app].available = food
            #stores rectangle of the clone in json file
            data["clone_image"][f"{app}food{data[food]["order"]}"] = clone
        

        


