PUBLISH_MODULE_EVENT = {
    "Module":"Event",
    "Coder":["QuangDeNhi"],
    "Target":"Listen to Event"
}

import pygame

class Event_Controller:
    def __init__(self) -> None:
        self.Mouse = Mouse()
        self.Keyboard = Keyboard()
    
    def Update(self):
        self.Mouse.Update()
        self.Keyboard.Update()

class Mouse:
    def __init__(self) -> None:
        self.x = self.y = 0
        self.IsClick = []

    def Update(self):
        self.x,self.y = pygame.mouse.get_pos()
        self.IsClick = pygame.mouse.get_pressed()
    
    def LeftClick(self):
        return self.IsClick[0]
    
    def MidClick(self):
        return self.IsClick[1]
    
    def RightClick(self):
        return self.IsClick[2]

class Keyboard:
    def __init__(self) -> None:
        self.key_pressing = []

    def Update(self):
        self.key_pressing = pygame.key.get_pressed()

    def IsPress(self,key):
        return self.key_pressing[key]