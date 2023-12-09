PUBLISH_MODULE_GRAPHIC = {
    "Module":"Graphic",
    "Coder":["QuangDeNhi"],
    "Target":"Create Graphic Object"
}

import pygame
from . import Human
from .Functional import CreateID

TOP_COLLIED = 501
BOTTOM_COLLIED = 502
LEFT_COLLIED = 503
RIGHT_COLLIED = 504
NONE_COLLIED = 500

SETTING_ARG_GRAPHIC = 101

def NoneFunction(graphic):
    return

class Graphic:
    def __init__(self,display,x,y) -> None:
        self.id = CreateID()
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.center = (self.x,self.y)
        self.alpha = 255
        self.display = display
        self.display.Graphics.append(self)

        self.Lock = False
        self.canCollied = True

        self.updateFunc = NoneFunction

    def Destroy(self):
        try:
            self.display.Graphics.remove(self)
        except ValueError:
            pass
        #  self = None
    
    def setPoint(self,x,y):
        self.x = x
        self.y = y
    
    def getId(self):
        return self.id

    def Update(self):
        self.center = (self.x+self.width/2,self. y+self.height/2)
        self.updateFunc(self)

class Rectangle(Graphic):
    def __init__(self, display, x, y,width,height) -> None:
        super().__init__(display, x, y)
        self.width = width
        self.height = height
        self.color = (200,200,200)
        self.Attribute = {
            "IsFlat":False,
            "IsImage":False
        }
        self.setting = self.display.setting

    def SetAttribute(self, name:str, value):
        self.Attribute[name] = value
        self.UpdateOnce()

    def GetAttribute(self, name:str):
        return self.Attribute[name]

    def Transform(self,new_width:int,new_height:int):
        self.width = new_width
        self.height = new_height

    def GetCollied(self,graphic:Graphic,max_speed:int):
        if graphic.canCollied == True:

            local_rect = pygame.Rect(self.x,self.y,self.width,self.height)
            other_rect = pygame.Rect(graphic.x,graphic.y,graphic.width,graphic.height)

            if local_rect.colliderect(other_rect):
                if abs(other_rect.top - local_rect.bottom) < max_speed*2 :
                    return (TOP_COLLIED,other_rect.top)
                if abs(other_rect.bottom - local_rect.top) < max_speed*2 :
                    return (BOTTOM_COLLIED, other_rect.top)
                if abs(other_rect.right - local_rect.left) < max_speed*2 :
                    return (RIGHT_COLLIED, other_rect.left)
                if abs(other_rect.left - local_rect.right) < max_speed*2 :
                    return (LEFT_COLLIED, other_rect.right)
            return (NONE_COLLIED,None)

    def isTouched(self,human):
        rect = human
        
        local_rect = pygame.Rect(self.x,self.y,self.width,self.height)
        # print(local_rect.collidepoint(rect.center))
        if local_rect.collidepoint(rect.center)              or \
            local_rect.collidepoint(rect.x,rect.y+rect.height) or \
            local_rect.collidepoint(rect.x+rect.width,rect.y ):
            return True
        else:
            return False

    def GravityUpdate(self):
        if self.Lock == False:
            self.y += self.setting.gravity

    def Update(self):
        self.GravityUpdate()
        for graphic in self.display.Graphics:
            if self.Lock == False:
                a = self.GetCollied(graphic,self.display.setting.gravity)
                if a == None: continue
                if a[0] == TOP_COLLIED:
                    self.y = a[1] - self.height
        return super().Update()

    def UpdateOnce(self):
        if self.Attribute["IsFlat"] == True:
            self.Transform(self.display._.get_width(),100)
            self.x = 0
            self.y = self.display._.get_height()
            self.Lock = True

    def MakeSurface(self):
        surface = pygame.Surface((self.width,self.height)).convert_alpha()
        pygame.draw.rect(surface,self.color,(0,0,self.width,self.height))
        surface.set_colorkey((0,0,0))
        surface.set_alpha(self.alpha)
        return surface

    def Render(self):
        # local_rect = pygame.Rect(self.x,self.y,self.width,self.height)
        # pygame.draw.rect(self.display._,self.color,local_rect)
        rect = self.MakeSurface()
        self.display._.blit(rect,(self.x,self.y))