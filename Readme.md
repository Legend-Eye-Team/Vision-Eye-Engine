# Status
[DEVLOG](Devlog.md)
- [9 dec]  Math Direction Testing ( Very Very Bug 💀 )
- [6 dec]  Math
- [5 dec] Finish effect 
<!-- - [3 dec] Testing for effect 
- [1 dec] Can't install now (Error in setup) -->

# Setup 
Create A Project
```
VisionE init <Name>
cd <Name>
python Run.py
```
# Code 
## Example
* [Block](Test/code/Block.py)
* [Effect](Test/code/Effect.py)


## Zone
In 'Main.py', have some zone. There are:
* Import (Import library and Engine)
* Initial (Create variable, Block, Gui, ...)
* Functional (Create function)
* Main (Main Function)
    - 'display.Input()' get data input
    - 'display.Update' update everything
    - 'Code' this is zone for function, code, ...
    - 'display.Render' render Block, Gui
## Create a block

### Rectangle
#### Initial
```
name_of_block = Rectangle(display,x_pos,y_pos,width,height)
```

#### Method
```
block = Rectangle(display,250,250,100,100)

# Change new size
block.Transform(50,50) 

# Change new position
block.setPoint(100,100)

# Check Human is touched
block.isTouched(player)

# Set attribute
# isFlat: Create flat by block 
block.SetAttribute("IsFlat")
```
### Image
```
image = Image.Image(display,x_pos,y_pos,source)

# Change new size
image.Transform(100,100)
```
### Human
```
player = Human.Human(Rectangle | Image)

# Note: To access Rectangle Use
# player.Rectangle

# Move Human
player.MoveTo(HUMAN_DIRECTION_RIGHT | HUMAN_DIRECTION_LEFT)

# Jump Human
player.JumpActive()

# Take Health
player.TakeHealth(damage)
```
### id of Rectangle
In a rectangle, image they are have a id. And you can get it by
```
rect = Rectangle(display,10,10,100,50)
id_rect = rect.getId()
```
Note: Gui has its own id

## Create a gui
### Text
```
# Create text
text = Gui.Text(display,<Path to font>, <Size> ,<Text>,<x_pos>,<y_pos>)
# Edit
# write to code zone
text.content = <Text>
```
### Button
I'm lazy 💀

## Create a effect
### Create
```
effect = Effect.ParticleGroup(display,<x_pos>,<y_pos>)
```
### Edit effect
#### Before create
```
def flame():
    effect.x = 100
    effect.y = 100

    effect.direction = Vector.Vector2(
        random.randint(0,20)/10-1, # move right or left
        -5)                        # for move up

    effect.color = random.choice(('red','orange','yellow'))
    effect.timeLife_perP = random.randint(10,12)
effect.updateAtt = flame
```
#### For particle ( After create )
```
fountain = Effect.ParticleGroup(display,300,300)

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
```
### Example
```
fountain = Effect.ParticleGroup(display,500,300)

def fountainCreate():
    fountain.direction = Vector.Vector2(
        random.randint(0,20)/10-1, # move right or left
        -6)                        # for move up

    fountain.color = random.choice(('blue','cyan'))
    fountain.timeLife_perP = random.randint(6,10)
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
```