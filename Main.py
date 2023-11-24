from Engine import *
import time, threading

display = Display(1000,600,DISPLAY_CAPTION)

image = Image.Image(display,10,500,".\\test2.png")
image.Transform(100,100)
image.Lock = True

image2 = Image.Image(display,10,100,".\\test.png")
image2.Transform(50,50)

player = Human.Human(image2)

floor = Rectangle(display,0,0,0,0)
floor.SetAttribute("IsFlat",True)

text = Gui.Text(display,"Font.ttf",20,"",10,10)

button = Gui.Button(display,"Font.ttf",20,"Hello Btn",100,100,130,50)

# def a(a):
#     i = 0
#     while i < 50 and display.Enable:
#         print(i, end="\r")
#         image2.MoveTo(5)
#         time.sleep(0.1)
#         i += 1

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
    # thread = threading.Thread(target=a,args=(1,))
    # thread.start()
    button.initFunction(test)
    while display.Enable:
        display.Input()
        display.Update()
        # TODO: Code
        text.content = str(round(display.Clock.get_fps()))
        b()
        display.FillDisplay(20,20,20)
        display.Render()
f_MAIN()