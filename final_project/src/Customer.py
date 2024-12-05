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

    def new_order(self):
        self.order = self.order_list[random.randint(0, len(self.order_list)-1)]
        
    def new_cus(self, screen):
        self.waiting = False
        #customer
        self.display(self.customer_list[random.randint(0, len(self.customer_list)-1)], screen, self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        #order
        self.display(self.order, screen, self.order_x, self.order_y, self.order_w, self.order_h)

    def new_time(self):
        self.time_btwn_cus = random.randint(1500, 3500)

    def display(self, image, surface, x, y, w ,h):
        self.image = pygame.image.load(f"assets/fp_images/{image}.png")
        self.image = pygame.transform.scale(self.image, (w, h))
        self.image_rect = pygame.Surface.get_rect(self.image)
        surface.blit(self.image, (x, y))

    def served(self):
        self.waiting = True 
   
        