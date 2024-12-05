import pygame

class Timer:

    def __init__(self):
        self.duration = 0
        self.start_time = 0
        self.current_time = 0
        self.active = False
        self.activated = False

    def activate(self):
        self.active = True
        self.activated = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        self.current_time = 0
        if self.active and self.activated:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.start_time >= self.duration:
                self.deactivate()
                print(self.active, self.activated)
                
    def str(self):
        return [self.duration, self.start_time, self.current_time, self.active]