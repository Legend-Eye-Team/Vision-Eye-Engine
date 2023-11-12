import pygame
from . import Rectangle

class Image(Rectangle):
    def __init__(self, display, x, y,source) -> None:
        self.image = pygame.image.load(source).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        super().__init__(display, x, y,self.width,self.height)
        self.SetAttribute("IsImage",True)
    def Render(self):
        self.display._.blit(self.image,(self.x,self.y))
    
    def Transform(self,new_width,new_height):
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
        self.UpdateImage()
    
    def UpdateImage(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
