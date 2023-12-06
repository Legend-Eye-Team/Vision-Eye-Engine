import math
from .Graphic import Graphic

def getDistance(graphic1:Graphic,  graphic2:Graphic):
    dx =  graphic2.x+ graphic2.width /2 - graphic1.x
    dy =  graphic2.y+ graphic2.height/2 - graphic1.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance