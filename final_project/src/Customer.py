import pygame

class Customer():
    def __init__(self, x, y, customerimg, orderimg):
        self.x = x
        self.y = y
        self.image = pygame.image.load(customerimg)
        self.order_image = pygame.image.load(orderimg)
        self.order_state = "waiting"
    def neworder(self, screen):
        order_x = self.x + (self.image.get_width() - self.order_image.get_width()) // 2  
        order_y = self.y - self.order_image.get_height() - 10  
        screen.blit(self.order_image, (order_x, order_y))
    def serve_order(self):
        self.order_state = "served"  
    def is_served(self):
        return self.order_state == "served"
        