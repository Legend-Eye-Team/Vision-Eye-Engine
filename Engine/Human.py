INFO_MODULE_HUMAN = {
    "Module":"Human",
    "Coder":["QuangDeNhi"]
}

from . import Functional
# from . import Rectangle
import threading,time

TOP_COLLIED = 501
BOTTOM_COLLIED = 502
LEFT_COLLIED = 503
RIGHT_COLLIED = 504
NONE_COLLIED = 500

class Human:
    def __init__(self,Rectangle) -> None:
        self.Rectangle = Rectangle
        self.Health = 100
        self.Max_health = 100

        self.Jump_power = 120
        self._CanJump = True
        self._countdownJump = .7

        self.walkSpeed = 2

    def MoveTo(self,dir_=1):
        will_x = self.Rectangle.x 
        speed = self.walkSpeed * dir_
        will_x += self.walkSpeed
        
        for graphic in self.Rectangle.display.Graphics:
            a = self.Rectangle.GetCollied(graphic,abs(self.walkSpeed))
            if a == None: continue
            elif a[0] == LEFT_COLLIED and self.walkSpeed > 0:
                if graphic.Lock == True: return
                elif graphic.Lock == False:
                    graphic.x += self.walkSpeed / 2
                    will_x = self.walkSpeed / 2
                    return

            elif a[0] == RIGHT_COLLIED and self.walkSpeed < 0:
                if graphic.Lock == True: return
                elif graphic.Lock == False:
                    graphic.x += self.walkSpeed / 2
                    will_x = self.walkSpeed / 2
                    return

        
        self.Rectangle.x = will_x


    def _Jump(self,_):
        self._CanJump = False
        self.Rectangle.Lock= True
        for i in  range(0,5):
            self.Rectangle.y -= self.Jump_power / 5
            time.sleep(.02)
        self.Rectangle.Lock= False

    def JumpActive(self):
        if self._CanJump == True:
            f =threading.Thread(target=self._Jump,args=(1,))
            f.start()
            def convert(): self._CanJump = True
            Functional.WaitThread(self._countdownJump,convert)

    def TakeHealth(self,damage):
        self.Health -= damage