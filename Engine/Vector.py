PUBLISH_MODULE_VECTOR = {
    "Module":"Vector",
    "Coder":["QuangDeNhi"],
    "Target":"Create Datatype"
}

class Vector2:
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y
    
    def getVec(self):
        return (self.x,self.y)