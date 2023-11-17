PUBLISH_MODULE_GUI = {
    "Module":"Gui",
    "Coder":["QuangDeNhi"],
    "Target":"Create Gui for Client"
}

import pygame

class Text:
    def __init__(self,display,font,size,text,x,y) -> None:
        self.font = pygame.font.Font(font,size)
        self.content = text
        self.color_text = (255,255,255)
        self.label = self.font.render(self.content,True,self.color_text)
        self.textRect = self.label.get_rect()
        self.display = display
        self.display.Graphics.append(self)
        self.x = x
        self.y = y
        self.size = size

        self.canCollied = False

    def Destroy(self):
        self = None

    def Render(self):
        self.display._.blit(self.label,(self.x,self.y))
    
    def Update(self):
        self.label = self.font.render(self.content,True,self.color_text)

class Button(Text):
    def __init__(self, display, font, size_text, text,x,y,width,height) -> None:
        super().__init__(display,font,size_text,text,x,y)
        self.color_background = (255,255,255)
        self.color_text = (0,0,0)
        self.width = width
        self.height = height
        self.isPressing = None

    def Render(self):
        pygame.draw.rect(self.display._,self.color_background,(self.x-self.size/2,self.y-self.size/2,self.width,self.height))
        return super().Render()

    def Update(self):
        self.isPressing = self.IsPressOnce()
        return super().Update()

    def IsPressOnce(self):
        mouse_data = self.display.EventControl.Mouse

        if mouse_data.LeftClick():
            x,y = mouse_data.GetPosition()
            rect = pygame.Rect(self.x,self.y,self.width,self.height)
            if rect.collidepoint(x,y):
                if self.isPressing == True:
                    return True
                print("pressed")

                return True
            return False
        return False