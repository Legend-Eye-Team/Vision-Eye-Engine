import pygame

TOP_COLLIED = 501
BOTTOM_COLLIED = 502
LEFT_COLLIED = 503
RIGHT_COLLIED = 504
NONE_COLLIED = 500


start_id = 0
def CreateID():
    global start_id
    start_id += 1
    return start_id - 1

class Graphic:
    def __init__(self,display,x,y) -> None:
        self.id = CreateID()
        self.x = x
        self.y = y
        self.display = display
        self.display.Graphics.append(self)

        self.Lock = False
        self.canCollied = True

    def Destroy(self):
        self = None

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

    def SetAttribute(self, name, value):
        self.Attribute[name] = value
        self.UpdateOnce()

    def Transform(self,new_width,new_height):
        self.width = new_width
        self.height = new_height

    def GetCollied(self,graphic,max_speed):
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

    def UpdateOnce(self):
        if self.Attribute["IsFlat"] == True:
            self.Transform(self.display._.get_width(),100)
            self.x = 0
            self.y = self.display._.get_height()
            self.Lock = True

    def Render(self):
        local_rect = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(self.display._,self.color,local_rect)
    
    