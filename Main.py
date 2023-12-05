## 0.0.1.4
## 0.0.1.3.8: Test for effect

from Engine import *
import random
display = Display(1000,600,DISPLAY_CAPTION)

flame = Effect.ParticleGroup(display,500,300)

def flameCreate():
    flame.x = 500
    flame.y = 300

    flame.direction = Vector.Vector2(
        random.randint(0,20)/10-1, # move right or left
        -3)                        # for move up

    flame.color = random.choice(('red','orange','yellow'))
    flame.timeLife_perP = random.randint(4,8)
def flameEff(effect):
    direction =  effect.direction.getVec()
    effect.x += direction[0]
    effect.y += direction[1]
    effect.timeLife -= effect.KillSpeed
    effect.size -= effect.KillSpeed
    effect.alpha -= 6

flame.updateParticle = flameEff
flame.updateAtt = flameCreate

fountain = Effect.ParticleGroup(display,300,300)

def fountainCreate():
    fountain.direction = Vector.Vector2(
        random.randint(0,20)/10-1,-6)

    fountain.color = random.choice(('blue','cyan'))
    fountain.timeLife_perP = random.randint(3,6)
fountain.updateAtt = fountainCreate

def fountainEff(effect):
    direction =  effect.direction.getVec()
    effect.x += direction[0]
    effect.y += direction[1]
    effect.timeLife -= effect.KillSpeed
    effect.size -= effect.KillSpeed
    effect.direction.y += 0.2
    if effect.y >= 350:
        effect.timeLife = 0
fountain.updateParticle = fountainEff

def f_MAIN():
    while display.Enable:
        display.Input()
        display.Update()
        # Code
        display.FillDisplay(0,0,23)
        display.Render()
f_MAIN()

## 0.0.1.3.1
V00131_CODE = """
from Engine import *
import time, threading

display = Display(1000,600,DISPLAY_CAPTION)

image = Image.Image(display,10,500,".\\testAsset\\test2.png")
image.Transform(100,100)
image.Lock = True

image2 = Image.Image(display,10,100,".\\testAsset\\test.png")
image2.Transform(50,50)

player = Human.Human(image2)

floor = Rectangle(display,0,0,0,0)
floor.SetAttribute("IsFlat",True)

text = Gui.Text(display,"testAsset\\Font.ttf",20,"",10,10)

button = Gui.Button(display,"testAsset\\Font.ttf",20,"Hello Btn",100,100,130,50)

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
"""