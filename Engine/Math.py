import math
from .Graphic import Graphic

def getDistance(rect1:Graphic, rect2:Graphic):
    dx = rect2.x+rect2.width /2 - rect1.x
    dy = rect2.y+rect2.height/2 - rect1.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance