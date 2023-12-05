PUBLISH_MODULE_EFFECT = {
    "Module":"Effect",
    "Coder":["QuangDeNhi"],
    "Target":"Create Effect"
}

import pygame, random
from . import Vector
from .Human import IS_DIED,IS_LIVE


def MoveParticle(effect):
    direction =  effect.direction.getVec()
    effect.x += direction[0]
    effect.y += direction[1]
    effect.timeLife -= effect.KillSpeed
    effect.size -= effect.KillSpeed
    # Testing ...
    # particle[1][1] +=

class Particle:
    def __init__(self,x,y,direction:Vector.Vector2,timeLife,color) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.timeLife = timeLife
        self.size = self.timeLife
        self.color = color
        self.KillSpeed = 2 / 60 # 60 is fps

        self.move = MoveParticle

        self.alpha = 255

    def MakeSurface(self):
        radius = self.size * 2
        surface =  pygame.Surface((radius*2,radius*2)).convert_alpha()
        pygame.draw.circle(surface,self.color,(radius,radius),radius)
        surface.set_colorkey((0,0,0))
        surface.set_alpha(self.alpha)
        return surface

    def Update(self):
        self.move(self)

    def Draw(self,display):
        # pygame.draw.circle(display._,self.color,(self.x,self.y),self.size)
        surf = self.MakeSurface()
        display._.blit(surf,(self.x,self.y))
        if self.timeLife <= 0 or self.alpha <= 0:
            return IS_DIED
        return IS_LIVE



class ParticleGroup:
    def __init__(self,display,x,y,
        direction = Vector.Vector2(random.randint(0,20)/10-1,-4)) -> None:

        self.group = []
        self.x = x
        self.y = y
        
        self.direction = direction

        self.timeLife_perP = 10
        self.Enable = True
        self.color = (255,255,255)

        self.display = display
        self.display.Effects.append(self)

        self.updateAtt = None
        self.updateParticle = None

    def CreateNew(self):
        if self.notEnable(): return
        # self.group.append([[self.x,self.y],[self.move.getVec()],
        #               self.timeLife_perP, self.color] )
        particle = Particle(self.x,self.y,self.direction,self.timeLife_perP,self.color)
        if self.updateParticle:
            particle.move = self.updateParticle
        self.group.append(particle)

    def Update(self):
        if self.notEnable(): return
        if self.updateAtt:
            self.updateAtt()
        else:
            self.UpdateAttribute()
        self.CreateNew()
        for particle in self.group:
            particle.move(particle)

    def Render(self):
        if self.notEnable(): return
        for particle in self.group:
            status = particle.Draw(self.display)
            if status == IS_DIED:
                self.group.remove(particle)
    
    def UpdateAttribute(self):
        self.direction = Vector.Vector2(random.randint(0,20)/10-1,-4)
        self.timeLife_perP = random.randint(6,10)
        
    
    def notEnable(self):
        return self.Enable != True

    def Destroy(self):
        self = None