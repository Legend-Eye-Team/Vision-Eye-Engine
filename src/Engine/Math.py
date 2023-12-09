import math
from .Graphic import Graphic
from .Vector import Vector2

def getDistance(graphic1:Graphic,  graphic2:Graphic|Vector2):
    distance = 0
    if type(graphic2) == Vector2:
        dx =  graphic2.x - graphic1.x
        dy =  graphic2.y - graphic1.y
        distance = math.sqrt(dx**2 + dy**2)
    else:
        dx =  graphic2.center[0] - graphic1.x
        dy =  graphic2.center[1] - graphic1.y
        distance = math.sqrt(dx**2 + dy**2)
    return distance

def getDirection(graphic1:Graphic,  graphic2:Graphic|Vector2):
    norm = getDistance(graphic1,graphic2)

    if type(graphic2) == Graphic:
        vec = Vector2(graphic2.center[0] - graphic1.center[0], graphic2.center[1] - graphic1.center[1])
        direction = Vector2(vec.x / (norm+0.1),vec.y / (norm+0.1))
        return direction 
    elif type(graphic2) == Vector2:
        vec = Vector2(graphic2.x - graphic1.center[0], graphic2.y - graphic1.center[1])
        direction = Vector2(vec.x / (norm+0.1),vec.y / (norm+0.1))
        return direction 