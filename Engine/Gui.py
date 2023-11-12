import pygame
class Text:
    def __init__(self,display,font,size,text) -> None:
        self.font = pygame.font.Font(font,size)
        self.content = text
        self.color_text = (255,255,255)
        self.text = self.font.render(self.content,True,self.color_text)
        self.textRect = self.text.get_rect()
        self.display = display
        self.display.Graphics.append(self)

        self.canCollied = False

    def Destroy(self):
        self = None

    def Render(self):
        self.display._.blit(self.text,self.textRect)
    
    def Update(self):
        self.text = self.font.render(self.content,True,self.color_text)