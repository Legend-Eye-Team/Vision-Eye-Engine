## 0.0.1.4
from Engine import *
import random
display = Display(1000,600,DISPLAY_CAPTION)

flame = Effect.ParticleGroup(display,500,300)

def flameCreate():
    flame.x = 500
    flame.y = 300

    flame.direction = Vector.Vector2(
        random.randint(0,20)/10-1,-3)

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
fountain.updateAtt = fountainCreate

def f_MAIN():
    while display.Enable:
        display.Input()
        display.Update()
        # Code
        display.FillDisplay(0,0,23)
        display.Render()
f_MAIN()
