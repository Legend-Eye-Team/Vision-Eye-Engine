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
IS_LIVE = 510
IS_DIED = 511

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
        will_x += speed
        
        for graphic in self.Rectangle.display.Graphics:
            a = self.Rectangle.GetCollied(graphic,abs(self.walkSpeed))
            if a == None: continue
            elif a[0] == LEFT_COLLIED and speed> 0:
                if graphic.Lock == True: return
                elif graphic.Lock == False:
                    graphic.x += speed
                    will_x = speed
                    return

            elif a[0] == RIGHT_COLLIED and speed < 0:
                if graphic.Lock == True: return
                elif graphic.Lock == False:
                    graphic.x += speed
                    will_x = speed
                    return

        
        self.Rectangle.x = will_x
    
    def Move2D(self,dir_x=0,dir_y=0):
        will_x = self.Rectangle.x 
        speed = self.walkSpeed * dir_x
        will_x += speed

        will_y = self.Rectangle.y
        speed2 = self.walkSpeed * dir_y
        will_y += speed2
        
        for graphic in self.Rectangle.display.Graphics:
            a = self.Rectangle.GetCollied(graphic,abs(self.walkSpeed))
            if a == None: continue
            elif a[0] == LEFT_COLLIED and speed> 0 or \
                a[0] == RIGHT_COLLIED and speed < 0:
                if graphic.Lock == True: return
                elif graphic.Lock == False:
                    graphic.x += speed
                    will_x = speed
                    return

            elif a[0] == TOP_COLLIED and speed < 0 or \
                a[0] == BOTTOM_COLLIED and speed < 0:
                if graphic.Lock == True: return
                elif graphic.Lock == False:
                    graphic.y += speed
                    will_y = speed
                    return

        self.Rectangle.x = will_x
        self.Rectangle.y = will_y

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