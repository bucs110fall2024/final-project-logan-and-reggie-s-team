import pygame
import random

class Customer():
    def __init__(self, data, customer_num):
        self.num = f"{customer_num}"
        self.x = data["customer"]["act_pos"][self.num][0]
        self.y = data["customer"]["act_pos"][self.num][1]
        self.order_x = self.x - data["customer"]["size"]["width"]/4
        self.order_y = self.y + data["customer"]["size"]["height"]/3
        self.order_w = data["customer"]["size"]["width"]/3
        self.order_h = data["customer"]["size"]["width"]/3
        self.rect = pygame.Rect(self.x, self.y, data["customer"]["size"]["width"], data["customer"]["size"]["height"])
        self.waiting = True
        self.time_btwn_cus = 0
        self.customer_list = data["customer"]["image"]
        self.order = ""
        self.order_list = data["order_list"]
        
    """
    This method chooses a random order from a valid list of potential orders.
    args: None
    return: None
    """
    def new_order(self):
        self.order = self.order_list[random.randint(0, len(self.order_list)-1)]
    
    """
    This method displays a random customer and their associated order on the screen.
    args: screen [obj]: Takes the pygame surface the image will be loaded into
    return: None
    """    
    def new_cus(self, screen):
        self.waiting = False
        #customer
        self.display(self.customer_list[random.randint(0, len(self.customer_list)-1)], screen, self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        #order
        self.display(self.order, screen, self.order_x, self.order_y, self.order_w, self.order_h)

    """
    This method generates a random time (within a certain interval) in which customers arrive
    args: None
    return: None
    """
    def new_time(self):
        self.time_btwn_cus = random.randint(1500, 3500)

    """
    This method, sizes, and displays an image on a surface at the given position.
    args: image [str]: The file path of the image that will be loaded in
    surface [obj]: Takes the pygame surface the image will be loaded into
    x [int]: Takes the x-position the image will be loaded on
    y [int]: Takes the y-position the image will be loaded on
    w [int]: Takes the width the image will be sized to
    h [int]: Takes the height the image will be sized to
    """
    def display(self, image, surface, x, y, w ,h):
        self.image = pygame.image.load(f"assets/fp_images/{image}.png")
        self.image = pygame.transform.scale(self.image, (w, h))
        self.image_rect = pygame.Surface.get_rect(self.image)
        surface.blit(self.image, (x, y))

    """
    This method updates the Customer served status as True and is no langer waiting for an order.
    args: None
    return: None
    """
    def served(self):
        self.waiting = True 
   
        