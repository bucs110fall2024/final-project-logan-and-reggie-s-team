import pygame

class Timer:

    def __init__(self):
        self.duration = 0
        self.start_time = 0
        self.current_time = 0
        self.active = False
        self.activated = False

    """
    This method starts the timer and gets the tick at which it was started
    args: None
    return: None
    """
    def activate(self):
        self.active = True
        self.activated = True
        self.start_time = pygame.time.get_ticks()
        
    """
    This method stops the timer and resets the start time
    args: None
    return: None
    """
    def deactivate(self):
        self.active = False
        self.start_time = 0

    """
    This method compares current to start time and deactivates the timer if the duration has passed
    args: None
    return: None
    """
    def update(self):
        self.current_time = 0
        if self.active and self.activated:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.start_time >= self.duration:
                self.deactivate()
                print(self.active, self.activated)