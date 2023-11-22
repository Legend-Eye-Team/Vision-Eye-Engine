# Import
from Engine import *
import pygame
import random
import threading, time

# Initial
display = Display(1000,600,DISPLAY_CAPTION)

player = Human.Human(Rectangle(display,100,450,50,50))
player._countdownJump = .7
player.Jump_power = 150
player.Rectangle.color = (0, 153, 255)


lava_floor = Rectangle(display,0,550,1000,50)
lava_floor.Lock = True
lava_floor.color = (255, 12, 37)
lava_floor.canCollied = False


Rect1 = Rectangle(display, 75,500,75,100)
Rect1.Lock = True
Rect1 = Rectangle(display, 275,500,75,100)
Rect1.Lock = True
Rect1 = Rectangle(display, 475,500,75,100)
Rect1.Lock = True
Rect1 = Rectangle(display, 675,500,75,100)
Rect1.Lock = True
Rect1 = Rectangle(display, 875,500,75,100)
Rect1.Lock = True


fps_text = Gui.Text(display,"asset/Font.ttf",20,"",10,10)
point_text = Gui.Text(display,"asset/Font.ttf",20,"",10,50)

point = 0

display.setting.gravity = 3
speed = 2
speed2 = 2

upperPost = 0
isWin = False
# Functional

def Move():

    if display.EventControl.Keyboard.IsPress(pygame.K_w):
        player.JumpActive()

def Reset(damage):
    global point,speed,speed2
    if damage.isTouched(player) == True:
        player.Rectangle.x = 100
        player.Rectangle.y= 450
        point = 0
        speed  = 2
        speed2 = 2

def addPost():
    points = [500,450,400,]
    a = random.randint(0,len(points)-1)
    y=points[a] - upperPost
    new_post = Rectangle(display,1000,y,75,50)
    new_post.Lock = True
    if isWin == True:
        new_post.color = (255,215,0)

def boss():
    global speed,speed2,upperPost,point,isWin    
    speed = 2
    speed2 = 1.9
    boss = Rectangle(display,900,100,200,400)
    boss.Lock = True
    boss.color = (97,56,60)
    boss.id = -2
    point = 0
    upperPost = 20
    while point <= 200 and display.Enable:
        skill = random.randint(0,1)
        if skill == 0:
            print("upper!")
            for graphic in display.Graphics:
                if graphic.id == player.Rectangle.id or graphic.id == lava_floor.id or graphic.id == -1 or graphic.id == -2:
                    continue
                else:
                    graphic.y -= 10
            time.sleep(10)
        elif skill == 1:
            print("Smoke!")
            smoke = Rectangle(display,0,player.Rectangle.y-350,1200,450)
            smoke.Lock = True
            time.sleep(5)

    for i in range(0,100):
        boss.y += 1
        boss.x += 1
        time.sleep(0.01)
    boss.Destroy()
    road = Rectangle(display,1000,500,5000,400)
    road.Lock = True
    isWin = True
    print("winner")
    time.sleep(8)
    road.id = -2
    text = Gui.Text(display,"asset/Font.ttf",50,"Victory!",400,300)

def updatePost():
    global speed, speed2
    for graphic in display.Graphics:
        if graphic.id == player.Rectangle.id or graphic.id == lava_floor.id or graphic.id == -1 or graphic.id == -2:
            continue
        else:
            graphic.x -= speed
            speed  *= 1.000005
            speed2 /= 1.000005
            if graphic.x <= -10:
                graphic.Destroy()

def updatePoint():
    global point
    while display.Enable:
        point += 2
        addPost()
        time.sleep(speed2)


# Main
def f_MAIN():
    thread = threading.Thread(target=updatePoint)
    thread.start()
    thread2 = threading.Thread(target=boss)
    boss_spawned = False
    while display.Enable:
        display.Input()
        display.Update()
        # Code
        display.FillDisplay(0,0,0)
        fps_text.content = str(round(display.Clock.get_fps()))
        point_text.content = str(point)
        updatePost()
        Move()
        Reset(lava_floor)
        if point >= 200 and boss_spawned == False:
            thread2.start()
            boss_spawned = True
        display.Render()
f_MAIN()