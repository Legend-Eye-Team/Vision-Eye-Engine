## 0.0.1.4
## 0.0.1.3.8: Test for effect
V0014_CODE = """
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
f_MAIN()"""

## 0.0.1.3.1
# 0.0.1.3.1
from Engine import *

display = Display(1000,600,DISPLAY_CAPTION)

image = Image.Image(display,10,400,"testAsset\\test2.png")
image.Transform(100,100)
image.Lock = True
# image.angle = 20


image2 = Image.Image(display,10,100,"testAsset\\player.png")
image2.Transform(50,50)

player = Human.Human(image2)

floor = Rectangle(display,0,0,0,0)
floor.SetAttribute("IsFlat",True)

text = Gui.Text(display,"testAsset\\Font.ttf",20,"",10,10)

block = Circle(display,400,10,20)

testBlock = Polygone(display,100,200)
testBlock.Lock = True

def b():
    if display.EventControl.Keyboard.IsPress(pygame.K_d):
        player.MoveTo(HUMAN_DIRECTION_RIGHT)
    if display.EventControl.Keyboard.IsPress(pygame.K_a):
        player.MoveTo(HUMAN_DIRECTION_LEFT)
    if display.EventControl.Keyboard.IsPress(pygame.K_w):
        player.JumpActive()

def f_MAIN():
    while display.Enable:
        display.Input()
        display.Update()
        # Code
        text.content = str(round(display.Clock.get_fps()))
        b()
        display.FillDisplay(50,50,75)
        display.Render()
f_MAIN()

## 0.0.1.4.1
V00142_CODE = """
from Engine import *
import time, threading

display = Display(1000,600,DISPLAY_CAPTION)

image = Image.Image(display,10,450,".\\testAsset\\test2.png")
image.Transform(100,100)
image.Lock = True
image.canCollied = False

# image2 = Image.Image(display,800,600,".\\testAsset\\test.png")
# image2.Transform(25,25)

# player = Human.Human(image2)

# rect = image2
# rect.Lock = True
hp = 1000
floor = Rectangle(display,0,0,0,0)
floor.SetAttribute("IsFlat",True)

text = Gui.Text(display,"testAsset\\Font.ttf",20,"",10,10)

button = Gui.Button(display,"testAsset\\Font.ttf",20,"Hello Btn",100,100,130,50)

player = Image.Image(display,100,100,".\\testAsset\\player.png")
player.Transform(50,50)
player.Lock = True
player = Human.Human(player)

# vector = Math.getDirection(rect,image)

def updateBullet(graphic):
    global hp
    speed = 8
    vector = graphic.GetAttribute("Direction")
    graphic.setPoint(graphic.x + vector.x*speed,graphic.y + vector.y*speed)
    isTouch = image.isTouched(graphic,)
    if isTouch == True:
        hp -= 1
        print(hp)
        graphic.Destroy()


def a(a):
    # time.sleep(1)
    while display.Enable:
        # new = 
        pos = player.Rectangle.center
        new = Image.Image(display,pos[0],pos[1],".\\testAsset\\test.png")
        new.Transform(25,25)
        new.Lock = True
        new.updateFunc = updateBullet
        posMouse = display.EventControl.Mouse.GetPosition()
        newVector = Math.getDirection(new,Vector.Vector2(posMouse[0],posMouse[1]))
        new.SetAttribute("Direction",newVector)

        time.sleep(.1)

def move():
    speed = 2
    if display.EventControl.Keyboard.IsPress(pygame.K_d):
        player.Move2D(speed)
    if display.EventControl.Keyboard.IsPress(pygame.K_a):
        player.Move2D(-speed)
    if display.EventControl.Keyboard.IsPress(pygame.K_w):
        player.Move2D(0,-speed)
    if display.EventControl.Keyboard.IsPress(pygame.K_s):
        player.Move2D(0,speed)

def f_MAIN():
    global vector
    thread = threading.Thread(target=a,args=(1,))
    thread.start()
    # a(1)
    # button.initFunction(test)
    while display.Enable:
        display.Input()
        display.Update()
        # TODO: Code
        display.FillDisplay(20,20,20)
        text.content = str(round(display.Clock.get_fps()))
        move()

        display.Render()
f_MAIN()
"""