INFO_MODULE_IMAGE = {
    "Module":"Graphic-Image",
    "Coder":["QuangDeNhi"]
}

import pygame
from . import Rectangle

class Image(Rectangle):
    def __init__(self, display, x, y,source) -> None:
        self.image = pygame.image.load(source).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        super().__init__(display, x, y,self.width,self.height)
        self.SetAttribute("IsImage",True)

    def MakeSurface(self):
        surface = pygame.Surface((self.width,self.height)).convert_alpha()
        # pygame.draw.rect(surface,self.color,(0,0,self.width,self.height))
        pic = self.image.copy()
        surface.blit(pic,(0,0))
        pic = pygame.PixelArray(pic)
        # self.image = pygame.PixelArray(self.image)
        surface.set_colorkey((0,0,0))
        surface.set_alpha(self.alpha)
        return surface

    def Render(self):
        rect = self.MakeSurface()
        self.display._.blit(rect,(self.x,self.y))
        rect = pygame.PixelArray(rect)
    
    def Transform(self,new_width:int,new_height:int):
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
        self.UpdateImage()
    
    def UpdateImage(self):
        self.width = self.image.get_width()
        self.height = self.image.get_height()
