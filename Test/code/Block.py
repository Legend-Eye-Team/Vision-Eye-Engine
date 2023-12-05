# 0.0.1.3.1
from Engine import *

display = Display(1000,600,DISPLAY_CAPTION)

image = Image.Image(display,10,500,"image")
image.Transform(100,100)
image.Lock = True

image2 = Image.Image(display,10,100,"image")
image2.Transform(50,50)

player = Human.Human(image2)

floor = Rectangle(display,0,0,0,0)
floor.SetAttribute("IsFlat",True)

text = Gui.Text(display,"font",20,"",10,10)

button = Gui.Button(display,"font",20,"Hello Btn",100,100,130,50)

def test():
    player.JumpActive()

def b():
    if display.EventControl.Keyboard.IsPress(pygame.K_d):
        player.MoveTo(HUMAN_DIRECTION_RIGHT)
    if display.EventControl.Keyboard.IsPress(pygame.K_a):
        player.MoveTo(HUMAN_DIRECTION_LEFT)
    if display.EventControl.Keyboard.IsPress(pygame.K_w):
        player.JumpActive()

def f_MAIN():
    button.initFunction(test)
    while display.Enable:
        display.Input()
        display.Update()
        # Code
        text.content = str(round(display.Clock.get_fps()))
        b()
        display.FillDisplay(20,20,20)
        display.Render()
f_MAIN()