PUBLISH_MODULE_DISPLAY = {
    "Module":"Display",
    "Coder":["QuangDeNhi"],
    "Target":"Init and Control Game"
}

import pygame
from. import Setting
from. import Event

class Display:
    pygame.init()
    def __init__(self,width,height,caption) -> None:
        self._ = pygame.display.set_mode((width,height))
        pygame.display.set_caption(caption)
        self.width = width
        self.height = height
        self.caption = caption

        self.Enable = True

        self.Clock = pygame.time.Clock()

        self.Graphics = []
        self.Effects = []
        self.EventControl = Event.Event_Controller()

        self.setting = Setting.Setting()

    
    def FillDisplay(self,r:int,g:int,b:int):
        self._.fill((r,g,b))

    def Input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Exit()
        self.EventControl.Update()
    
    def Render(self):
        if self.Enable == False: pygame.quit();return
        for graphic in self.Graphics:
            graphic.Render()
        for effect in self.Effects:
            effect.Render()
        pygame.display.update()

    def Exit(self):
        self.Enable = False

    def Update(self):
        self.Clock.tick(self.setting.fps)
        for graphic in self.Graphics:
            graphic.Update()
        for effect in self.Effects:
            effect.Update()